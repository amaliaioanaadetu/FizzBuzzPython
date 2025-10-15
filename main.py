# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fizzbuzz(upperLimit):
    for i in range(1,upperLimit + 1):
        if i % 11 == 0:
            print("Bong")
            continue

        parts = []

        if i % 3 == 0:
            parts.append("Fizz")
        if i % 5 == 0:
            parts.append("Buzz")
        if i % 7 == 0:
            parts.append("Bang")

        if i % 13 == 0:
            inserted = False
            for idx, part in enumerate(parts):
                if part.startswith("B"):
                    parts.insert(idx, "Fezz")
                    inserted = True
                    break
            if not inserted:
                parts.append("Fezz")

        if i % 17 == 0:
            parts.reverse()

        print("".join(parts) if parts else i)


def fizzbuzzSimple(upperLimit):
    res = list(map(lambda x: math.floor((x - 1) % 3 / 2) * "Fizz" + math.floor((x - 1) % 5 / 4) * "Buzz" or x, range(1, upperLimit + 1)))
    for elem in res:
        print(elem)

if __name__ == '__main__':
    upperLimit = int(input("Select the maximum number: "))
    fizzbuzz(upperLimit)

