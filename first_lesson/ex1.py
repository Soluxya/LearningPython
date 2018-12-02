
mystring = 'hello'
myfloat = float(10.2)
myint = 21


if mystring == "hello":
    print("String: %s" % mystring)
if mystring != "hello":
    print("String was not intended: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.1:
    print("Float: %f" % myfloat)
if isinstance(myfloat, float) and myfloat != 10.1:
    print("Float was not intended: %f" % myfloat)
if isinstance(myfloat, int) and myfloat != 10.1:
    print("this was not a float type")
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
if isinstance(myint, int) and myint != 20:
    print("Integer was not intended: %d" % myint)
