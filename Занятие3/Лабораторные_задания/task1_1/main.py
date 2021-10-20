
def main():
    sum_ = 0
    n = 1
    while True:
        sum_ = sum_+n**2
        print(n, sum_)
        next_ = (n+1)**2
        if sum_ + next_ >= 500:
            break
        n += 1
    return n


if __name__ == "__main__":
    print(main())
