from utils import CSVFile
from data_extractor import DataExtractor


class DataProcessor:
    def __init__(self, customer_sample_file, customer_file, invoice_file, invoice_item_file):
        self.customer_sample_file = customer_sample_file
        self.customer_file = customer_file
        self.invoice_file = invoice_file
        self.invoice_item_file = invoice_item_file

    def read_customer_sample(self):
        customer_codes = {}
        for row in self.customer_sample_file.read():
            customer_codes[row[0]] = None
        return customer_codes

    def process_and_write_data(self):

        customer_codes = self.read_customer_sample()

        data_extractor = DataExtractor()

        for input_file, output_file in [('CUSTOMER.CSV', 'OUTPUT_CUSTOMER.CSV'),
                                        ('INVOICE.CSV', 'OUTPUT_INVOICE.CSV'),
                                        ('INVOICE_ITEM.CSV', 'OUTPUT_INVOICE_ITEM.CSV')]:
            data_extractor.extract_data(input_file, output_file, customer_codes)
