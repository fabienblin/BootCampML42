t = (19,42,21)

print("The 3 numbers are:", end="")
i = 0
for n in t :
    if i != 0 :
        print(",", end="")
    print(" {0:d}".format(n), end="")
    i += 1
print("")