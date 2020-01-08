def vymen(zoz, i, j):
    zoz[i], zoz[j] = zoz[j], zoz[i]

def bubble_sort(zoz):
    for i in range(len(zoz)):
        for j in range(len(zoz)-1):
            if zoz[j] > zoz[j+1]:
                vymen(zoz, j, j+1)
        print(*zoz)

z = [13, 7, 11, 3, 5, 2]
bubble_sort(z)