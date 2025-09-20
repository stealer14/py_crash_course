audience_follower = [7, 4, 3, 100, 765, 2344, 1, 2, 32] #total is 5056
empty_list = []

#estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )

total_spread = 0
num_followers = len(audience_follower)
sum_followers = sum(audience_follower)
avg_followers = sum_followers / num_followers

spread = avg_followers * (sum_followers ** 1.2)
    
'''
for i in audience_follower:
    spread = avg * (sum ** 1.2)
    print(i, spread)
    total_spread += spread
'''
print(spread)