from sys import argv

script, inputFile = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

currentFile = open(inputFile)

print("Print the whole file:\n")
print_all(currentFile)

print("Rewind like a tape:")
rewind(currentFile)

print("Print three lines:")
currentLine = 1
print_a_line(currentLine, currentFile)

currentLine += 1
print_a_line(currentLine, currentFile)

currentLine += 1
print_a_line(currentLine, currentFile)
print("\n")