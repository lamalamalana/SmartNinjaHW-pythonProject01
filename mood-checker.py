mood = input("How're you feeling? ").lower()

if mood == "happy":
    print("It's great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Don't be sad, be awesome instead!")
elif mood == "excited":
    print("That's awesome!")
elif mood == "relaxed":
    print("That's cool.")
else:
    print("I don't recognize this mood.")