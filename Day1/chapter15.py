from sys import argv
# my file is test.txt

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again pleaseeee:")
your_file_again = input("> ")

display_txt_again = open(your_file_again)

print(display_txt_again.read())