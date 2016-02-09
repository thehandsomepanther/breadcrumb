import csv
import sys
import fileinput

dirty_file = sys.argv[1]
clean_file = sys.argv[2]

# copy all columns except search fields
print "Copying data into {}...".format(clean_file)
with open(dirty_file, 'rb') as dirty, open(clean_file, 'wb') as clean:
    reader = csv.reader(dirty, delimiter=',')
    writer = csv.writer(clean, delimiter=',')

    for row in reader:
        # print "{} {}-{}".format()
        clean.write(",".join(row[3:]))
        clean.write('\n')

# remove duplicate rows
print "Removing duplicate rows..."
with open(clean_file, "r") as reader:
    lines = reader.read().split("\n")

with open(clean_file, "w") as writer:
    for line in set(lines):
        if line:
            writer.write(line + "\n")
