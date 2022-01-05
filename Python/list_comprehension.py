# new_list = [ i for i in list if i > something]


employees = [
    {'name': 'John Conners', 'seniority': 10},
    {'name': 'River Tam', 'seniority': 3},
    {'name': 'Bilbo Baggins', 'seniority': 12},
    {'name': 'Harry Potter', 'seniority': 7},
    {'name': 'Darth Revan', 'seniority': 19},
    {'name': 'Khan', 'seniority': 6},
    {'name': 'Dobbie', 'seniority': 1},
    {'name': 'R2D2', 'seniority': 6}
]

# Challenge #1
filtered_employees_one = [i['name'] for i in employees if i['seniority']>= 10]

if filtered_employees_one == ['John Conners', 'Bilbo Baggins', 'Darth Revan']:
    print('SUCCESS Test One')

# Challenge #2
filtered_employees_two = [i['name'] for i in employees if i['seniority'] % 3 == 0 ]

if filtered_employees_two == ['River Tam', 'Bilbo Baggins', 'Khan', 'R2D2']:
    print('SUCCESS Test Two')