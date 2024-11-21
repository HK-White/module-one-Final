# Create a basic dictionary representing the Fellowship of the Ring
fellowship = {
    "Frodo": "Ring-bearer",
    "Aragorn": "Ranger of the North",
    "Legolas": "Elf of Mirkwood",
    "Gimli": "Dwarf of Erebor",
    "Boromir": "Man of Gondor",
    "Sam": "Gardener",
}

# Accessing a value by key
print(f"Frodo's role: {fellowship['Frodo']}")
print(f"Frodo's role: {fellowship['Galadriel']}")

# Using .get() to safely access keys
print(f"Galadiel's role: {fellowship.get('Galadriel')}")
print(f"Galadriel's role {fellowship.get('Galadriel', 'Not in the fellowship')}")

# Adding a new member
fellowship["Merry"] = "Hobbit of the Shire"
print("\nAfter adding Merry:", fellowship)

# Removing a member using .pop()
removed = fellowship.pop("Boromir")
print("\nRemoved Boromir:", removed)
print("After removing Boromir:", fellowship)

# Removing a member using del
del fellowship["Sam"]
print("\nAfter removing Sam with del:", fellowship)

# Modifying an element in a dictionary
fellowship["Legolas"] = "Prince of Mirkwood"
print("\nAfter modifying Legolas's role:", fellowship)

# .keys(), .values(), and .items()
print("\nMembers (keys):", fellowship.keys())
print("Roles (values):", fellowship.values())
print("Members and roles (items):", fellowship.items())

# Looping through the dictionary
print("\nLooping through dictionary:")
for member in fellowship:
    print(f"{member}")

# Looping using .keys() and .values()
print("\nLooping using keys():")
for member in fellowship.keys():
    print(f"Member: {member}")
print("\nLooping using values():")
for role in fellowship.values():
    print(f"Role: {role}")

# Nested dictionaries
middle_earth = {
    "Fellowship": fellowship,
    "Enemies": {
        "Saruman": "Corrupted Wizard",
        "Sauron": "Dark Lord",
        "Orcs": "Creatures of Mordor"
    },
}
# Accessing nested dictionaries
print("\nSauron's title:", middle_earth["Enemies"]["Sauron"])
print("\nFrodo's title:", middle_earth["Fellowship"]["Frodo"])

# Modifying a nested dictionary
middle_earth["Enemies"]["Saruman"] = "Traitorous Wizard"
print("\nAfter modifying Saruman's title:", middle_earth["Enemies"])

# Dictionaries are VERY VERY important to understand