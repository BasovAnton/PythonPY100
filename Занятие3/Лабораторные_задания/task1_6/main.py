def strong_life(b, a):
    money = 0
    for i in range(0, 10):
        k = 1.03**i
        b_new = k*b
        money += b_new-a
        print(round(b_new,2), round(money,2))
    return round(money,2)


if __name__ == "__main__":
    print(strong_life(6000, 5000))
