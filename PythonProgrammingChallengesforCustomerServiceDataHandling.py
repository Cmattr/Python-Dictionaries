service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

print(''' Main Menu
      1. open a new service ticket
      2. update the status of an existing ticket
      3. display tickets''')
menu_selection = input("please select an option: ")

def display_tickets(service_tickets):
    ticket_selection = input("open, closed, or all: ")
    if ticket_selection == "all":
        print(service_tickets)
    if ticket_selection == "open":
        for ticket, detail in service_tickets.items():
            if detail["Status"] == "open":
                print(f"ticket{ticket}:, Customer {detail["Customer"]}, Issue {detail["Issue"]}")
    if ticket_selection == "closed":
        for ticket, detail in service_tickets.items():
            if detail["Status"] == "closed":
                print(f"ticket{ticket}:, Customer {detail["Customer"]}, Issue {detail["Issue"]}")

def new_ticket(service_tickets):
    ticket = input("please enter a new ticket number")
    customer = input("please enter your name")
    issue = input("please provide a brief explination of your issue")
    service_tickets[ticket]= {"Customer": customer, "Issue": issue, "Status": "open"}

def update_status(service_ticket):
    update = input("Please input the ticket that you would like to update: ")
    for ticket, detail in service_tickets.items():
        if detail["Status"] == "open":
            detail["Status"] = "closed"       
    
        
    
if menu_selection == "display tickets":
    display = display_tickets(service_tickets)
    print(display)

if menu_selection == "open a new service ticket":
    new_ticket(service_tickets)
    print(service_tickets)

if menu_selection == "update the status of an existing ticket":
    update_status(service_tickets)
    print(service_tickets)
