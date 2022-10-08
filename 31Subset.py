# issubset()
fish = {"salmon", "shark", "dolphin", "piranya"}
x = {"salmon", "shark"}
y = {"piranya", "m16"}
print("x is subset of fish : ", x.issubset(fish))
print("y is subset of fish : ", y.issubset(fish))
print("\n")

# issuperset()
a = {"shark", "piranya"}
b = {"salmon", "m4a1"}
print("fish is superset of  a : ", fish.issuperset(a))
print("fish is superset of  b : ", fish.issuperset(b))
print("\n")