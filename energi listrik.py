print("="*40)
print("RUMUS ENERGI LISTRIK")
print("="*40)

v = int(input("Potensial listrik: "))
l = int(input("Kuat arus listrik: "))
q = int(input("Muatan listrik: "))
r = int(input("Hambatan: "))
t = int(input("Waktu: "))

epl = q * v
eldr = l * l * r * t

print(f"Energi potensial listrik = {epl}")
print(f"Energi listrik dalam rangkaian = {eldr}")