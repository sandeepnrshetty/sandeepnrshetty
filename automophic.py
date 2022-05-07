#WAP  print first N  amstrong number
def main():
    upper=int(input('enter a range of number:'))
    first_n_armstrong(upper)

def first_n_armstrong(upper):
    for var in range(1,upper+1):
        ln=len(str(var))
        sum=0
        temp=var
        while temp>0:
            digit=temp%10
            sum=sum+digit**ln
            temp//=10
            if var==sum:
                print(var)
main()