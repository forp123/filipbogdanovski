from utils import CSVFile
from data_processor import DataProcessor


if __name__ == '__main__':
    customer_sample_file = CSVFile('CUSTOMER_SAMPLE.CSV')
    customer_file = CSVFile('CUSTOMER.CSV')
    invoice_file = CSVFile('INVOICE.CSV')
    invoice_item_file = CSVFile('INVOICE_ITEM.CSV')

    data_processor = DataProcessor(customer_sample_file, customer_file, invoice_file, invoice_item_file)
    data_processor.process_and_write_data()
