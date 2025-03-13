def ticket_price(age):
    if age < 5:
        return "Free"
    elif 5 <= age <= 17:
        return "$5"
    elif 18 <= age <= 64:
        return "$10"
    else:
        return "Senior Discount - $7"

# TODO: Write test cases for all paths
print(ticket_price(3))
print(ticket_price(8))
print(ticket_price(47))
print(ticket_price(1897))