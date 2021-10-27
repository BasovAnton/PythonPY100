if __name__ == "__main__":
    # Write your solution here
    def kvadrat(n,m):
        return [i**2 for i in range(n,m+1) if i%2 ==1]
    print (kvadrat(1,10))
