import csv
import re


def cleanAttrib(attrib):
	cleanr = re.compile('<.*?>')
	return (re.sub(cleanr, '', attrib))

try:
	cleanFile = open("cleanData.csv", "wb")
	writer = csv.writer(cleanFile)
	f = open("currData.csv", "r+")
	with f:
		readFile = csv.reader(f)

		for row in readFile:
			if '<a href' in row[6]:
				row[6] = cleanAttrib(row[6])
				row[7] = cleanAttrib(row[7])
			writer.writerow(row)

		print "Done!"

finally:
	cleanFile.close()
	f.close()
