    #  fp = open("myfile.txt","w")
    #  fp.write("Hello World! It's Asmita.")
    #  fp.close() 

def writetext(mytext) : 
     fp = open("myfile.txt","w")   
     fp.write(mytext)
     fp.close()

filename = input ("filename : ")
with open(filename,"w")as fp:
       fp.write(input())

def readtext() :
     fp = open("myfile.txt","r") 
     text = fp.read()
     print("read file :",text)
     fp.close()

def appendtext() :
     fp = open("myfile.txt","a")
     print("")

writetext(input("Enter whatever you want :"))
readtext()
 