def oa1():
    seen = set()
    res = []
    for i in logs[::-1]:
        if i in seen:
            continue
        seen.add(i)
        res.append(i)
    return res

def findMinimumInefficiency(serverType):
    # Helper function to count the inefficiency
    def count_inefficiency(s):
        return sum(1 for i in range(1, len(s)) if s[i] != s[i-1])

    # Convert string into list for easier manipulation
    servers = list(serverType)
    n = len(servers)
    
    # If there's only one type of server or all are unknown, simply return 0
    if all(s == servers[0] for s in servers):
        return 0

    # Go through the list and set the server type wherever it's '?'
    i = 0
    while i < n:
        # If server type is known, skip to the next
        if servers[i] in ['0', '1']:
            i += 1
            continue
        
        # Find the range of '?'
        j = i
        while j < n and servers[j] == '?':
            j += 1
        
        # Decide the server type for the range
        if i > 0 and j < n:
            # Both sides have known server types
            if servers[i-1] == servers[j]:
                # Both sides are the same, so fill all with that type
                for k in range(i, j):
                    servers[k] = servers[i-1]
            else:
                # Both sides are different, so fill half and half
                mid = (i+j) // 2
                for k in range(i, mid):
                    servers[k] = servers[i-1]
                for k in range(mid, j):
                    servers[k] = servers[j]
        elif i == 0:
            # Only the right side is known
            for k in range(i, j):
                servers[k] = servers[j]
        else:
            # Only the left side is known
            for k in range(i, j):
                servers[k] = servers[i-1]

        i = j

    # Return the inefficiency of the final configuration
    return count_inefficiency(servers)

# Test Cases
print(findMinimumInefficiency("00?10??1?1"))  # Expected output: 3
print(findMinimumInefficiency("????"))  # Expected output: 0