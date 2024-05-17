def hashfunktion(namn):
    summa = 0
    for tkn in namn:
        summa = summa*365 + ord(tkn)
    return summa % 8 + 1

print(hashfunktion("elliotst"))