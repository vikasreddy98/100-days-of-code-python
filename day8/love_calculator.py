def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    T = combined_name.lower().count('t')
    R = combined_name.lower().count('r')
    U = combined_name.lower().count('u')
    E = combined_name.lower().count('e')
    L = combined_name.lower().count('l')
    O = combined_name.lower().count('o')
    V = combined_name.lower().count('v')

    # print(f"T occurs {T} times")
    # print(f"R occurs {R} times")
    # print(f"U occurs {U} times")
    # print(f"E occurs {E} times")
    total1 = T+R+U+E
    # print(f"Total= {total1}")

    # print(f"L occurs {T} times")
    # print(f"O occurs {R} times")
    # print(f"V occurs {U} times")
    # print(f"E occurs {E} times")
    total2 = L+O+V+E
    # print(f"Total= {total2}")

    print(f" Your Love Score is {total1}{total2}")

name1 = input("Enter your name: ").lower()
name2 = input("Enter the other person's name: ").lower()

calculate_love_score(name1, name2)