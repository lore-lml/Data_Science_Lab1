import csv
from math import sqrt, pow


def avg(sum, len):
    return float(sum) / len


def quad_dev(val, avg):
    return pow(val - avg, 2)


def std_dev(sum_quad_dev, len):
    return sqrt(sum_quad_dev / len)

dataset = list()
with open("data_sets/iris.csv") as iris:
    for row in csv.reader(iris):
        row = list(row)
        if len(row) != 0:
            dataset.append(row)

# Calcolo media per ogni colonna e diferenziazione dei tre dataset
sl = sw = pl = pw = .0
categories = {}
for row in dataset:
    sl += float(row[0])
    sw += float(row[1])
    pl += float(row[2])
    pw += float(row[3])

    category = row[4].lower()
    if category not in categories:
        categories[category] = []
    else:
        categories[category].append(row)

n_rows = len(dataset)
sl = avg(sl, n_rows)
sw = avg(sw, n_rows)
pl = avg(pl, n_rows)
pw = avg(pw, n_rows)

# Calcolo std dev per ogni colonna
std_dev_sl = std_dev_sw = std_dev_pl = std_dev_pw = 0
for row in dataset:
    std_dev_sl += quad_dev(float(row[0]), sl)
    std_dev_sw += quad_dev(float(row[1]), sw)
    std_dev_pl += quad_dev(float(row[2]), pl)
    std_dev_pw += quad_dev(float(row[3]), pw)

std_dev_sl = std_dev(std_dev_sl, n_rows)
std_dev_sw = std_dev(std_dev_sw, n_rows)
std_dev_pl = std_dev(std_dev_pl, n_rows)
std_dev_pw = std_dev(std_dev_pw, n_rows)

print(f"Avg: [{sl:.2f}, {sw:.2f}, {pl:.2f}, {pw:.2f}]")
print(f"Std Dev: [{std_dev_sl:.2f}, {std_dev_sw:.2f}, {std_dev_pl:.2f}, {std_dev_pw:.2f}]")

# Calcolo media per ogni categoria
for category in categories.values():
    sl = sw = pl = pw = .0
    for row in category:
        sl += float(row[0])
        sw += float(row[1])
        pl += float(row[2])
        pw += float(row[3])

    n_rows = len(category)
    sl = avg(sl, n_rows)
    sw = avg(sw, n_rows)
    pl = avg(pl, n_rows)
    pw = avg(pw, n_rows)

    std_dev_sl = std_dev_sw = std_dev_pl = std_dev_pw = 0
    for row in category:
        std_dev_sl += quad_dev(float(row[0]), sl)
        std_dev_sw += quad_dev(float(row[1]), sw)
        std_dev_pl += quad_dev(float(row[2]), pl)
        std_dev_pw += quad_dev(float(row[3]), pw)

    std_dev_sl = std_dev(std_dev_sl, n_rows)
    std_dev_sw = std_dev(std_dev_sw, n_rows)
    std_dev_pl = std_dev(std_dev_pl, n_rows)
    std_dev_pw = std_dev(std_dev_pw, n_rows)

    print(f"\n{category[0][4]}:")
    print(f"Avg: [{sl:.2f}, {sw:.2f}, {pl:.2f}, {pw:.2f}]")
    print(f"Std Dev: [{std_dev_sl:.2f}, {std_dev_sw:.2f}, {std_dev_pl:.2f}, {std_dev_pw:.2f}]")
