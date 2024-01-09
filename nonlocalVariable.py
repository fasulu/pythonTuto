
# ********nonlocal variable

# ******** 1st example without nonlocal variable

def outerFunc():
    msg="hello"
    def innerFunc():
        msg="welcome"
        print(msg)
    innerFunc()
    print(msg)

outerFunc()

# output is
# welcome
# hello

# ******** 2nd example nonlocal variable

def outerFunc():
    msg="hello"
    def innerFunc():
        nonlocal msg        # this will make msg as global variable so msg value will assigned as 'welcome'
        msg="welcome"
        print(msg)
    innerFunc()
    print(msg)

outerFunc()

# output is
# welcome
# welcome