def squared_numbers(start, stop):
    out = []
    while start <= stop:
        out.append(start ** 2)
        start += 1
    return out

def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))

if __name__ == '__main__':
    main()