print("Hello World!")

print (type(2))
print (type(2.4))
print (type("clara"))


name = "clara"
age, height = 23, 5.7

status = "single"

text = name + " is " + status
new_text = f"{name} is {status}"
print(new_text)
print(text)

name = "clara"
age = 23
status = "single"
hobby = "Reading"
school = "univelcity"
course = "backend"
bio = f"""Hi my name is {name}. i am {age} years old.
I am currently {status}. I love {hobby} in my free time. I am studying {course}
at {school}
"""
print(bio)

