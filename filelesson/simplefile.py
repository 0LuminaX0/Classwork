import os.path


file = open("data/data.csv")
info = file.read()
print(info)
file.close()


lines = info.splitlines()
#print(lines)
file.close()

keys = lines[0].split(", ")
values = lines[1].split(", ")
print(keys,"\n",values)

petro = dict()
#for i in keys:
 #   if i in petro:
 #
  #  else:
  #      petro[i] = values(keys.index(i)
for index in range(len(keys)):
    petro[keys[index]] = values[index]
print(petro)

#values = [i for i in lines[1:]].split("")


