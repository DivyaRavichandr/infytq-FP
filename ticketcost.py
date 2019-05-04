def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    ticket_amount=0
    Rate_per_adult=37550
    Rate_per_child=37550/3
    
    
    ticket_amount=(no_of_adults*Rate_per_adult)+(no_of_children*Rate_per_child)
    service_tax=0.07*ticket_amount
    total_cost=ticket_amount+service_tax 
    total_ticket_cost=total_cost-(0.1*total_cost)
    

    return total_ticket_cost



total_ticket_cost=calculate_total_ticket_cost(2,3)
print("Total Ticket Cost:",total_ticket_cost)
