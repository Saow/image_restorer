from PIL import Image 
from PIL import ImageFilter
import os

def main():
    print("Welcome to the Image Filter Program")
    print("Please enter the name of the image you would like to filter")

    imageinput = input("Enter the name of the image: ")
    object = Image.open(imageinput)
    # object.show()

    while True:
        print("[1] Blur")
        print("[2] Sharpen")
        print("[3] Smooth")
        print("[4] Fast save")
        print("[5] Save as")
        print("[6] Exit")

        selectioninput = int(input("Enter the number of the filter you would like to apply: "))

        if selectioninput == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            object = object.filter(ImageFilter.BLUR)
            object.show()
            continue

        elif selectioninput == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            object = object.filter(ImageFilter.SHARPEN)
            object.show()
            continue

        elif selectioninput == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            object = object.filter(ImageFilter.SMOOTH)
            object.show()
            continue

        elif selectioninput == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            object.save("filteredimage.jpg") 
            print("Image has been saved as filteredimage.jpg")
            break

        
        elif selectioninput == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[1] JPEG")
            print("[2] PNG")
            print("[3] webp")
            print("[4] GIF")
            
            try:
                image_format = int(input("Enter the format of the image: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            if image_format == 1:
                object.save(input("Enter the name of the image you would like to save: ") + ".jpg")
                os.system('cls' if os.name == 'nt' else 'clear')
            elif image_format == 2:
                object.save(input("Enter the name of the image you would like to save: ") + ".png")
                os.system('cls' if os.name == 'nt' else 'clear')
            elif image_format == 3:
                object.save(input("Enter the name of the image you would like to save: ") + ".webp")
                os.system('cls' if os.name == 'nt' else 'clear')
            elif image_format == 4:
                object.save(input("Enter the name of the image you would like to save: ") + ".gif")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Invalid format selection.")
                continue

        elif selectioninput == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Thank you for using the Image Filter Program")
            break

        else:
            print("Invalid selection")
            continue
main()