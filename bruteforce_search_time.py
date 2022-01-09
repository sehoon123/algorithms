n = int(input())

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if s % 10 == 3 or s // 10 == 3:
                print("%s:%s:%s" % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))
                continue
            if m % 10 == 3 or m // 10 == 3:
                print("%s:%s:%s" % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))
                continue
            if h % 10 == 3 or h // 10 == 3:
                print("%s:%s:%s" % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))
                continue
