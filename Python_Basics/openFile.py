# file = open("Test.txt")
# line = file.readline()
# while line != "":
#    print(line)
#    line = file.readline()

# for line in file.readlines():
#     print(line)
# file.close()

with open("Test.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("Test.txt", "w") as writer:
        writer.writelines(reversed(content))
        #for line in reversed(content):
            #writer.write(line)



