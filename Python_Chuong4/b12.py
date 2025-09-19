def oscillate(x, y):
    #tạo ra dãy số dao động đối xứng
    for i in range (x, y):
        yield i
        yield -i

def main():
    print (list ( oscillate(-3,5)))
    for n in oscillate(-3,5):
        print(n, end=' ')
    print()

if __name__ == '__main__':
    main()