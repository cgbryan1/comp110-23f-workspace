"""Practice with Dictionaries."""

# Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

print(ice_cream)

# Adding key-value pair to dictionary
ice_cream["mint"] = 3

print("After adding mint:")
print(ice_cream)

# Removing key-value pair from dictionary
ice_cream.pop("mint")

print("After removing mint:")
print(ice_cream)

print(f"There are {ice_cream['chocolate']} orders of chocolate.")
ice_cream["vanilla"] = 10

print(f"The number of my ice cream flavors is {len(ice_cream)}")

if ("mint" in ice_cream):
    print(ice_cream["mint"])
else:
    print("no orders of mint.")

print("Is chocolate in my list?")
print("chocolate" in ice_cream)

print(len(ice_cream))

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders")