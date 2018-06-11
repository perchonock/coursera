import sys

input = sys.argv[1]
#input = input()
n = int(input)
output = ''

for i in range(1, n + 1):
    output += " " * (n - i)
    output += "#" * i
    output += "\n"

print(output)