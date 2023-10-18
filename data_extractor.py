import csv

CUSTOMER_CSV = "CUSTOMER.CSV"
INVOICE_CSV = "INVOICE.CSV"
INVOICE_ITEM_CSV = "INVOICE_ITEM.CSV"

INVOICE_CODE_COLUMN_NAME = "INVOICE_CODE"
CUSTOMER_CODE_COLUMN_NAME = "CUSTOMER_CODE"




def find_column_index(header, target_column_name):
    target_column_name = target_column_name.strip().lower()
    for idx, column in enumerate(header):
        if column.strip().lower() == target_column_name:
            return idx
    return -1


class DataExtractor:
    def __init__(self):
        self.customer_codes = set()
        self.invoice_codes = set()

    def extract_data(self, input_filename, output_filename, customer_codes):

        with open(input_filename, 'r', encoding='utf-8-sig') as input_file, open(output_filename, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            header = next(reader)
            writer.writerow(header)

            customer_code_index = -1
            if input_filename == CUSTOMER_CSV or INVOICE_CSV:
                customer_code_index = find_column_index(header, CUSTOMER_CODE_COLUMN_NAME)
            print(f'Column "{CUSTOMER_CODE_COLUMN_NAME}" index in file: {input_filename} is {customer_code_index}')

            invoice_code_index = -1
            if input_filename == INVOICE_CSV or INVOICE_ITEM_CSV:
                invoice_code_index = find_column_index(header, INVOICE_CODE_COLUMN_NAME)

            print(f'Column "{INVOICE_CODE_COLUMN_NAME}" index in file: {input_filename} is {invoice_code_index}')

            for row in reader:

                if input_filename == CUSTOMER_CSV and row[customer_code_index] in customer_codes:
                    writer.writerow(row)

                elif input_filename == INVOICE_CSV and row[customer_code_index] in customer_codes:
                    writer.writerow(row)
                    if invoice_code_index != -1:
                        self.invoice_codes.add(row[invoice_code_index])

                elif input_filename == INVOICE_ITEM_CSV and row[invoice_code_index] in self.invoice_codes:
                    writer.writerow(row)



