from PIL import Image
import math
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    img = Image.open(filename)
    return img



# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(new_img, newfilename):
    new_img.save(newfilename)



# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
#       append adds new item to list

def obamicon(img):
    data = img.getdata() 
    new_data = []
    for pixel in data :
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            new_data.append((0, 51, 76))
        elif intensity >= 182 and intensity < 364:
            new_data.append((217, 26, 33))
        elif intensity >= 364 and intensity < 546:
            new_data.append((112, 150, 158))
        elif intensity >=546:
            new_data.append((252, 227, 166))
    
    new_image = Image.new(img.mode, img.size)
    new_image.putdata(new_data)

    return new_image

def grayscale(img):
    data = img.getdata()
    new_data = []
    for pixel in data:
        gray_value = ((pixel[0] + pixel[1] + pixel[2]) // 3)
        
        new_data.append((gray_value, gray_value, gray_value))

    new_image = Image.new(img.mode, img.size)
    new_image.putdata(new_data)

    return new_image

def invert(img):
    data = img.getdata()
    new_data = []
    for pixel in data:
        invert_r = 255 - pixel[0] 
        invert_g = 255 - pixel[1] 
        invert_b = 255 - pixel[2] 

        new_data.append((invert_r, invert_g, invert_b))

    new_image = Image.new(img.mode, img.size)
    new_image.putdata(new_data)

    return new_image

def green(img):
    data = img.getdata()
    new_data = []
    for pixel in data:
        same_red = int(pixel[0] + 0)
        more_green = int(pixel[1] + 100)
        same_blue = int(pixel[2] + 0)

        new_data.append((same_red, more_green, same_blue))
        
    new_image = Image.new(img.mode, img.size)
    new_image.putdata(new_data)

    return new_image

def emphasize(img):
    data = img.getdata()
    new_data = []
    color1 = (199, 142, 221)
    color2 = (203, 120, 38)
    for pixel in data:

        distance1 = math.sqrt(
            (pixel[0] - color1[0])**2 + 
            (pixel[1] - color1[1])**2 +
            (pixel[2] - color1[2])**2
        )
        distance2 = math.sqrt(
            (pixel[0] - color2[0])**2 + 
            (pixel[1] - color2[1])**2 +
            (pixel[2] - color2[2])**2

        )
        same_red = pixel[0]
        same_green = pixel[1]
        same_blue = pixel[2]

        if distance1 <= 60 or distance2 <= 60:
            new_data.append((same_red, same_green, same_blue))
        else:
            gray_value = ((pixel[0] + pixel[1] + pixel[2]) // 3)
        
            new_data.append((gray_value, gray_value, gray_value))

    new_image = Image.new(img.mode, img.size) 
    new_image.putdata(new_data)

    return new_image




        