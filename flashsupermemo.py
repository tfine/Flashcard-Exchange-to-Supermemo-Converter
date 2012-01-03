import csv
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--r", "--reverse", action="store_true", dest="reverse", 
    default=False, help="reverse questions and answers")
(options, args) = parser.parse_args()

reader = csv.reader(open(args[0], "r"))
output = open(args[1], "w")

for row in reader:
    row = tuple(cell.replace('\n', '\x02') for cell in row[:2])
    output.write("Q: %s\nA: %s\n\n" % row)
    if options.reverse:
        output.write("Q: %s\nA: %s\n\n" % row[::-1])

output.close()