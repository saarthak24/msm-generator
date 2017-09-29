from flask import Flask
from flask import request
import PIL
from convert import convert
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

app = Flask(__name__)

def convert(message):
    output = ""
    i = True  # capitalize
    for char in message:
        if i:
            output += char.lower()
        else:
            output += char.upper()
        i = not i
    return output

@app.route('/meme',methods=['POST'])
def generate():
    data = request.args['message']
    topString = input("Enter Top Message: ")
    bottomString = input("Enter Top Message: ")
    topString = convert(topString)
    bottomString = convert(bottomString)
    print(topString + " " + bottomString)

    img = Image.open("base.jpg")
    imageSize = img.size
    fontSize = int(imageSize[1] / 5)
    font = ImageFont.truetype("Krabby Patty.ttf", fontSize)

    topTextSize = font.getsize(topString)
    bottomTextSize = font.getsize(bottomString)

    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize = fontSize - 1
        font = ImageFont.truetype("Krabby Patty.ttf", fontSize)
        topTextSize = font.getsize(topString)
        bottomTextSize = font.getsize(bottomString)

    topTextPosition = ((imageSize[0] / 2) - (topTextSize[0] / 2), 0)
    bottomTextPosition = ((imageSize[0] / 2) - (bottomTextSize[0] / 2), imageSize[1] - bottomTextSize[1])
    draw = ImageDraw.Draw(img)

    #Outline text
    outlineRange = int(fontSize / 15)
    for x in range(-outlineRange, outlineRange + 1):
        for y in range(-outlineRange, outlineRange + 1):
            draw.text(
                (topTextPosition[0] + x, topTextPosition[1] + y), topString, (0, 0, 0), font=font)
            draw.text(
                (bottomTextPosition[0] + x, bottomTextPosition[1] + y), bottomString, (0, 0, 0), font=font)

    draw.text(topTextPosition, topString, (255, 255, 255), font=font)
    draw.text(bottomTextPosition, bottomString, (255, 255, 255), font=font)

    img.save("meme.png")
