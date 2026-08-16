#Reading file contents
"""with open("security.log","r") as file:
    content=file.read()
    print(content)"""

#Writing to a file
"""with open("names.txt","w") as file:
    content=file.write("Abdirahman Ahmed \nAyaan Ahmed \nShukri Ahmed")
    print(content)"""

#Appending to a file
"""with open("names.txt","a") as file:
    file.write("\nAbdirahman Ahmed")"""

#Streaming line by line
"""with open("names.txt","r") as file:
    for line in file:
        print(line.strip())"""

with open("report.txt","w") as file:
    file.write("Bronze layer processed: 500 records\n")
with open("report.txt","a") as file:
    file.write("Silver layer processed: 480 records\n")