print("Input .n to exit the loop")
while True:
    filename = input("Input the Filename: ")
    f = filename.split(".")
    if f[-1]=="py":
        x="python"
    elif f[-1]=="C" or f[-1]=="c":
        x="C"
    elif f[-1]=="h":
        x="C++"
    elif f[-1]=="java":
        x="Java"
    elif f[-1]=="n":
        break
    else:
        x="Unknown"
    print ("The extension of the file is:",x)
    
