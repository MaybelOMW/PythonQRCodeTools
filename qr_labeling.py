from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2

BLANK_AREA_HEIGHT = 28

def ReadImage(index):
    qr_image = cv2.imread("QRcode_" + str(index) + ".png")
    # Convert to PIL Image
    cv2_im_rgb = cv2.cvtColor(qr_image, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(cv2_im_rgb)
    
    return pil_img, qr_image

def AddWhiteSpace(index, pil_img):
    # Append white space underneath
    new_img = Image.new(pil_img.mode, size=(pil_img.size[0], pil_img.size[1] + BLANK_AREA_HEIGHT), color="white")
    new_img.putdata(pil_img.getdata())
    new_img.save("QRcode_" + str(index) + ".png")

def LabelQRcode(index, pil_img, qr_image):
    # Create image object
    draw = ImageDraw.Draw(pil_img)

    # Props gathering
    font = ImageFont.truetype("arial.ttf", 30)
    embeded_text = 'QR-' + str(index)
    H, W, _ = qr_image.shape
    w, h = font.getsize(embeded_text)
    xy_coor = ((W-w)/2,430)

    # Draw the text
    draw.text(xy_coor, embeded_text, fill="black", font=font)

    # Save the image
    cv2_im_processed = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    cv2.imwrite("QRcode_" + str(index) + ".png", cv2_im_processed)