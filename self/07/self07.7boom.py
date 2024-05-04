def seven_boom(end_number):
    out = []
    for i in range(0, end_number + 1):
        if i % 7 == 0 or "7" in str(i):
            out.append("BOOM")
        else:
            out.append(i)
    return out


def main():
    print(seven_boom(17))


if __name__ == '__main__':
    main()
