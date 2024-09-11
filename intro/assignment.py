first_name = "Clara"
last_name = "Ojobo"
age = 23

# Concatenate first_name and last_name
full_name = first_name + " " + last_name 

print(full_name)

# String formatting
intro = f""" My name is {full_name} and I am {age} years old. """
print(intro)

hobby = "Reading"
hobby_message = f""" I love {hobby} in my free time """
print(hobby_message)

# string concatenation
personal_info = "My name is " + first_name + " " + last_name + ", I am " + str(age) + " years old, and I love " + hobby + " in my free time"
print(personal_info)

# string formatting
personal_info = f"""My name is {first_name} {last_name}. I am {age} years old and i love {hobby} in my free time.
"""
print(personal_info)