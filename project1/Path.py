from pathlib import Path
path=Path("../training") /"report.txt"
with open(path,"r",encoding="utf-8") as file:
    data=file.read()
    print(data)