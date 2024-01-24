def predictAnswer(stockData, queries):
    # Function to find the closest day with a lower price
    def find_nearest_lower_day(query_day, stockData):
        # Price on the query day
        query_price = stockData[query_day - 1]  # -1 for zero-based index
        # Search for the closest lower price in both directions
        left_day, right_day = query_day - 2, query_day  # Start from adjacent days
        while left_day >= 0 or right_day < len(stockData):
            # Check left side
            if left_day >= 0 and stockData[left_day] < query_price:
                return left_day + 1  # +1 to convert back to one-based index
            # Check right side
            if right_day < len(stockData) and stockData[right_day] < query_price:
                return right_day + 1  # +1 to convert back to one-based index
            # Move outwards
            left_day -= 1
            right_day += 1
        # If no such day exists, return -1
        return -1
    

    # Process each query and store the result
    result = [find_nearest_lower_day(day, stockData) for day in queries]
    return result

# Example usage with the data provided in the image:
n = 10
stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
queries = [6, 5, 4]

# Call the function with the example data
print(predictAnswer(stockData, queries))

