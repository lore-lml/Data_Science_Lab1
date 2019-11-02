import csv
from random import randint
from math import sqrt

VECTOR_LENGTH = 784
BLACK_TH = 128


def translate(pixel):
    translation = {
        (0, 63): " ",
        (64, 127): ".",
        (128, 191): "*",
        (192, 255): "#"
    }
    for k, v in translation.items():
        if k[0] <= pixel <= k[1]:
            return v
    raise Exception("pixel is not in range [0,255]")


def print_digit(digits, index):
    random_digit = digits[index]
    for i, pixel in enumerate(random_digit['pixels']):
        print(translate(pixel), end='')
        if (i + 1) % 28 == 0:
            print()


def euclidean_distance(v1, v2):
    l_v1 = len(v1)
    l_v2 = len(v2)

    if l_v1 != l_v2:
        raise Exception("Lists have not the same lenght")

    quad_diff = []
    for e1, e2 in zip(v1, v2):
        quad_diff.append((e1 - e2) ** 2)

    return sqrt(sum(quad_diff))


def get_distances(digits, chosen_digits):
    distances = []
    for i in range(0, len(chosen_digits)-1):
        v1 = digits[chosen_digits[i]]['pixels']
        for j in range(i+1, len(chosen_digits)):
            v2 = digits[chosen_digits[j]]['pixels']
            distances.append(euclidean_distance(v1, v2))

    return distances


def get_zeroes_ones(digits):
    zeroes = []
    ones = []
    for e in digits:
        if e['digit'] == '0':
            zeroes.append(e['pixels'])
        elif e['digit'] == '1':
            ones.append(e['pixels'])

    return zeroes, ones


def count_black_pixels(zeroes, ones):
    Z = [0] * VECTOR_LENGTH
    O = [0] * VECTOR_LENGTH

    for z, o in zip(zeroes, ones):
        for i in range(0, VECTOR_LENGTH):
            if z[i] >= BLACK_TH:
                Z[i] += 1
            if o[i] >= BLACK_TH:
                O[i] += 1

    return Z, O


def compute_differences(v1, v2):
    if len(v1) != len(v2):
        raise Exception("Lists have not the same lenght")
    return [abs(e1 - e2) for e1, e2 in zip(v1, v2)]


def get_best_separator(differences):
    # max ritorna la tupla (index, value) mentre la key si riferisce alla parte della lista da confrontare
    # in questo caso il value in posizione 1
    return max(enumerate(differences), key=lambda x: x[1])[0]


if __name__ == '__main__':

    # 1.
    digits = []
    with open("data_sets/mnist.csv") as dataset:
        for row in csv.reader(dataset):
            digits.append({
                "digit": row[0],
                "pixels": list(map(int, row[1:]))
            })

    # 2.
    print_digit(digits, randint(0, 10000))

    # 3.
    chosen_digits = [25, 29, 31, 34]
    distances = get_distances(digits, chosen_digits)
    print(f"Distances between pair of {[digits[e]['digit'] for e in chosen_digits]}:")
    print(["%.2f" % d for d in distances])

    # 4.
    # La distanza più piccola è ragionevolmente riferita alla coppia dei due numeri uguali ovvero gli uni
    # Le distanza intermedia è riferita alle due coppie 1,7 in quanto hanno una rappresentazione simile graficamente
    # Le distanze più grosse sono quelle tra 0,1 e 0,7, anch'esse paragonabili per lo stesso motivo sopra

    # 5.
    zeroes, ones = get_zeroes_ones(digits)
    Z, O = count_black_pixels(zeroes, ones)
    differences = compute_differences(Z, O)
    print(f"\nThe pixel that best separates 0's and 1's is: {get_best_separator(differences)}th")

    # Essendo il vettore lungo 784, 406 è un pixel che ragionevolmente starà circa nel mezzo il che ha senso in quanto
    # ogni uno è disegnato ragionevolmente al centro della matrice 28x28 e quindi passerà per il centro, mentre lo zero
    # ha il centro vuoto e avrà quindi pixel tendenti al bianco