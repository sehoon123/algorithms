n = int(input())

for h in range(1, 10):
    for e in range(0, 10):
        for l in range(0,10):
            for o in range(0,10):
                for w in range(1,10):
                    for r in range(0,10):
                        for d in range(0, 10):
                            if h == e or h == l or h == o or h == w or h == r or h == d or e == l or e == o or e == w or e == r or e == d or l == o or l == w or l == r or l == d or o == w or o == r or o == d or w == r or w == d or r == d:
                                continue
                            if 10000*h + 10000*w + 1000*e + 1000*o + 100*l + 100*r + 10*l + 10*l + o + d == n:
                                print(f'  {h}{e}{l}{l}{o}\n+ {w}{o}{r}{l}{d}\n-------')
                                print("%7d" %n)
                                exit()

print("No Answer")
