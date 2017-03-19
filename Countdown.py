import sys
from PyQt4 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt")
   w.show()
   sys.exit(app.exec_())

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)


def recurse(thirdList: list, myTarget: int, myoperator: str = None) -> None:
    global closestanswer
    if (myoperator == None):
        for operator in operators:
            recurse(thirdList, myTarget, operator)
        return

    newValue = "(" + str(thirdList[0]) + myoperator + str(thirdList[1]) + ")"
    fourthList = thirdList.copy()
    del fourthList[0]
    fourthList[0] = newValue
    if len(fourthList) > 1:
        recurse(fourthList, myTarget, None)
    else:
        answer = eval(fourthList[0])

        if abs(myTarget - answer) < abs(myTarget - closestanswer):
            print (answer)
            closestanswer = answer
            return
        if (answer == myTarget):
            print("")
            print(fourthList[0], end="")
            print(" = " + str(answer))
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

    "This would create first object of Employee class"
    emp1 = Employee("Zara", 2000)
    "This would create second object of Employee class"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print ("Total Employee %d" % Employee.empCount)

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

closestanswer = 0
operators = ["+", "-", "*", "/", "*0+"]
if __name__ == '__main__':
    main()




app = ExampleApp(tk.Tk())
app.run()