if __name__ == "__main__":
    # Write your solution here
    def func(n, m):

        sred = sum(range(n, m+1))/len(range(n, m+1))
        return [i  for i in range(n, m+1) if i>sred]


    print(func(1, 2))
