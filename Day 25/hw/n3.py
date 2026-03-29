def pal(string):
    if string[ : :]==string[: :-1]:
        return "Palindrom"
    else:
        return "Not Palindrom"
    
print(pal("level"))
print(pal("don"))