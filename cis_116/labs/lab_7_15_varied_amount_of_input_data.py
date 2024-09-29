lists = "53 15 97"
num = list(map(float, lists.split()))
# num = map(float, lists.split())
print(type(num))

print(f'{max(num):.2f} {(sum(num)/len(num)):.2f}')
