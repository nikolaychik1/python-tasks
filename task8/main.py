max_n = int(input())
avg = set(i for i in range(1, max_n + 1))
biat = input()
while biat != "HELP":
    av = input()
    if av == "YES":
        avg &= set(map(int, biat.split()))
    if av == "NO":
        avg -= set(map(int, biat.split()))
    biat = input()
print(*sorted(avg))
