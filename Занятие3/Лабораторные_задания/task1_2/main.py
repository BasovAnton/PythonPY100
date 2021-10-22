def factorial(n):
    n_fact = 1
    for i in range(1, n+1):
        n_fact *= i
        print(n_fact)
    return n_fact


if __name__ == "__main__":
    # Write your solution here
    print (factorial(5))
