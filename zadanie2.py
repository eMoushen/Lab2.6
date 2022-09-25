if __name__ == '__main__':

    num = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    print({v:k for k, v in num.items()})