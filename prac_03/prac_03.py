# Read a file and print only lines starting with #


def main():
    """Ask user for file name and call the functions"""
    file_name = input("Enter file name: ")
    read_file(file_name)
    first_line(file_name)
    read_lines(file_name)
    add_to_file()
    write_to_file()
    writelines_to_file()


def read_file(file_name):
    """Read lines in file starting with #"""
    in_file = open(file_name, "r")  # Can also do open(filename) then in_file.read()
    for line in in_file:
        if line.startswith("#"):
            print(line, end="")
    print()
    in_file.close()


def first_line(file_name):
    """Reading one line at a time"""
    in_file = open(file_name, "r")
    line = in_file.readline()
    print(line, end="")
    in_file.close()


def read_lines(file_name):
    """Read lines as list"""
    in_file = open(file_name, "r")
    content = in_file.readlines()
    print(content)
    in_file.close()


def add_to_file():
    """Adds text to a file (creates a file if it doesn't exist)"""
    out_file = open("demo.txt", "w")       # Change w to a, this appends instead of overwriting
    print("I like Python", file=out_file)  # Old content gets overwritten | Print always goes to new line
    out_file.close()


def write_to_file():
    """Writes text to a file (same line)"""
    out_file = open("demo.txt", "a")
    out_file.write("I like Python")  # Continues on the same line, it does not add a break
    out_file.close()


def writelines_to_file():
    """Add a list to a file"""
    countries = ["Italy", "France", "Germany", "Singapore", "Switzerland", "United Kingdom"]

    out_file = open("demo.txt", "a")
    out_file.writelines(countries)  # Continues on the same line, it does not add a break or space
    out_file.close()


main()


# -------------------------------------------------
# \t does tab space, \n is new line
# sep arranges the space between the string and variable

s = "\tPython, Monty"
print(s[1], ".", sep="")         # Outputs P.
print(s.strip, ".", sep="")      # Python, Monty. (Remove any whitespace before and after)
s.replace('', '*')   #
print(s.lstrip(), ".", sep="")   #
print(s.strip(), ".", sep="")    #


"""asking user name and putting name in file, opening and closing file using with"""
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)
print("Done")


"""creating files called name.txt from names, then print name and index in the file"""
def main():
    names = ["Bob", "Joe", "Alice"]
    create_new_file(names)

def create_new_file(names):
    for i in range(len(names)):
        with open(f"{names[i]}.txt", "w") as out_file:
            print(i+1, names[i], file=out_file)
main()

"""types of errors when printing in python"""
name = "Biden"
try:
    print(name1)
except NameError:
    print("Variable name not found")

try:
    print(123 + "abc")
except TypeError:
    print("Object type error")

names = ["Bob", "Joe", "Alice"]
try:
    print(names[3])
except IndexError:
    print("Index out of range")