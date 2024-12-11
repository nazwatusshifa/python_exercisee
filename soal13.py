print
print
print

huruf = input("Masukan huruf: ")
vokal = [
    "a", 
    "i", 
    "u", 
    "e", 
    "o"
]

if huruf in vokal :
    print("Ini Vokal")
elif huruf.isdigit() :
   print("Ini Angka")
else :
    print("Ini Konsonan")