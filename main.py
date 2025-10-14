# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fizzbuzz():
    for i in range(1,500):
        if i % 11 == 0:
            print("Bong")
            continue

        placeHolder = ""

        if i % 3 == 0:
            if i % 5 == 0:
                placeHolder = "FizzBuzz"
            else:
                placeHolder = "Fizz"
        elif i % 5 == 0:
            placeHolder = "Buzz"
        elif i % 7 == 0:
            placeHolder = "Bang"

        if i % 7 == 0 and (i % 3 == 0 or i % 5 == 0):
            placeHolder += "Bang"

        if placeHolder:
            print(placeHolder)
        else:
            print(i)



if __name__ == '__main__':
    fizzbuzz()

