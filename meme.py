import speech_recognition as sr
from PIL import Image, ImageFont, ImageDraw
import random, textwrap

IMAGE_ID = 'final.jpg'
FONT_TYPE = "opensans.ttf"
SAMPLE_TEXT = "This is a sample text"
WIDTH = 0
HEIGHT = 0

def getImage():
    imageNames = ['jackiechan', 'michaeljordan', 'pikachu', 'spongebob', 'success']
    randNum = random.randint(0, len(imageNames) - 1) 
    imageURL = "{}.jpg".format(imageNames[randNum])
    try:
        img = Image.open(imageURL)
        return img
    except IOError as e:
        print('IOError: {0}'.format(e))
        return None

def speechToText(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)
    try:
      print("Google Speech Recognition Input: " + r.recognize_google(audio))
    except sr.UnknownValueError:
      print("Audio Not Recognized")
    except sr.RequestError as e:
      print("Results not requested from Google Speech Recognition service; {0}".format(e))
    rawText = r.recognize_google(audio)
    textInit = rawText if rawText != None else SAMPLE_TEXT
    txt = textwrap.fill(textInit, width=WIDTH/15)
    return txt

def imageText(img, txt):
    box = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_TYPE, int(HEIGHT/25))
    box.rectangle(((WIDTH/10, HEIGHT*(8/10)), (WIDTH*(9/10), HEIGHT*(19/20))), fill='black')
    box.text((WIDTH/10, HEIGHT*(8/10)), txt, fill='white', font=font)
    return img
  
if __name__ == '__main__':
    img = getImage()
    WIDTH, HEIGHT = img.size
    txt = speechToText()
    if img != None and txt != None:
        final = imageText(img, txt)
        final.save(IMAGE_ID)
        final.show()
    else:
        print("Error: Unvalid Entry")