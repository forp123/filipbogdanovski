import csv


class CSVFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            yield next(reader)
            for row in reader:
                yield row


