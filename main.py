from PIL import Image 
from PIL import ImageFilter
import os

def main():
    print("Welcome to the Image Filter Program")
    print("Please enter the name of the image you would like to filter")

    imageinput = input("Enter the name of the image: ")
    object = Image.open(imageinput)
    object.show()

    while True:
        print("[1] Blur")
        print("[2] Sharpen")
        print("[3] Smooth")
        print("[4] Fast save")
        print("[5] Save as")
        print("[6] Exit")

        selectioninput = int(input("Enter the number of the filter you would like to apply: "))

        if selectioninput == 1:
            object = object.filter(ImageFilter.BLUR)
            object.show()
            continue

        elif selectioninput == 2:
            object = object.filter(ImageFilter.SHARPEN)
            object.show()
            continue

        elif selectioninput == 3:
            object = object.filter(ImageFilter.SMOOTH)
            object.show()
            continue

        elif selectioninput == 4:
            object.save("filteredimage.jpg") 
            print("Image has been saved as filteredimage.jpg")
            break

        elif selectioninput == 5:
            print("[1] JPEG")
            print("[2] PNG")
            print("[3] webp")
            print("[5] gif")
            format = input(int("Enter the format of the image: "))
            if format == 1:
                saveimg = object.save(input("Enter the name of the image you would like to save: ") + ".jpg")
            elif format == 2:
                saveimg = object.save(input("Enter the name of the image you would like to save: ") + ".png")
            elif format == 3:
                saveimg = object.save(input("Enter the name of the image you would like to save: ") + ".webp")
            elif format == 4:
                saveimg = object.save(input("Enter the name of the image you would like to save: ") + ".gif")
            else:
                continue
            print("Image has been saved as " + saveimg)
            break

        elif selectioninput == 6:
            print("Thank you for using the Image Filter Program")
            break

        else:
            print("Invalid selection")
            continue
if __name__ == "__main__":
    main()

