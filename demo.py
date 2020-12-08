a1 =set(["A", "n"])
a2 =set(["a", "x"])

print(len(set([a.lower() for a in a1]).intersection(a2)))