p1 = " Make a lot of money"
p2 = " Buy now"
p3 = " Subscribe this"
p4 = " Click this"
message  = input("Enter your message")
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("Spam")
else:
    print("Thank you for your comment")
