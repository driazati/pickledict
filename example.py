from pickledict import jsondict

my_dict = jsondict(some_key="a value")

# Writes and modifications are automatically recorded and saved
my_dict["dog"] = 1
my_dict["dog"] += 1

print(my_dict)
