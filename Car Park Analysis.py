cars = []

with open('car_park.txt', encoding="utf8") as file:
    next(file)
    for line in file:
        line = line.rstrip('\n')
        split = line.split(',')
        car = dict(
            license = split[0],
            manufacturer = split[1],
            model = split[2],
            year = int(split[3])
        )
        cars.append(car)

def print_all_cars(comment):
    print(comment)
    for car in cars:
        print(cars)

print_all_cars(comment='Cars in the car park:')

print()
print('1.\n')
#
# # 1. Find which manufacturers have more than one car, print the manufacturer names on the screen.
#
def manufacturers():
    list_of_manufacturers = []
    for car in cars:
        list_of_manufacturers.append(car['manufacturer'])
    return list_of_manufacturers

def manufacturers_of_more_than_one_car():
    more_than_one = []
    for manufacturer in manufacturers():
        if manufacturers().count(manufacturer) > 1:
            more_than_one.append(manufacturer)
    unique_more_than_one = set(more_than_one)
    return unique_more_than_one

def print_manufacturers_of_more_than_one_car(comment, unique_more_than_one):
    print(comment)
    for number, manufacturer in enumerate(unique_more_than_one, 1):
        print(f'{number}. {manufacturer}')

unique_more_than_one = manufacturers_of_more_than_one_car()
print_manufacturers_of_more_than_one_car(comment='Manufacturers with more than one car in the car park:',
                                              unique_more_than_one=unique_more_than_one)

print()
print('2.\n')

# 2. Make a list of all cars of the selected manufacturer (e.g. Volvo),
# print the car's license plate number, model, and year of manufacture on the screen.
# If such car is not in the list, print the message:
# "There are no cars by this manufacturer in the list.".

def cars_by_selected_manufacturer():
    cars_by_manufacturer = []
    while True:
        manufacturer = input("Which manufacturer's cars would you like to see?: ")
        found = False
        for car in cars:
            if car['manufacturer'] == manufacturer:
                cars_by_manufacturer.append(car)
                found = True
        if not found:
            print('There are no cars by this manufacturer in the list.')
        else:
            break
    return cars_by_manufacturer

def printing_and_writing(comment, cars):
    with open('Cars.txt', 'w', encoding='utf8') as file:
        print(comment)
        file.write(comment + '\n')
        for number, car in enumerate(cars, 1):
            print(f'{number}. License plate number: {car["license"]}, model: {car["model"]}, year: {car["year"]}')
            file.write(f'{number}. License plate number: {car["license"]}, model: {car["model"]}, year: {car["year"]}\n')

selected_cars = cars_by_selected_manufacturer()
printing_and_writing(comment=f'Cars by {selected_cars[0]["manufacturer"]}:',
                         cars=selected_cars)

print()
print('3.\n')

# 3. Make a list of cars older than 10 years, and enter all their data into the file "Old_Cars.csv".
# If the program does not find any antiques, print a message on the screen
# "There are no cars older than 10 years in the list".

import datetime
from csv import writer

def finding_old_cars(cars):
    old_cars = []
    for car in cars:
        if datetime.datetime.now().year - car["year"] >= 10:
            old_cars.append(car)
    return old_cars

def printing_and_writing_old_cars(comment, old_cars):
    with open('Old_Cars.csv', 'w', newline='') as file1:
        csv_writer = writer(file1)
        if len(old_cars) == 0:
            print('There are no cars that are older than 10 years.')
            csv_writer.writerow(['There are no cars that are older than 10 years.'])
        else:
            print('Cars older than 10 years:')
            csv_writer.writerow(['Cars older than 10 years:'])
            csv_writer.writerow(['Nr.', 'License Nr.', 'Manufacturer', 'Model', 'Year'])
            for number, car in enumerate(old_cars, 1):
                print(number, car)
                csv_writer.writerow([number, car["license"], car["manufacturer"], car["model"], car["year"]])

old_cars = finding_old_cars(cars)
printing_and_writing_old_cars(comment='Cars older than 10 years:', old_cars=old_cars)
