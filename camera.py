import cv2
from PIL import Image
from pytesseract import pytesseract


def capture():
    camera=cv2.VideoCapture(0)

    while True:
        _,image=camera.read()
        cv2.imshow('image',image)
        if cv2.waitKey(1)& 0xFF==ord('s'):
            cv2.imwrite('test1.jpg',image)
            break
    camera.release()
    cv2.destroyAllWindows()

    path_to_tesseract = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    image_path = "test1.jpg"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    return text


Number_plate = capture()
print(Number_plate)

Number_plate2 = capture()
print(Number_plate2)
