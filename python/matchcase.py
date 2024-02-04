x = int(input())
match x:
    case 0:
        print("Its 0!")
    case _ if(x > 0):
        print("positive")
    case _ if(x<0):
        print("Negative")