my_family = {
    "sister": {
        "name": "carmen",
        "age": 25
    },
    "mother": {
        "name": "Margrita",
        "age": 55
    },
    "uncle": {
        "name": "Luis",
        "age": 61
    },
    "aunt": {
        "name": "Norma",
        "age": 70
    },
    "dad": {
        "name": "Jorge",
        "age": 61
    },
    "grandpa": {
        "name": "Julian",
        "age": 93
    }
}

# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old

for ftitle, finfo in my_family.items():

    # print(ftitle, finfo)

    print(finfo['name'] + ' is my ' + ftitle + ' and is ' + str(finfo['age']) + ' years old.')

