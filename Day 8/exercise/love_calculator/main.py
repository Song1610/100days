def calculate_love_score(name1, name2):
    calculate_love = []
    
    name = (name1 + name2).lower()

    t = name.count('t')
    r = name.count('r')
    u = name.count('u')
    e = name.count('e')

    true = t + r + u + e


    l = name.count('l')
    o = name.count('o')
    v = name.count('v')
    e = name.count('e')

    love = l + o + v + e
    
    score = int(str(true) + str(love))
    print(f"Love score is {score}")

calculate_love_score("Kanye West", "Kim Kardashian")