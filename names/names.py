import time
from bst import BSTNode  # imported from my bst file.

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

the_bst = BSTNode("")  # rewuires a positional argument which is value so I decided to use empty string.
for n1 in names_1:
    the_bst.insert(n1)

for n2 in names_2:
    if n2 not in duplicates:
        if the_bst.contains(n2):
            duplicates.append(n2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# add this to the above code to see runtime!
# duplicates = set.intersection(set(names_1), set(names_2))
