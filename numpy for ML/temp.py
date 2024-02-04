import sys
original_stdout = sys.stdout
with open('output.txt', 'w') as f:
    sys.stdout = f
    for x in range(20001):
        print(x)
    sys.stdout = original_stdout
    