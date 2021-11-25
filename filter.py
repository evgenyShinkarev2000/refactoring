from PIL import Image
import numpy as np


def solveMiddleBright(pixels, curX, curY, maxX, maxY):
    return np.mean(pixels[curX:maxX, curY:maxY, 0:3])


def replacePixelsMiddleBright(pixels, curX, curY, maxX, maxY, gradationCoef, middle):
    pixels[curX:maxX, curY:maxY] = np.uint8((middle // gradationCoef) * gradationCoef)


def solveGradationCoef(gradationCount):
    return 255 / gradationCount


def filterImage(pixels, pixelSide, gradationCount):
    lenX = len(pixels)
    lenY = len(pixels[1])
    gradationCoef = solveGradationCoef(gradationCount)

    for curX in range(0, lenX, pixelSide):
        for curY in range(0, lenY, pixelSide):
            maxX = min(curX + pixelSide, lenX)
            maxY = min(curY + pixelSide, lenY)
            middle = solveMiddleBright(pixels, curX, curY, maxX, maxY)
            replacePixelsMiddleBright(pixels, curX, curY, maxX, maxY, gradationCoef, middle)


def program():
    imgName = input("Введите имя файла: ") or "Lenna.png"
    targetImgName = input("Введите имя выходного файла: ") or "res.jpg"
    pixelSide = input("Введите размер пикселя: ") or 10
    gradation = input("Введите кол-во градаций серого: ") or 5
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
