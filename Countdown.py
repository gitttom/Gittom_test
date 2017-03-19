import sys


def recurse(thirdList: list, myTarget: int, myoperator: str = None, difference: int = None) -> object:
    if (myoperator == None):
        for operator in operators:
            recurse(thirdList, myTarget, operator)
        return
    if (difference == None):
        difference = myTarget

    newValue = "(" + str(thirdList[0]) + myoperator + str(thirdList[1]) + ")"
    fourthList = thirdList.copy()
    del fourthList[0]
    fourthList[0] = newValue
    if len(fourthList) > 1:
        recurse(fourthList, myTarget, None, difference)
    else:
        answer = eval(fourthList[0])
        newdifference = abs(answer - myTarget)
        if newdifference < difference:
            difference = newdifference
            print("** " + str(answer))
        if (answer == myTarget):
            print("")
            print(fourthList, end="")
            print("           = " + str(answer))
            exit(0)


def calc(myList, myTarget):
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    listlen = len(myList)
    while i < listlen:
        print("")
        j = 0
        while j < listlen:
            if (i != j):
                k = 0
                while k < listlen:
                    print(".", end="", flush=True)
                    if (i != k and j != k):
                        l = 0
                        while l < listlen:
                            if (i != l and j != l and k != l):
                                m = 0
                                while m < listlen:
                                    if (i != m and j != m and k != m and l != m):
                                        n = 0
                                        while n < listlen:
                                            if (i != n and j != n and k != n and l != n and m != n):
                                                # print(str(i) + str(j) + str(k) + str(l) + str(m) + str(n))
                                                newList = [myList[i], myList[j], myList[k], myList[l], myList[m],
                                                           myList[n]]
                                                recurse(newList, myTarget)
                                            n += 1
                                    m += 1
                            l += 1
                    k += 1
            j += 1
        i += 1


def main():
    print("Welcome to countdown!")
    myList = [0, 0, 0, 0, 0, 0]
    myTarget = 0
    i = 0
    while i < 6:
        try:
            myList[i] = int(input("Please enter number " + str(i) + ": "))
            i += 1
        except ValueError:
            print("Not a number")

    myTarget = int(input("Please enter target number "))

    calc(myList, myTarget)

    print("")
    print("Solution not found.")
    exit(0)


operators = ["+", "-", "*", "/", "*0+"]
if __name__ == '__main__':
    main()
