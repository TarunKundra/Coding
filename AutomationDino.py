# ImageGrab - use to take ss
import pyautogui
from PIL import ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)
def isCollide(data):
    # birds
    for i in range(250, 370):
        for j in range(300, 370):
            if data[i, j] < 40:
                hit('down')
                return True
    # cactus
    for i in range(220, 390):
        for j in range(410, 500):
            if (data[i, j] < 100):
                hit('up')
                return True
    return False
if __name__ == '__main__':
    time.sleep(3)
    while True:
        # to convert image in gray scale
        image = ImageGrab.grab().convert('L')
        # from image to array
        data = image.load()
        # if collide with obstical
        isCollide(data)
		
'''
# to text image
# cactus
for i in range(220,390):
    for j in range(410, 500):
        data[i, j] = 0  # for black
# birds
for i in range(250, 370):
    for j in range(300, 370):
        data[i, j] = 171
image.show()

# to get image array
from numpy import asarray
image = ImageGrab.grab().convert('L')
print(asarray(image))

'''