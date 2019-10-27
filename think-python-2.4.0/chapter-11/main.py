count = 1

def fun():
    global count
    count = 5
    print(count)

fun()
print(count)