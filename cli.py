from House import House

house = House()

while True:
    print("What would you like to do?")
    choice = input("1. open door 2. close door 3. turn on heating 4. turn off heating 5. do nothing: ")

    if choice.startswith('1'):
        house.open_door()
        print('The door is now open.')
    elif choice.startswith('2'):
        house.close_door()
        print('The door is now closed.')
    elif choice.startswith('3'):
        house.start_heating()
        print('The heating is now on.')
    elif choice.startswith('4'):
        house.stop_heating()
        print('The heating is now off.')
    elif choice.startswith('5'):
        print("You've done nothing.")
    else:
        print('Invalid choice.')
        continue

    house.process_moment()
    house.print_stats()
    print()
