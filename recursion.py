def fun(x):
    if x > 0:
        x = x - 1
        fun(x)
        print(x)
        x = x - 1
        fun(x)
fun(4) 