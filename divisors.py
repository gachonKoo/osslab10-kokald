import sys
number = int(sys.argv[1])
for i in range(1,100):
  if (100 % i) == 0:
    print(i, end=" ")
print()
