
A = set(range(1, 26))

B = set()
C = set()

for x in A:
    if x % 3 == 0:
        B.add(x)
    else:
        C.add(x)

print("Множина A:", sorted(A))
print("Множина B (діляться на 3):", sorted(B))
print("Множина C (не діляться на 3):", sorted(C))
