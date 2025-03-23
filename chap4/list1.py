#Looping thorough an entire list and priting eahc name
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
        
#Expanded using conditional structures
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    if magician == "alice":
        print(f"Hey {magician.title()}, that was not a great trick!")
    else:
        print(f"{magician.title()}, that was a great trick!")
        
#After the loop block is done
print("\nThank you, everyone. That was a great magic show!")