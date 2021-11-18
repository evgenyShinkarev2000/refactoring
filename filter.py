from PIL import Image
import numpy as np


def solveMiddleBright(pixels, curX, curY, pixelSide):
    lenX = len(pixels)
    lenY = len(pixels[1])
    middle = 0
    for offsetX in range(curX, min(curX + pixelSide, lenX)):
        for offsetY in range(curY, min(curY + pixelSide, lenY)):
            middle += sum(pixels[offsetX][offsetY])

    return int(middle // (pixelSide ** 2 * 3))


def replacePixelsMiddleBright(pixels, curX, curY, pixelSide, gradation, middle):
    lenX = len(pixels)
    lenY = len(pixels[1])
    for offsetX in range(curX, min(curX + pixelSide, lenX)):
        for offsetY in range(curY, min(curY + pixelSide, lenY)):
            pixels[offsetX][offsetY] = int(middle // gradation) * gradation


def solveGradationCoef(gradationCount):
    return 256 / gradationCount


def run():
    img = Image.open("img-test.png").convert("RGB")
    pixels = np.array(img)
    lenX = len(pixels)
    lenY = len(pixels[1])
    pixelSide = 1
    gradationCoef = solveGradationCoef(3)

    for curX in range(0, lenX, pixelSide):
        for curY in range(0, lenY, pixelSide):
            middle = solveMiddleBright(pixels, curX, curY, pixelSide)
            replacePixelsMiddleBright(pixels, curX, curY, pixelSide, gradationCoef, middle)

    res = Image.fromarray(pixels)
    res.save('res.jpg')


run()
