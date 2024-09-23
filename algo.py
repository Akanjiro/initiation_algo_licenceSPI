
# Exercice 4
A = 2
print(A)
B = 5
A = B
print(A, B)
B = A + 3 * B
print(B)
C = A * 2 + B
print(C)
C = B - A
print(C)

# Exercice 6
# Petit 1
A = 7
B = 3
print("A vaut", A, "et","B vaut", B)
# A prends la valeur de B
A = B
print("Nouvelle valeur de A est", A, "B vaut toujours", B)
# B prends la valeur de A
B = A
print("Nouvelle valeur de B est", B, "A vaut toujours", A)

# Petit 2
print("écrire V1")
v1 = int(input("v1 = "))
print(v1)
print("écrire v2")
v2 = int(input("v2 = "))
print("Avant permutation")
print("v1 = " + str(v1))
print("v2 = " + str(v2))
v1 = v2
v2 = v1
print("Après permutation")
print("v1 = " + str(v1))
print("v2 = " + str(v2))

# Faire une permutation entre 3 nombres, a, b c, contenu de a va dans b, contenu de b va dans c,
