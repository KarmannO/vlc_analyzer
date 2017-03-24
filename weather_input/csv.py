import csv
import datetime

class CSVInput:
    def __init__(self):
        self.temperature_dict = {}

    def read(self, filename):
        with open(filename, encoding='utf-16') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                if len(row) >= 2:
                    try:
                        self.temperature_dict[row[0]] = float(row[1])
                    except:
                        continue

    def get_temperature(self):
        return self.temperature_dict