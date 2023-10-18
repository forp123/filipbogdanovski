import csv


def find_column_index(input_filename, target_column_name):
    with open(input_filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        header = next(reader)
        target_column_name = target_column_name.strip().lower()
        for idx, column in enumerate(header):
            if column.strip().lower() == target_column_name:
                return idx
    return -1


class DataExtractor:
    def __init__(self):
        self.customer_codes_dict = {}
        self.invoice_codes_dict = {}

    def extract_data(self, input_filename, output_filename, customer_codes):
        data = []

        target_column_name = "CUSTOMER_CODE" if input_filename in ['CUSTOMER.CSV', 'INVOICE.CSV'] else "INVOICE_CODE"
        target_column_found = find_column_index(input_filename, target_column_name)

        if target_column_found == -1:
            print(f'Column "{target_column_name}" not found in {input_filename}')
            return

        invoice_code_index = -1
        if input_filename == 'INVOICE.CSV':
            invoice_code_index = find_column_index(input_filename, 'INVOICE_CODE')

        with open(input_filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            header = next(reader)
            data.append(header)

            for row in reader:

                if input_filename == 'CUSTOMER.CSV' and row[target_column_found] in customer_codes:
                    data.append(row)
                elif input_filename == 'INVOICE.CSV' and row[target_column_found] in customer_codes:
                    data.append(row)
                    if invoice_code_index != -1:
                        self.invoice_codes_dict[row[invoice_code_index]] = None
                elif input_filename == 'INVOICE_ITEM.CSV' and row[target_column_found] in self.invoice_codes_dict:
                    data.append(row)

        self.write_data(data, output_filename)

    def write_data(self, data, output_filename):

        cleaned_data = [row if not row[0].startswith('\ufeff') else [row[0][1:]] + row[1:] for row in data]

        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(cleaned_data)
