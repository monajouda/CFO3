list_chair = []
class bus:
    count_of_chair = 30
    def init(self ,destination_from ,destination_to):
        self.destination_from = destination_from
        self.destination_to = destination_to

#North of the sector * South of the sector * West of the sector * East of the sector

bus1 = bus('North of the sector','cairo')
bus2 = bus('South of the sector','cairo')
bus3 = bus('West of the sector ','cairo')
bus4 = bus('East of the sector','cairo')


bus5 = bus('cairo','North of the sector')
bus6 = bus('cairo','South of the sector')
bus7 = bus('cairo','West of the sector ')
bus8 = bus('cairo','East of the sector')

def display():

    print('''
    1-from North of the sector to cairo
    2-from South of the sector to cairo
    3-from West of the sector to cairo
    4-from East of the sector to cairo
    5-from  cairo to North of the sector 
    6-from  cairo to South of the sector 
    7-from  cairo to West of the sector 
    8-from  cairo to  East of the sector 
    ''')


Destination = input('If you want to see the destinations,enter T if not enter F\t:')
if Destination == 'T':
    display()
else:
    exit()
while True:

    q = input('If you want to reserve a seat, enter T , if no, enter F\t:')
    if q == 'T':
        n = int(input('Enter The number destination'))
        print('How many chairs are left', 30-len(list_chair))
        num = int(input("Enter The number chair who you want to book : "))
        if num not in list_chair:
            list_chair.append(num)
            print('The opration successfully')
        else:
            print('The chair is reserved')
    else:
        exit()
    if len(list_chair) == 30:

        exit()