if __name__ == "__main__":
    # Write your solution here
    def number(n):
        print([int(i) for i in str(n)])
        print(sum([int(i) for i in str(n)]))
        print(sum([int(i) for i in str(n) if int(i) % 2 == 0]))
        print(len([int(i) for i in str(n)]))
        print(min([int(i) for i in str(n)]))
        print([int(i) for i in str(n)[::2]])

        list_ = [int(i) for i in str(n)]
        print(list_[0]-list_[-1])

        a = 10
        b = 0
        for i, value in enumerate(list_):
            if value < a:
                a = value
                b = i
        print(a, b)


    number(5679)
