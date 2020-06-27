class College:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __hash__(self):
        return hash((self.name, self.address))
    def __eq__(self, other):
        return (self.name,self.address) == (other.name, other.address)

a = College("DYPatil","Pune")
b = College("Wadia","Pune")

dict_college = {a: 1, b: 2}

print(dict_college[a])
print(dict_college[b])

if a == b:
    print("A and B are equal")
else:
    print("A and B are not equal")