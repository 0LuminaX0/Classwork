file = open("data/data.csv")
info = file.read()
print(info)

lines = info.splitlines()
print(lines)
file.close()

keys = lines[0]
#values = [i for i in lines[1:]].split("")


