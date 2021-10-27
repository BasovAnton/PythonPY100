def summa(e):
    s = 0
    a = 0.5
    while True:
        s = s+a
        if a <= e:
            break
        else:
            a = a * 0.5

    return s


if __name__ == "__main__":
    # Write your solution here
    print(summa(0.0001))
