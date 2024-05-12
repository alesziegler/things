

headings = ["jmeno", "vek", "telefon"]

customers = []

customer_1 = {
    "jmeno": "Karel Novak",
    "vek": 20,
    "kontakt": "722458220"
}

customer_2 = {
    "jmeno": "Bara Soukupova",
    "vek": 21,
    "kontakt": "405821564"
}

customer_3 = {
"jmeno": "Jane Doe",
    "vek": 30,
    "kontakt": "401050230"
}

#print(type(customer_1))

#print(headings)

customers.append(customer_1)

customers.append(customer_2)

customers.append(customer_3)

#print(customers)

A = [[0, 1, 4, 'whatever', 3],
     [1, 0, 2, float('inf'), 4],
     [4, 2, 0, 1, 5],
     [float('inf'), 'next_whatever', 1, 0, 3],
     [3, 4, 5, 3, 0]]

for row in A:
    print(' '.join(['{:8}'.format(item) for item in row]))

"""
for heading in headings:
    print(heading,end=" ")
"""
print()

database = ""

for customer in customers:
    #print(' '.join(['{:8}'.format(['jmeno']) for ['jmeno'] in customer]))
    printed_customer = (
        f"{customer['jmeno']},{customer['vek']},{customer['kontakt']}\n")
    database += printed_customer


#database += str(customer['vek'])
#database += customer['kontakt']

print(database)

def find_something(query,database,identifier):
    count = 0
    print("Vysledky hledani:")
    for customer in database:
        if str(customer[identifier].lower()) == query.lower():
            for identifier in customer:
                print(f"{identifier}: {customer[identifier]},",end=" ")

            count += 1
        print(end="\n")
    print(f"nalezeno {count} vysledku.")


find_something("blabla",customers,'jmeno')

print()

find_something("Jane",customers,'jmeno')

find_something("Jane Doe",customers,'jmeno')

find_something("405821564",customers,'kontakt')

