

names = ["Darcy", "Elizabeth", "Bingley", "Jane", "Lydia"]

print( names[0] )
print( names[1] )

names.append("Liya")

print(names)

second_names = ["Aerin"] + names 
print(second_names)

print("------")
for string in names:
     print (string + " Hello?")
     print(string[0] + " the first letter of the name!" ) # D for "Darcy"
     for c in string:
          print(c)
print("Finished.")


for k in [0,1,2,3,4,5]:
      print(k, names[k])
      
      hundnames = [ f"nae_{i}" for i in range(100) ]
      print(hundnames)
      
      for k in range(6):
            print(k, names[k])