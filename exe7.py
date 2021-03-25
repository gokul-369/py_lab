filelocation = str(input("Enter directory path with file & it's extension: "))#E://folder//filename.extn
file=open(filelocation,"a")        
c=input("Enter string to append: \n");
file.write("\n")
file.write(c)
file.close()
print("Contents of appended file:\n");
fileread=open(filelocation,'r')
line1=fileread.readline()
while(line1!=""):
    print(line1)
    line1=fileread.readline()    
fileread.close()
