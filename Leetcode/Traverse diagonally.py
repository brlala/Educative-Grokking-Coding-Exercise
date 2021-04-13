k = 0
while k < 5:
    for i in range(5 - k):
        j = i + k
        print(f"{i=}, {j=}")
    k += 1

# i=0, j=0
# i=1, j=1
# i=2, j=2
# i=3, j=3
# i=4, j=4
# i=0, j=1
# i=1, j=2
# i=2, j=3
# i=3, j=4
# i=0, j=2
# i=1, j=3
# i=2, j=4
# i=0, j=3
# i=1, j=4
# i=0, j=4
