import cv2
import numpy as np
from tkinter import filedialog

def load_image():
    path = filedialog.askopenfilename(title = "Select an Image: ")
    img = cv2.imread(path)
    return img

def display_image(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image (img):
    cv2.imwrite('image_opencv.png', img)

def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale', img)
    cv2.waitKey(0)
    return img

def inversion (img):
    img = 255 - img
    cv2.imshow('Inversion', img)
    cv2.waitKey(0)
    return img

def brightness (img):
    lvl = int (input("Press 1 to increase or 0 to decrease: "))
    if lvl == 1:
        img = img + 10
        img = np.clip (img, 0, 255)
        cv2.imshow('Brightness', img)
        cv2.waitKey(0)
        return img
    elif lvl == 0:
        img = img - 10
        img = np.clip(img, 0, 255)
        cv2.imshow('Brightness', img)
        cv2.waitKey(0)
        return img
    else:
        print("Invalid input.")
        return img

def resize_img (img):
    p,y = map(int ,input ("Enter resize values:").split())
    img = cv2.resize(img,(p,y))
    cv2.imshow('Resize', img)
    cv2.waitKey(0)
    return img

def crop_img (img):
    x1,x2,y1,y2 = map(int ,input ("Enter crop values (first horizontal then vertical):").split())
    img = img[x1:x2, y1:y2]
    cv2.imshow('Crop', img)
    cv2.waitKey(0)
    return img

def rotate_img (img):
    if len(img.shape) == 3:
        height, width, c = img.shape
    else:  # grayscale
        height, width = img.shape
    x_pos = width / 2
    y_pos = height / 2
    ang = int (input ("Enter rotation angle:"))
    rotation_matrix = cv2.getRotationMatrix2D((x_pos,y_pos),ang,1)
    img = cv2.warpAffine (img,rotation_matrix,(width,height))
    cv2.imshow('Rotate', img)
    cv2.waitKey(0)
    return img

def flip_img (img):
    flip = int (input ("Enter flipping value (0 for vertical flip, 1 for horizontal flip): "))
    img = cv2.flip(img,flip)
    cv2.imshow('Flip', img)
    cv2.waitKey(0)
    return img

def blur_img (img):
    img = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow('Blur', img)
    cv2.waitKey(0)
    return img

def edge_detection (img):
    img = cv2.Canny(img,100,200)
    cv2.imshow('Edge Detection', img)
    cv2.waitKey(0)
    return img

def shapes (img):
    s = input ('What shape do you want? (r for rectangle, l for line, c for circle): ')
    if s == 'r':
        p1,q1,p2,q2 = map (int, input ('Enter coordinates of side of rectangle: (p1 q1 p2 q2):\n').split())
        r,g,b = map (int, input ('Enter color of rectangle: (r g b):\n').split())
        t = int( input ('Enter thickness of rectangle:\n'))
        img = cv2.rectangle(img,(p1,q1),(p2,q2),(r,g,b),t)
        cv2.imshow('Rectangle', img)
        cv2.waitKey (0)
        return img
    elif s == 'l':
        s1, t1, s2, t2 = map(int, input('Enter coordinates of side of rectangle: (s1 t1 s2 t2):\n').split())
        r, g, b = map(int, input('Enter color of rectangle: (r g b):\n').split())
        t = int(input('Enter thickness of rectangle:\n'))
        img = cv2.line(img, (s1, t1), (s2, t2), (r, g, b), t)
        cv2.imshow('Rectangle', img)
        cv2.waitKey(0)
        return img
    elif s == 'c':
        m , n = map (int, input ('Enter coordinates of circle center: (m n):\n').split())
        rad = int (input ('Enter radius of circle:\n'))
        r, g, b = map(int, input('Enter color of circle: (r g b):\n').split())
        t = int(input('Enter thickness of circle:\n'))
        img = cv2.circle(img, (m,n), rad, (r,g,b), t)
        cv2.imshow('Circle', img)
        cv2.waitKey(0)
        return img
    else:
        print("Invalid input.")
        return img

def add_text (img):
    txt = input ('Enter text (enter to quit): ')
    posx, posy = map (int, input ('Enter position of text: (x y):\n').split())
    size_txt = int (input ('Enter size of text:\n'))
    r, g, b = map(int, input('Enter color of text: (r g b):\n').split())
    t = int(input('Enter thickness of text:\n'))
    img = cv2.putText(img, txt, (posx, posy), cv2.FONT_HERSHEY_SIMPLEX, size_txt, (r, g, b), t)
    cv2.imshow('Text', img)
    cv2.waitKey(0)
    return img


menu = ['Load Image','Display Image','Save Image','Grayscale Image','Color Inversion','Brightness','Resize','Crop','Rotate','Flip','Blur','Edge Detection','Shapes', 'Add Text','Exit']
for idx,item in enumerate (menu,start=1):
    print(idx,".",item)

img = None

while True:
    x = int(input('Enter choice no.: '))
    if x == 1:
        img = load_image()
        print ('Image loaded')
    elif img is None:
        print("⚠️ No image loaded yet. Please load an image first.")
    elif x == 2:
        display_image(img)
        print ('Image displayed')
    elif x == 3:
        save_image(img)
        print ('Image saved')
    elif x == 4:
        img = grayscale(img)
        print ('Image grayscaled')
    elif x == 5:
        img = inversion(img)
        print ('Color inverted')
    elif x == 6:
        img = brightness(img)
        print ('Brightness adjusted')
    elif x == 7:
        img = resize_img(img)
        print ('Image Resized')
    elif x == 8:
        img = crop_img(img)
        print ('Image Cropped')
    elif x == 9:
        img = rotate_img(img)
        print ('Image Rotated')
    elif x == 10:
        img = flip_img(img)
        print ('Image Flipped')
    elif x == 11:
        img = blur_img(img)
        print ('Image Blurred')
    elif x == 12:
        img = edge_detection(img)
        print ('Image Edge Detection completed')
    elif x == 13:
        img = shapes(img)
        print ('Added Shapes to image')
    elif x == 14:
        img = add_text(img)
        print ('Text added')
    elif x == 15:
        break
    else:
        print ('Invalid input.')
        continue


