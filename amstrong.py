def main():
    num=int(input('enter a number:'))
    ln=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit ** ln
        temp=temp//10
    if num==sum:
        print(f'{num} is armstong')
    else:
        print(f'{num} is not armstrong')
main()