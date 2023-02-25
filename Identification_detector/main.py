import os

from PIL import Image

name = input("Whats your name:")

# Ask for user's identity
identification = input("Enter Your Identity: ")

# Check if the identity is correct
if identification == "Rewrite this for your identity and below mention your image path":
    # Ask for image path and open/display the image
    image_path = ("Enter the path to your image: ")
    img = Image.open(image_path)
    img.show()


elif identification == "Rewrite this for your identity and below mention your image path": #<- your identity
    # Ask for image path and open/display the image
    image_path = ("Enter the path to your image: ")
    img = Image.open(image_path)
    img.show()



else:
    # Display the message and exit
    print("\nI am gonna throw you out,.. Get lost  \n\n")
    exit()

# Ask for user's password
password = input("Please enter the password: ")

# Check if the password is correct
if password == "Enter your Password here": # <- Update Password section

    # Ask for signature path and open/display the signature image
    signature_path = ("Enter the path to your signature image: ")
    sig = Image.open(signature_path)
    sig.show()
    print(f"Here's your signature {name}")


else:
      # Exit the program
    os.system("shutdown /s /t 1")
    exit()