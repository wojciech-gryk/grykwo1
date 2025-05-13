from datetime import datetime

with open("plik.txt", "a") as f:
    now = datetime.now()
    f.write(str(now) + "\n")
    f.writelines(str(now) + "\n")
