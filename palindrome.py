a="lalaa"
for i in range(len(a)):
    if (a[i] != a[-i-1]):
        print(False)
        break
else:
    print(True)


