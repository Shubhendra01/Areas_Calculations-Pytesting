def RectangleArea(a,b):
    return a * b
def RectanglePerimeter(a,b):
    return a+a+b+b
def SquareArea(a):
    return a * a


if __name__ == "__main__":
    while True:
        print("Make a Choice")
        print("1.Area of Rectangle")
        print("2.Perimeter of Rectangle")
        print("3.Area of Square")
        print("4.Exit")
        x = int(input("Enter Your Choice"))

        if x == 1:
            num1 = int(input("Enter the Length"))
            num2 = int(input("Enter the Breadth"))
            result = RectangleArea(num1, num2)
            print(result)

        elif x == 2:
            num1 = int(input("Enter the Length"))
            num2 = int(input("Enter the Breadth"))
            result = RectanglePeri(num1, num2)
            print(result)

        elif x == 3:
            num1 = int(input("Enter the Side"))
            result = SquareArea(num1)
            print(result)

        else:
            print("Invalid Choice")