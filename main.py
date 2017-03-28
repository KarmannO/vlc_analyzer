from weather_input import csv
import sys
from volcanoes_input import archive
import matplotlib.pyplot as plt

# Get weather.
filename = 'files/25-02-2014_31-03-2017.csv'
importer = csv.CSVInput()
importer.read(filename)

# Get archive images.
temp = importer.get_temperature()
getter = archive.ArchiveGetter([2015, 2016])

if 'pageloading' in sys.argv:
    getter.load_pages()
if 'imageloading' in sys.argv:
    getter.load_images()

# Extract archive photos timestamps.

# Compare weather timestamps with archive photos timestamps.

# Get



