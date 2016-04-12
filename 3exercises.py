
def main():
    recArea()
    tempChange()
    bmi()

def recArea():
    length=float(input("Enter rectangle's lenth (in meter): "))
    width=float(input("Enter rectangle's width (in meter): "))
    recarea=length*width
    print("Area of rectangle is: ",recarea,"\n")

def tempChange():
    celsius=float(input("Enter temp. in celsius: "))
    fahrenheit= (celsius*1.8) + 32.00
    print("Fahrenheit value is: ",fahrenheit,"\n")

def bmi():
    bmiW=float(input("Enter weight(in kg): "))
    bmiH=float(input("Enter height(in meter): "))
    bmiF=bmiW/(bmiH*bmiH)
    print("Body mass index is: ",bmiF,"\n")

main()