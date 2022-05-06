def main():

    length=float(input('enter a len of the rectangle: '))
    breadth =float(input('enter a bre of the rectangle: '))
    area_of = area(length, breadth)
    display(length,breadth,area_of)

def read(msg):
    return float(input(msg))

def area(length, breadth):
    return length*breadth

def display(length, breadth, area_of):
    print(f'the area of rectangle is {area_of=}')

main()