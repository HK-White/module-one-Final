'''
Sets: Unordered collections of unique (no repeats, one of each value max) that 
are common for unique requiring tasks or use cases

Used for: usernamed, passwords, checking redeem codes
'''

fellowship = set()

fellowship.add("Matt")
fellowship.add("Jesse")
fellowship.add("Milo")

enemies = set()

enemies.add("Kirby")
enemies.add("Matt")
print("\nIs Kirby in the fellowship?", "Kirby" in fellowship)



"""
In Python, a set is an unordered collection of unique elements. 
It is defined using curly braces {} or the set() constructor. 

Key Characteristics of Sets:
Unique Elements: A set automatically removes duplicate elements.
Unordered: The elements in a set do not have a defined order 
    and cannot be accessed by index.
Mutable: Sets themselves can be modified (adding or removing elements), 
    but the elements in a set are immutable (e.g., numbers, strings, tuples).
    
Common uses: removing duplicates, checking memberships (emails, ips, usernames),
    tracking unique visits to a website, checking password against set of
    commonly used passwords, game inventories, etc
"""

# Validation of Membership or Inclusion: 
# Is my group (heroes) a part of their group (fellowship)"
# Use issubset() to ensure that a smaller collection (heroes) 
# is fully satisfied by a larger collection (fellowship).
# Examples - graduation requirements | read/write permissions
print("\nAre all heroes in the fellowship?", enemies.issubset(fellowship))
# Containment or Ownership Testing
# Does my group (fellowship) contain their group (heroes)?
# Use issuperset() to confirm that one set (fellowship) 
# includes all elements of another (heroes)
# Examples - catalog of items | making sure a catalog contains all items
print("Does the fellowship contain all the heroes?", fellowship.issuperset(heroes))

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True

"""
Summary Analogy:
issubset(): "Do my skills meet the job requirements?"
issuperset(): "Does my toolbox contain all the tools needed for the task?"
"""
# Add a duplicate list of hobbits and remove duplicates using a set
hobbits_list = ["Frodo", "Sam", "Merry", "Pippin", "Frodo", "Sam"]
unique_hobbits = set(hobbits_list)
print(f"\nUnique hobbits after removing duplicates: {unique_hobbits}")

heroes_in_fellowship = fellowship.intersection(enemies)