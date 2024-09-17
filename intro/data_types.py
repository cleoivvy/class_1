# list_fruits =[
#     "apple",
#     "mango",
#     "banana",
#     "orange",
#     "grapes"
# ]

# print(list_fruits)
# print(type(list_fruits))

# list_fruits [2] = 2001
# list_fruits [-1] = True
# list_fruits [1] = 20.13
# print(list_fruits)

# list_numbers = [1, 2, 3, 4, 5]
# list_numbers.insert(3, 6)
# print(list_numbers[2:])
# print(list_numbers)

# list_fruits.append("strawberry")
# list_fruits.append([23, 34])
# list_fruits[-1].insert(-1, "kiwi")
# list_fruits.insert(1, "guava")
# print(list_fruits)


# list_cars = [
#     "G-wagon",
#     "Corrola",
#     "Mercedes",
#     "Toyota"
# ]

# list_fruits.extend(list_cars)

# list_fruits.remove("apple")
# list_fruits.reverse()
# list_fruits.sort(reverse=True)
# print(list_fruits)



list_data = [
    1, 2, 3, 4, 5, [2, 4, 6, 1], 6, [3, 6, 8, 1]
]
list_data[5].sort()
list_data[7].sort()
print(list_data)


data = {
    "name": "Clara",
    "status": "Resident"
}
print(data)
data["name"] = "kamso"
data["age"] = 23
print(data)




nested = {
    "full_name": "Kamso Dan",
    "age": 27,
    "status": "unsingle",
    "address": {
        "street": "123 Main street",
        "city": "Lagos",
        "code": [
            1000001,
            1200001,
            1000541
        ]
    },
    "religion": "Christianity",
    "church": {
        "type":{
            "name": "Catholic",
            "Location": "Lagos",
            "address": {
                "street": "123 Main street",
                "city": "Lagos",
                "code": [
                    1011001,
                    1223001,
                    1034541
                ]
            }
        }
    }
}
print(nested["church"]["type"]["address"]["code"][1])

test_1 = [15782183, 21626139]
test_2 = [23643652,276479866]

nested["address"]["code"].extend(test_1)
nested["church"]["type"]["address"]["code"].extend(test_2 )
print(nested)

