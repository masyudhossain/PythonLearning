# Write a program to greet all the person names stored in a list ‘l’ and which starts with M. 
# l = ["Masyud", "Sohom", "Minhaz", "Rahul"]
l = ["Masyud", "Sohom", "Minhaz", "Rahul"]

for name in l:
    if(name.startswith("M")):
        print(f"Assalamualikum {name}")