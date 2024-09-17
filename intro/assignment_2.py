data = {
    "company": {
        "departments": [
            {
                "name": "Engineering",
                "employees":[
                    {
                        "id": 101,
                        "name" : "Alice",
                        "role": "software Engineer",
                        "projects" : [
                            {"name" : "Alpha",
                             "status" : "completed"},
                            {
                                "name": "Beta",
                                "status" : "in progress"}
                        ]
                    },
                    {
                        "id" : 102,
                        "name" : "Bob",
                        "role": "DevOps Engineer",
                        "projects": [
                            {
                                "name": "Gamma",
                                "status": "completed"
                            },
                            {
                                "name": "Delta",
                                "status": "not started"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Marketing",
                "employees" : [
                    {
                        "id" : 201,
                        "name": "charlie",
                        "role": "Content Strategist",
                        "campaigns": [
                            {
                                "title": "Product Launch",
                                "budget": 5000
                            },
                            {
                                "title": "Rebranding",
                                "budget": 8000
                            }
                        ]
                    }
                ]
            }
        ]
    }
}



# Departments in the company
department_1 = data["company"]["departments"][0]["name"]
department_2 = data["company"]["departments"][1]["name"]
print(department_1, " ",  department_2)

# Engineers in the company
engineer_1 = data["company"]["departments"][0]["employees"][0]["name"]
engineer_2 = data["company"]["departments"][0]["employees"][1]["name"]
print(engineer_1, " ", engineer_2)

# Alice's projects
alice_project = data["company"]["departments"][0]["employees"][0]["projects"]
print(alice_project)


# Budget for rebranding
rebranding = data["company"]["departments"][1]["employees"][0]["campaigns"][1]
print(rebranding)


# Modify the nested data
# new_project = {"name": "epsilon", "status" : "planned"}
# bob_project = data["company"]["departments"][0]["employees"][1]["projects"]
# update_bob =bob_project.append(new_project)
# print(update_bob)
# there's an issue with this one


# new_budget = data["company"]["departments"][1]["employees"][0]["campaigns"][0]["budget"] + 2000
# product_launch = data["company"]["departments"][1]["employees"][0]["campaigns"]
# new_launch = product_launch.append(new_budget)
# print(new_launch)
# there's an issue with this as well
                          
                          
                          
                          
# destructuring the nested dictionary
print(data["company"])
print(data["company"]["departments"])

# departments in the company
print(data["company"]["departments"][0]["name"])

# employees in engineering
print(data["company"]["departments"][0]["employees"])

# alice in engineering
print(data["company"]["departments"][0]["employees"][0]["name"])

# projects that alice handles
print(data["company"]["departments"][0]["employees"][0]["projects"][0])
print(data["company"]["departments"][0]["employees"][0]["projects"][1])

# bob in engineering and the project he handles 
print(data["company"]["departments"][0]["employees"][1]["name"])
print(data["company"]["departments"][0]["employees"][1]["projects"])


# marketing department
print(data["company"]["departments"][1]["name"])

# the employee in marketing department
print(data["company"]["departments"][1]["employees"][0]["name"])

# the campaigns in marketing department
print(data["company"]["departments"][1]["employees"][0]["campaigns"])

# the title of the first campaign under marketing
print(data["company"]["departments"][1]["employees"][0]["campaigns"][0]["title"])

# the budget for product launch
print(data["company"]["departments"][1]["employees"][0]["campaigns"][0]["budget"])

# rebranding and it's budget
print(data["company"]["departments"][1]["employees"][0]["campaigns"][1]["title"])
print(data["company"]["departments"][1]["employees"][0]["campaigns"][1]["budget"])