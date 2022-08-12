# Importing library
import qrcode

# Data to be encoded
data = input("What is your name? ")

# Encoding data using make() function
img = qrcode.make(data)

inside = str(data) + ".png"

# Saving as an image file
img.save(inside)
