def gen_square(max_root):
    root = 0
    while root < max_root:
        yield root**2
        root += 1


squares = gen_square(5)

for square in squares:
    print(square)