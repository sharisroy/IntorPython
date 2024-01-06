a = 10
print(a)
print(type(a))
                                    # List
value = [1,2,3,"Haris", "Roy", 5]
print(value)
print(value[1])
print(value[3])
print(value[1:5])
print(value[:2])
print(value[3:])
value.insert(4,"Chandra") # [1, 2, 3, 'Haris', 'Chandra', 'Roy', 5]
print(value[4])
print(value)
value.append("Last") # [1, 2, 3, 'Haris', 'Chandra', 'Roy', 5, 'Last']
print(value)
del value[0] #[2, 3, 'Haris', 'Chandra', 'Roy', 5, 'Last']
print(value)

                # Tuple - immutable
value = (1,2,3,"Haris", "Roy", 5)
print(value)
print(value.index("Haris"))

                #  Dictionary
dic = {1: "Haris", "a": 2, "b": "Chandra Roy", 3: 100}
print(dic)
print(dic[1])
print(dic["a"])
print(dic["a"])
print(dic[3])

d = {}
d["firstName"] = "Haris"
d["lastname"] = "Chandra Roy"
d["age"] = 30

print(d)
print(d["firstName"])
print(d["age"])
