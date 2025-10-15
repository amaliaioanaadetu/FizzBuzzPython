# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fizzbuzz(upperLimit):
    for i in range(1,upperLimit + 1):
        if i % 11 == 0:
            print("Bong")
            continue

        placeHolder = ""

        if i % 3 == 0:
            placeHolder += "Fizz"
        if i % 5 == 0:
            placeHolder += "Buzz"
        if i % 7 == 0:
            placeHolder += "Bang"

        if i % 13 == 0:
            positionFirstB = placeHolder.find("B")
            if positionFirstB != -1:
                placeHolder = placeHolder[:positionFirstB] + "Fezz" + placeHolder[positionFirstB:]
            else:
                placeHolder += "Fezz"

        if i % 17 == 0:
            reversedPlaceHolder = ""
            for i in range(0, len(placeHolder)):
                if placeHolder[i].isupper():
                    word = placeHolder[i: i + 4]
                    reversedPlaceHolder = word + reversedPlaceHolder
            placeHolder = reversedPlaceHolder

        if placeHolder:
            print(placeHolder)
        else:
            print(i)


def fizzbuzzSimple(upperLimit):
    res = list(map(lambda x: math.floor((x - 1) % 3 / 2) * "Fizz" + math.floor((x - 1) % 5 / 4) * "Buzz" or x, range(1, upperLimit + 1)))
    for elem in res:
        print(elem)

if __name__ == '__main__':
    upperLimit = int(input("Select the maximum number: "))
    fizzbuzzSimple(upperLimit)

