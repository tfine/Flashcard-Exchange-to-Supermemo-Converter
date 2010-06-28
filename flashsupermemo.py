import csv

filename = "pol.csv"
readera = csv.reader(open(filename, "r"))

e = open("bird1.txt", "w")

for x in readera:
    e.write("q: ")
    e.write(x[0])
    e.write("\n")
    e.write("a: ")
    e.write(x[1])
    e.write("\n")
    e.write("\n")
    e.write("q: ")
    e.write(x[1])
    e.write("\n")
    e.write("a: ")
    e.write(x[0])
    e.write("\n")
    e.write("\n")
e.close()