from PIL import Image
import numpy as np


def solveMiddleBright(pixels, curX, curY, maxX, maxY):
    """
    :param pixels: изображение
    :param curX: начальная x координата
    :param curY: начальная y координата
    :param maxX: конечная x координата
    :param maxY: конечная y координата
    :return среднея яркость пикселей в указаном диапозоне

    >>> solveMiddleBright(np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]]), 0, 0, 2, 2)
    2.5

    """
    return np.mean(pixels[curX:maxX, curY:maxY, 0:3])


def replacePixelsMiddleBright(pixels, curX, curY, maxX, maxY, gradationRatio, middle):
    pixels[curX:maxX, curY:maxY] = np.uint8((middle // gradationRatio) * gradationRatio)


def solveGradationRatio(gradationCount):
    """
    >>> solveGradationRatio(255)
    1
    """
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()

run()
