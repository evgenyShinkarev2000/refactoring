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


def filterImage(pixels, pixelSide=5, gradationCount=5):
    lenX = len(pixels)
    lenY = len(pixels[1])
    gradationCoef = solveGradationCoef(gradationCount)

    for curX in range(0, lenX, pixelSide):
        for curY in range(0, lenY, pixelSide):
            middle = solveMiddleBright(pixels, curX, curY, pixelSide)
            replacePixelsMiddleBright(pixels, curX, curY, pixelSide, gradationCoef, middle)

def program():
    imgName = input("Введите имя файла: ")
    if imgName == "":
        imgName = "img2.jpg"

    targetImgName = input("Введите имя выходного файла: ")
    if targetImgName == "":
        targetImgName = "rex.jpg"

    pixelSide, gradation = input("Введите размер пикселя и кол-во градаций серого: ").split(",")
    if pixelSide == "":
        pixelSide = 5
    if gradation == "":
        gradation = 10
    print("Ждите")

    img = Image.open(imgName).convert("RGB")
    pixels = np.array(img)
    filterImage(pixels, int(pixelSide), int(gradation))
    res = Image.fromarray(pixels)
    res.save(targetImgName)


def run():
    program()
    while True:
        flag = input("продолжить(y/n): ").lower()
        if flag == "y":
            program()
        elif flag == "n":
            break


run()
