
def multi(*numbers , **student):
    multi=1
    for num in numbers:
        multi*=num
        print(multi)
    print(f"Hello {student}")