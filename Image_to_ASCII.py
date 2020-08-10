from PIL import Image
import sys,os
from pathlib import Path

x_pixels = 0
y_pixels = 0

def fill_image(ascii_image, pixels):
    for i in range (0, len(ascii_image) - 1):
        for j in range(0, len(ascii_image[0]) - 1):
            if (pixels[j,i] < 32):
                ascii_image[i][j] = "m"
            elif (pixels[j,i] < 64):
                ascii_image[i][j] = "w"
            elif (pixels[j,i] < 128):
                ascii_image[i][j] = "o"
            elif (pixels[j,i] < 150):
                ascii_image[i][j] = ":"
            else:
                ascii_image[i][j] = " "

    return ascii_image

def write_txt(txt_address, ascii_image):
    txt = open(txt_address, "w")

    for i in range (len(ascii_image)):
        my_list = []

        for elem in ascii_image[i]:
            my_list.append(str(elem))

        str_row = "".join(my_list)

        txt.write(str_row + "\n")


def create_empty (n,m):
    ascii_image = [0] * m

    for i in range(m):
        ascii_image[i] = [0]*n

    return ascii_image

def read_picture(address): 
    my_image = Image.open(address) # opening picture

    if (my_image.width > 315):
        my_image = my_image.resize( (315, my_image.height) )

    if (my_image.height > 75):
        my_image = my_image.resize( (my_image.width, 75) )
    
    my_image = my_image.convert("L") # converting to grayscale 
    my_image.show()
    
    global x_pixels
    global y_pixels

    x_pixels = my_image.size[0] # size (pixels) along the x axis
    print ("X",x_pixels)
    y_pixels = my_image.size[1] # size (pixels) along the y axis
    print ("Y",y_pixels)
    pixels = my_image.load() # reading pixel values

    return pixels

def main(argv):
    image_address = "C:\\Users\\Korisnik\\Desktop\\obama.jpg"
    txt_address = "C:\\Users\\Korisnik\\Desktop\\ASCII.txt"

    print("Reading pixels!")
    pixels = read_picture(image_address)

    print("Creating empty!")
    ascii_image = create_empty(x_pixels, y_pixels)

    print("Filling!")
    ascii_image = fill_image(ascii_image, pixels)
      
    print("Writing!")
    write_txt (txt_address, ascii_image)

    print("Done!")

if __name__ == "__main__":
    main(sys.argv[1:])
