# read an image
try:
    with open("image01.png", "rb") as ifile:
        image_data = ifile.read()
        print(image_data)

    # copy the image
    with open("copy_image.png", "wb") as ofile:
        ofile.write(image_data)

        # ifile.close()
        # ofile.close()
except FileNotFoundError as e:
    print(e)
    
print("Finished executing.")