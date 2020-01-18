import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 7:
        title, publication, author, date, content, climate_change, immigration = data
        print "{0}\t{1}".format(publication, immigration)