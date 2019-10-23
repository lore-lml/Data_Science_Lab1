import csv
from random import randint

def translate(pixel):
    translation = {
        (0, 63): " ",
        (64, 127): ".",
        (128, 191): "*",
        (192, 255): "#"
    }
    for k,v in translation.items():
        if k[0] <= int(pixel) <= k[1]:
            return v
    raise Exception("pixel is not in range [0,255]")


if __name__ == '__main__':

    digits = []
    with open("data_sets/mnist.csv") as dataset:
        for row in csv.reader(dataset):
            digits.append({
                "digit": row[0],
                "pixels": row[1:]
            })

    random_digit = digits[randint(0, 10000)]
    for i, pixel in enumerate(random_digit['pixels']):
        print(translate(pixel), end='')
        if (i+1) % 28 == 0:
            print()