import csv
import sys
from header import *

dirty_file = sys.argv[1]
clean_file = sys.argv[2]

# copy all columns except search fields
print "Copying data into {}...".format(clean_file)
with open(dirty_file, 'rb') as dirty, open(clean_file, 'wb') as clean:
    reader = csv.reader(dirty, delimiter=',')
    writer = csv.writer(clean, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

    next(reader)
    for row in reader:
        writer.writerow(row[3:])

# remove duplicate rows
print "Removing duplicate rows..."
with open(clean_file, "r") as reader:
    lines = reader.read().split("\n")

with open(clean_file, "w") as writer:
    csv.DictWriter(writer, fieldnames = header[3:], delimiter = ',').writeheader()

    for line in set(lines):
        if line:
            writer.write(line + "\n")
