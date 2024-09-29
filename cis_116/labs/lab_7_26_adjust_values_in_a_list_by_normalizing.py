amt = int(input())

val = []
for i in range(amt):
    num = float(input())
    val.append(num)

val = [print(f'{x / max(val):.2f}') for x in val]
