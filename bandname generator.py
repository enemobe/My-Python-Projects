print("Hi! Welcome to Bandname Generator")
name = input("Enter your name: ")
animal = input("Enter your favorite animal: ")
city_state = input("Enter your city/state of birth: ")
if animal.endswith("sh"):
    print(f"Dear {name}, Your Bandname is {city_state} {animal}es.")
elif animal.endswith("y"):
    print(f"Dear {name}, Your Bandname is {city_state} {animal}ies.")
elif animal.endswith("f"):
    print(f"Dear {name}, Your Bandname is {city_state} {animal}ves.")
else:
    print(f"Dear {name}, Your Bandname is {city_state} {animal}s.")