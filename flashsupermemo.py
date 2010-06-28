#converter for CSV Flashcard Exchange Format to Supermemo Q&A
#entered into public domain by Todd Fine

import csv
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--r", "--reverse",
                  action="store_true", dest="reverse", default=False,
                  help="reverse questions and answers")
(options, args) = parser.parse_args()

filename = arg[0]
readera = csv.reader(open(filename, "r"))

e = open(arg[1], "w")

for x in readera:
    e.write("q: ")
    e.write(x[0])
    e.write("\n")
    e.write("a: ")
    e.write(x[1])
    e.write("\n")
    e.write("\n")
    if options.reverse:
        e.write("q: ")
        e.write(x[1])
        e.write("\n")
        e.write("a: ")
        e.write(x[0])
        e.write("\n")
        e.write("\n")
e.close()