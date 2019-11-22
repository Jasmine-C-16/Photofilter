from filters import *

def main():
    img = load_img("Ireland.jpg")
    new_image = emphasize(img)
    save_img(new_image, "Ireland_emphasize.jpg")



if __name__ == "__main__":
    main()


