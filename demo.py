name = input("enter your name: " )
name = name.capitalize().strip()
while name == "": 
    
    print("you did not enter your name")
    name = input("enter your name: ")
    name = name.strip().title()

print(f"hello {name}")    


print(f"{name}, (;")

