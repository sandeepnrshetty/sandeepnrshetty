def main():
    num=int(input('enter a number:'))
    ln=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=factorial(digit)
        temp=temp//10
    if num==sum:
        print(f'{num} is special num')
    else:
        print(f'{num} is not special num')
def factorial(digit):
    fact=1
    while digit:
        fact*=digit
        digit-=1
    return fact
main()