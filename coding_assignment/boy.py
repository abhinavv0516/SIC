def can_be_arranged(n, boys, girls):
    boys.sort()
    girls.sort()
    i, j = 0, 0
    possible = True
    while i < n and j < n:
        if (i < n and boys[i] < girls[j]) or (j < n and girls[j] < boys[i]):
            if i > 0 and boys[i] == boys[i-1]:
                possible = False
                break
            if j > 0 and girls[j] == girls[j-1]:
                possible = False
                break

        if boys[i] < girls[j]:
            i += 1
        else:
            j += 1

    return "YES" if possible else "NO"
t = int(input())
for _ in range(t):
    n = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    print(can_be_arranged(n, boys, girls))
