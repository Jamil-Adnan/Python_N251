"""
We are going to create a file, open and read it. first creating a separate text file named test.txt
"""
# file = open ("test.txt", "r").read()
# file = open ("test.txt", "r").readline()
# file = open ("test.txt", "r").readlines()
# print (file)

"""
Now we are goint to write a file
"""

# file = open ("test1.txt", "w")
# for i in range(10):
#     file.write(f"I am Adnan Jamil {i+1}\n")
    
# #file.close()    #closes and frees up the ram.

"""
To continue writing on a file use "a" mode (append)
"""

# file = open ("test.txt", "a")
# file.write("Hello world")

"""
To both read and write use "w+ mode"
"""
# file = open ("sample.txt" , "w+")

# file.write("This is Adnan")

# file.seek(0)

# data = file.read()
# print (data)

"""a+ mode"""

file = open ("sample.txt", "a+")
file.seek(0)
data = file.read()
print (data)
#file.seek(0)
file.write("\nI am from Bangladesh. \nI am feeling good today\n")
file.seek(0)
data = file.read()
print (data)
file.close()