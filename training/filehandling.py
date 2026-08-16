"""with open("security.log","r") as file:
    content=file.read()
    print(content)"""

"""with open("names.txt","w") as file:
    content=file.write("Abdirahman Ahmed \nAyaan Ahmed \nShukri Ahmed")
    print(content)"""


file=r"C:\Users\user\OneDrive\Desktop\cloud-security-journey\auth.log"
with open(file,"r") as file:
    print(file.readline())
    print(file.readline())