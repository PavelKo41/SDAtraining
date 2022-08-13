import os
"""

File operations :
    -Creating
    -reading
    -updating
    -deleting

open(<<filename>>,<<mode>>)

r = read - open for reading(default), error if no file exists
w = write - open file for writing, creates if not exists (opens in start of file)
a = append - open the file for appending, if file not exists,it creates the file (opens in end of file)
x = create - create a new file, error if no file

t = text mode (default)
b = binary



"""
# read a file
f = open("test.txt")
print(f.read())
f.close()   # vsegda zakrqvat


f = open("test.txt", "w")
f.write(" \n Ohh, it is goigng to rain. \n Nice nice nice")
f.close()

with open("test.txt", "a") as f:
    f.write("\n Bla Bla Bla. \n too hard to understand")

if os.path.exists("tests.txt"):
    os.remove("tests.txt")

