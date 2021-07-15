a = 9

if a >= 10:
    print("Condition matches")
else:
    print("Condition does not match")

print("code ended")

summation = 0
for j in range(5, 10):
    summation = summation + j
print(summation)

for k in range(1, 10, 2):
    print(k)
print("******************************")
for l in range(20):
    print(l)
print("******************************")

list = [1, 2, 3, 4, 5, 6, 7, 8]
for m in list[1:8]:
    print(m)

print("******************************")

a = 0
while a<5:
    a = a + 1
    if a == 2:
        continue
    if a == 4:
        break
    print(a)



