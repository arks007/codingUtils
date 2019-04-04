# Author: Sujoy Purkayastha
# Last Modified: 4/3/2019
# Details: a python script to automatically generate getters and setters for java classes

# !/usr/bin/env python3

  
print("Please type your instance varibles to process followed by their respective types (int, char, etc).\nWhen you are done, type 'q' \n")


instanceVarsArray = []
typesArray = []
i = 1
entryInsVar = ""
entryType = ""

while(True):
    entryInsVar = str(input("Enter instance variable #" + str(i) +": "))
    if(entryInsVar == "q"):
        break
    entryType = str(input("Enter the type of " + entryInsVar + ": "))
    if(entryType == "q"):
        break
    
    instanceVarsArray.append(entryInsVar)
    typesArray.append(entryType)
    
    i += 1

print("\n")

writeFile = open("getSetGenFile.txt", "w+")

j = 0
for x in instanceVarsArray:
    #print(chr(ord(x[0]) - 32))     
    writeFile.write("public " + typesArray[j] + " get" + str(chr(ord(x[0]) - 32)) + x[1:len(x)] + "(){ \n \treturn" + x + "; \n} \n\n")    
    print("public " + typesArray[j] + " get" + str(chr(ord(x[0]) - 32))+ x[1:len(x)] + "(){ \n \treturn " + x + "; \n} \n\n")
    writeFile.write("public" + typesArray[j] + "set" + str(chr(ord(x[0]) - 32))+ x[1:len(x)] + "(" + typesArray[j] + " new" + str(chr(ord(x[0]) - 32))+ x[1:len(x)] + "){ \n \t" + x + "; \n} \n\n")    
    print("public void set" + str(chr(ord(x[0]) - 32))+ x[1:len(x)] + "(" + typesArray[j] + " new" + str(chr(ord(x[0]) - 32))+ x[1:len(x)] + "){ \n \t" + x + " = " + " new" + str(chr(ord(x[0]) - 32))+ x[1:len(x)] + "; \n} \n\n")          
    j += 1

    
    

