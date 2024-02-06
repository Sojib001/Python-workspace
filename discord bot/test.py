import math

def squareRoot(num):
    lower_bound = 0
    upper_bound = num
    temp = 0
    nCount = 100

    while nCount != 0:
        temp = (lower_bound + upper_bound) / 2
        if temp * temp == num:
            return temp
        elif temp * temp > num:
            upper_bound = temp
        else:
            lower_bound = temp
        nCount -= 1
    return temp

def solve():
    x1, y1, x2, y2 = map(float, input().split())
    a = y2*y2 - y1*y1
    b = 2*x2*y1*y1 - 2*x1*y2*y2
    c = (x1*x1*y2*y2) - (x2*x2*y1*y1)
    sq1, sq2 = 0, 0

    if a == 0:
        sq1 = (-1) * (c/b)
        sq2 = sq1
    else:
        sq1 = ((-1)*b + math.sqrt(b*b - 4*a*c)) / (2*a)
        sq2 = ((-1)*b - math.sqrt(b*b - 4*a*c)) / (2*a)

    d1 = math.sqrt((x1 - sq1)*(x1 - sq1) + y1*y1) + math.sqrt((x2 - sq1)*(x2 - sq1) + y2*y2)
    d2 = math.sqrt((x1 - sq2)*(x1 - sq2) + y1*y1) + math.sqrt((x2 - sq2)*(x2 - sq2) + y2*y2)

    print(f"{min(d1, d2):.10f}")

def main():
    t = int(input())
    for tc in range(1, t+1):
        solve()

if __name__ == "__main__":
    main()