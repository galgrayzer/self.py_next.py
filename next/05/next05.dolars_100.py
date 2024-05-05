from itertools import combinations

# wallet:
# 3 x 20
# 5 x 10
# 2 x 5
# 5 x 1


def get_combinations():
    for i in range(1, 16):
        for comb in combinations([20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1], i):
            if sum(comb) == 100:
                yield comb


def main():
    dolar100 = {comb for comb in get_combinations()}
    print(len(dolar100))


if __name__ == '__main__':
    main()
