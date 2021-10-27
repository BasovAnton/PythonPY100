if __name__ == "__main__":
    # Write your solution here
    def kvadrat(n, m):
        s = 0
        for i in range(n, m+1):

            if i % 2 == 0:
                s += 1
        return s


    print(kvadrat(3, 25))
