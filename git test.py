import sys
x = len(sys.argv)

if x == 3:
    print("Аргументы выданы: " + str(sys.argv))
else:
    print("Аргументы не выданы")
print(sys.argv[1])

print(sys.argv[2])

with open (sys.argv[1]) as f:
    with open(sys.argv[2], "w") as f1:
        for line in f:
            if "adapter" in line:
                f1.write(line)
