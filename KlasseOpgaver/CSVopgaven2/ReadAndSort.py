
file = open("FL_insurance_sample.csv")


residentialList = []
craftList = []

for i in file:
    a = i.split(",")
    residentialList.append(a[15])
    craftList.append(a[16])



cl = set(craftList)
rl = set(residentialList)
print(cl)
cl.remove("construction")
rl.remove("line")
for r in rl:
    print(r, residentialList.count(r),)

print("\n")

for c in cl:
    print(c, craftList.count(c))


