# Notes
# any function with a yield is a generator function

# every yield creates an exit point and re entry point

# generators also known as co-routines

def myitems(top):
    while top > 0:
        yield top**2
        top -= 1
    yield "All Done"
    yield "All Done Again"


for item in myitems(3):
    print(item)
