"""Convert the OS based program into a menu driven program using Python Code which
 will execute the required user query when user will give the input as a text."""
import pyttsx3
import os
import pyttsx3
print(">>>"+"_"*30+"<<<")
print("   WELCOME TO IIEC-RISE COMMUNITY")
print(">>>"+"_"*30+"<<<\n")
print(">>>"+"_"*85+"<<<")
print('''   This is python program to convert the OS based program into a menu driven program 
   will execute the required user query when user will give the input as a text.''')
print(">>>"+"_"*85+"<<<\n")

while True:
    command = input("Type the application name to open the application or type exit to close:")
    if(command != "exit"):
        os.system("start {}".format(command))
        pyttsx3.speak("{} opened successfully".format(command))
    else:exit()