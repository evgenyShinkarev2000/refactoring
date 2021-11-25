from PIL import Image
import numpy as np


def solveMiddleBright(pixels, curX, curY, maxX, maxY):
    return np.mean(pixels[curX:maxX, curY:maxY, 0:3])


def replacePixelsMiddleBright(pixels, curX, curY, maxX, maxY, gradationRatio, middle):
    pixels[curX:maxX, curY:maxY] = np.uint8((middle // gradationRatio) * gradationRatio)


def solveGradationRatio(gradationCount):
    return 255 / gradationCount


def filterImage(pixels, pixelSide, gradationCount):
    lenX = len(pixels)
    lenY = len(pixels[1])
    gradationRatio = solveGradationRatio(gradationCount)

    for curX in range(0, lenX, pixelSide):
        for curY in range(0, lenY, pixelSide):
            maxX = min(curX + pixelSide, lenX)
            maxY = min(curY + pixelSide, lenY)
            middle = solveMiddleBright(pixels, curX, curY, maxX, maxY)
            replacePixelsMiddleBright(pixels, curX, curY, maxX, maxY, gradationRatio, middle)


def program():
    img = Image.open("Lenna.png").convert("RGB")
    pixels = np.array(img)
    filterImage(pixels, 10, 5)
    res = Image.fromarray(pixels)
    res.save("res.jpg")


def run():
    program()


run()
