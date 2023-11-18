import os


print(" Starting checking ...!")
print(" Made by zNIC")

os.system("cd outputs ; cat *.txt > ../check.txt")
os.system("sudo java -jar RChecker.jar check.txt | grep SUCCESS")

print(" Do you want delete all outputs?")
select = input(" Yes/No: ")
if(select == "yes" and "y"):
    os.system("sudo rm -r check.txt")
    
elif(select == "no" and "n"):
    exit()