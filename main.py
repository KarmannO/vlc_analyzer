from weather_input import csv
from volcanoes_input import archive
import matplotlib.pyplot as plt


filename = 'files/25-02-2014_31-03-2017.csv'
importer = csv.CSVInput()
importer.read(filename)

temp = importer.get_temperature()
getter = archive.ArchiveGetter()



