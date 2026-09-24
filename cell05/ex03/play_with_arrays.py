Org = [2, 8, 9, 48, 8, 22, -12, 2]
New = set()

for i in range(8):
    if Org[i] > 5:
        New.add(Org[i] + 2)

print(f"Original array: {Org}")
print(f"New array: {New}")
