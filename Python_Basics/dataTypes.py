a = 10
b, c, d = 20, 40.44, "Rupesh Modak"
print(a)
print(b)
print(c)
print(d)


print("{} {}".format("Value of b is", b))
print(type(a))
print(type(c))
print(type(d))


values = [1, 2, "Rupesh", 4, 5, 6, 7.56]
print(values)
print(values[2])
print(values[1:5])
print(values[-1])
values.insert(3, "Modak")
values.append("Advay")
del values[4]
values[5] = "Aparna"
print(values)


val = (1, 2, 3, 4)
print(val)
print(val[2])
# val[3] = "Sanav"
print(val[3])


dic = {1: "Rupesh", "a": 4.5, 2: "Modak", "b": 1991}
print(dic[1])
print(dic["b"])

dic["b"] = 2000
print(dic["b"])

dictn = {}
dictn["Firstname"] = "Rupesh"
dictn["Lastname"] = "Modak"
print(dictn)
print(dictn["Lastname"])
