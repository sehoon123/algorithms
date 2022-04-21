
x1 = 11
x2 = 22
x3 = 33
x4 = 44

for i in range(4):
    xi = eval(f"fit(x{i+1}, y{i+1})")
    print(xi, end=" ")