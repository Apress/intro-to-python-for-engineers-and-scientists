# Open a new file in write-binary mode

file1 = open("new.txt","wb");

# Write a string to the file

file2 = file1.write("python\nPython");

# Open the file in read and write mode

file3 = open("new.txt","r+");

# Read first five characters of the file

char10 = file3.read(10);

print "first ten characters of the file are:", char10

# close the file

file3.close();

# Check it the file has been closed
print file3.closed