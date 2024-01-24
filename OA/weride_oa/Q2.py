# def taxiDriver(pickup, drop, tip):
#     # Initialize trips list where each trip is a tuple of (start, end, tip)
#     trips = sorted([(pickup[i], drop[i], tip[i]) for i in range(len(pickup))], key=lambda x: x[1])

#     # Initialize dp dictionary where key is drop location and value is the maximum profit
#     # at that point.
#     dp = {0: 0}

#     for start, end, extra_tip in trips:
#         # Find the time point to start this trip to get maximum profit
#         current_profit = 0
#         for time_point in sorted(dp.keys(), reverse=True):
#             if time_point <= start:
#                 current_profit = dp[time_point] + (end - start) + extra_tip
#                 break

#         # If the trip ends after all current recorded trips, add its profit to dp.
#         if end not in dp or current_profit > dp[end]:
#             dp[end] = current_profit

#     return max(dp.values())



def taxiDriver(pickup, drop, tip):
    # Combine all the trip details and sort by the drop-off location
    trips = sorted(zip(pickup, drop, tip), key=lambda x: x[1])
    
    # Initialize DP array where dp[i] will store the maximum profit
    # that can be made up to the i-th trip
    dp = [0] * len(trips)
    
    for i in range(len(trips)):
        # Earnings from the i-th trip without tip
        dp[i] = trips[i][1] - trips[i][0] + trips[i][2]
        
        # Check previous trips to see if we can chain the trips for a higher profit
        for j in range(i):
            if trips[j][1] <= trips[i][0]:  # If the j-th trip drop-off is before the i-th trip pickup
                dp[i] = max(dp[i], dp[j] + trips[i][1] - trips[i][0] + trips[i][2])
    
    # The maximum earnings will be the maximum value in the dp array
    return max(dp)

# Example from the problem statement
pickup = [0, 2, 9, 10, 11, 12]
drop = [5, 9, 11, 11, 14, 17]
tip = [1, 2, 3, 2, 2, 1]

# Calculate the maximum earnings
max_earnings = taxiDriver(pickup, drop, tip)
print(max_earnings)

pickup = [1,4]
drop = [5,6]
tip = [2,5]

max_earnings = taxiDriver(pickup, drop, tip)
print(max_earnings)


pickup = [0,4,5]
drop = [3,5,7]
tip = [1,2,2]

max_earnings = taxiDriver(pickup, drop, tip)
print(max_earnings)