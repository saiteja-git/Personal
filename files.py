import os
if os.path.exists("Demofile2.txt"):
    os.remove("Demofile2.txt")
else:
    print("File does not exist")
