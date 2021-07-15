try:
    with open("testing.txt") as reader:
        reader.read()

except Exception as error:
    print(error)


try:
    with open("testing.txt") as reader:
        reader.read()

except:
    print("Something went wrong")
