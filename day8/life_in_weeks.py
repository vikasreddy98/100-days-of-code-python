def life_in_weeks(age, max_age):
    rem_age = max_age-age
    age_in_weeks = rem_age*52
    print(f"You have {age_in_weeks} weeks left before you hit {max_age}.")
    
age = int(input("What is your age?: "))
max_age = int(input("How long do you expect to live?: "))
life_in_weeks(age, max_age)