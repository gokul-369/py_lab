filename=str(input("Enter the name of the file with its extension : "))
baselocation="C:\\Users\\LENOVO\\py lab\\"
filelocation=baselocation+filename
file=open(filelocation,"r")
line=file.readline()
while(line!=""):
    print("file opened...!\n")
    print(line)
    line=file.readline()
file.close()

