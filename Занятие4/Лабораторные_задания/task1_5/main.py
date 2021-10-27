if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list1=[i for i in list_ if i%2==0]
    list2 = [i for i in list_ if i%2 != 0]
    if len(list2)>len(list1):
        print("Нечетных больше")
    elif len(list2)<len(list1):
        print("Четных больше")
    else:
        print("Равно")
