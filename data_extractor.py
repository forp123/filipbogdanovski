import csv


class DataExtractor:
    def __init__(self):
        self.customer_codes_dict = {}
        self.invoice_codes_dict = {}

    def extract_data(self, input_filename, output_filename, customer_codes):
        data = []

        with open(input_filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data.append(header)

            for row in reader:
                # print(f"Checking row[0]: {row[0]}")
                # print(row)
                # print(f"Keys in invoice_codes: {self.invoice_codes.keys()}")
                # print(f"{input_filename}, {row[0]}")
                # print(f"{self.invoice_codes}")
                if input_filename == 'CUSTOMER.CSV' and row[0] in customer_codes:
                    data.append(row)
                elif input_filename == 'INVOICE.CSV' and row[0] in customer_codes:
                    data.append(row)
                    self.invoice_codes_dict[row[1]] = None
                elif input_filename == 'INVOICE_ITEM.CSV' and row[0] in self.invoice_codes_dict:
                    # print(f"Should add row: {row}")
                    data.append(row)

        self.write_data(data, output_filename)

    def write_data(self, data, output_filename):

        cleaned_data = [row if not row[0].startswith('\ufeff') else [row[0][1:]] + row[1:] for row in data]

        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(cleaned_data)
