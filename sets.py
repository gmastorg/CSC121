def main():

    myset = set()
    myset.add(1)
    myset.add(2)
    myset.add(3)
    myset.update([4,5,6])
    print(myset)  
    myset.remove(3)
    print(myset)
    myset.remove(9)
    print(myset)
main()
