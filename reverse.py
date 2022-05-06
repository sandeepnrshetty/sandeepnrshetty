def main():
    num = int(input('enter a num:'))
    reverse(num)

def reverse(num):
    count = 0
    temp = num
    while num:
        last_digit = num % 10
        count += 1
        num = num // 10
        if count >= 0:
             print(last_digit, end='')

main()