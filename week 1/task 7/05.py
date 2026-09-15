my_set = {1, 2, 3, 4, 5}
print(f"\nOriginal Set: {my_set}")
my_set.add(6)
print(f"After add(6): {my_set}")
my_set.remove(2)
print(f"After remove(2): {my_set}")

another_set = {4, 5, 6, 7, 8}
print(f"Another Set: {another_set}")
print(f"Union: {my_set.union(another_set)}")
print(f"Intersection: {my_set.intersection(another_set)}")