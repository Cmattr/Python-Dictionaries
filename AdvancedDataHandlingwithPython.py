hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

print(''' Main Menu
      1. book a room
      2. check out
      3. check status of rooms''')
menu_select = input("please select an option: ")

#Task 1: Hotel Room Booking Tracker
def check_status(hotel_rooms):
    for status in hotel_rooms:
        print(hotel_rooms[status])

def book_room(hotel_rooms):
    name = input("please enter your first and last name: ")
    room_number = input("please enter the room number you would like to reserve: ")
    hotel_rooms [room_number] ["customer"] = name
    for room, status in hotel_rooms.items():
        vacancy = status["status"]
        if vacancy == "available":
            status['status'] = "booked"
        
def check_out(hotel_rooms):
    room = input("please enter your room number to check out: ")
    hotel_rooms [room] ["status"] = "available" 
    hotel_rooms [room] ["customer"] = "" 

if menu_select == "check status of rooms":
    i = check_status(hotel_rooms)
    print(i)
    
if menu_select == "book a room":
    book_room(hotel_rooms)
    print(hotel_rooms)

if menu_select == "check out":
    check_out(hotel_rooms)
    print(hotel_rooms)