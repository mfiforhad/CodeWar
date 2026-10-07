employees = [ {'first_name': "Dipper", 'last_name': "Pines", 'role': "Boss"}, ]


def find_employees_role(name):
    arr = name.split()
    if len(arr) > 1:
        first_name = arr[0]
        last_name = arr[1]
        for e in employees:
            if e["first_name"] == first_name and e["last_name"] == last_name:
                return e["role"]
    elif len(arr) == 1:
        return "Should differentiate surname and name: None should equal 'Does not work here!"
    else:
        return "Does not work here!"


print(find_employees_role("Dipper Pines"))
