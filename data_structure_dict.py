

# d:dict[str,str|list[str]] = {
#     "name":"Gaurat",
#     "firstname":"fred",
#     "job":"dev"
# }

d:dict = {
    "name":"Gaurat",
    "firstname":"fred",
    "job":"dev"
}

print(d["job"])

d["job"] = "formateur"

d["languages"] = ["Python","PHP","Javascript"]
print(d)

from pprint import  pprint
pprint(d)


for k in d:
    print(k,d[k])

keys = d.keys()
values = d.values()

for k,v in d.items():
    print(k,"=>",v)

l = ['Value 01', 'Value 02', 'Value 03', 'Value 04', 'Value 05']

# for i in range(len(l)):
for i,v in enumerate(l):
    print(i,v)
