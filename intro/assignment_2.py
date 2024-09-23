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



departments = data['company']['departments']

employees = data['company']['departments'][0]['employees']

alice_prjs = employees[0]['projects']


for department in departments:
    print(department['name'])


for employee in employees:

    print(f"Name: {employee['name']} -- Role: {employee['role']}\n")


print("this is a list of all alice projects")
for prj in alice_prjs:
    
    print(f"""
Name: {prj['name']}
Status: {prj['status']}
""")
   


branding_budget = data['company']['departments'][1]['employees'][0]['campaigns'][1]['budget']

print(branding_budget)

data['company']['departments'][0]['employees'][0]['projects'][1]['status'] = "completed"
data['company']['departments'][0]['employees'][1]['projects'].append({'name': 'Epsilon', 'status': 'planned'})
data['company']['departments'][1]['employees'][0]['campaigns'][0]['budget'] += 2000


staffs1 = len(departments[0]['employees'])
staffs2 = len(departments[1]['employees'])





report = f"""


Data Reports:

The amount of staffs in Engineering is; {staffs1}

The amoount of staffs in Markteting is; {staffs2}


"""

print(report)


                          
                          
                          
                          
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


