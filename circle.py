def main():
    radius = read('enter the radius of the circle: ')
    display(area(radius), radius)

def read(msg):
    return float(input(msg))

def area(radius):
    return (22/7) * radius * radius

def display(area, radius):
    print(f'the area of the circle with {radius=} is {area}')

main()

def main():
    length=('enter a len of the rectangle')
    width=('enter a width of the rectangle')
    area=(length, width)
    display(length,width,area)

def read(msg):
    return float(input(msg))

def area(length, width):
    return length*width

def display(length,width, area):
    print(f'the area of the rectangle with{length=} and {width=} is {area}')

    main()