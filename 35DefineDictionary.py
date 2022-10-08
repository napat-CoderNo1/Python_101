# dictionary => key (access data) , value (value of data)

# define dictionary
# var = {key:value, key:value, key:value}
colors = {"red":1, 2:"yellow", "green":True}
print("key red have value = ", colors["red"])
print("key 2 have value = ", colors[2])
print("key green have value = ", colors["green"])

print("\n")

# define(constructor)
# var = dict(key = value, key = value, key = value)
animals = dict(cat = "4leg", dog = "4leg", duck = "2leg")
print(animals["dog"])

# สำหรับการประกาศเเบบ constructor จะมี {} ครอบหรือไม่ก็ได้
# animals = dict(cat = "4leg", dog = "4leg", duck = "2leg") as same as 
# animals = dict({cat = "4leg", dog = "4leg", duck = "2leg"})