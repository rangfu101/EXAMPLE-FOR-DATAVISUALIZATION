with open('result.csv') as raw_data:
    line = raw_data.readlines()
for l in line:
    print(l)
d = {
    1: "red",
    2: "green",
    3: "blue"
}
print(d.keys())
print(d.values())
for key, value in d.items():
    print(key)
    print(value)
    print(f"the key is: {key}, and the value is: {value}")
#print("Hello")