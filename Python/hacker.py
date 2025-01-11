# def find_max_xor(lo, hi, k):
#     max_xor = -1  # Initialize the maximum XOR value
#     for a in range(lo, hi):
#         for b in range(a + 1, hi + 1):
#             xor_val = a ^ b
#             if xor_val <= k:
#                 max_xor = max(max_xor, xor_val)
#     return max_xor

# # Example usage:
# lo = 2
# hi = 4
# k = 8

# result = find_max_xor(lo, hi, k)
# print(f"The maximum possible value of a XOR b is: {result}")


from itertools import combinations

def count_valid_teams(skills, minPlayers, minLevel, maxLevel):
    # Filter the players whose skill levels are between minLevel and maxLevel, inclusive
    valid_players = [skill for skill in skills if minLevel <= skill <= maxLevel]
    
    # Generate all possible teams with at least minPlayers
    team_count = 0
    for r in range(minPlayers, len(valid_players) + 1):
        team_count += len(list(combinations(valid_players, r)))
    
    return team_count

# Example usage
skills = [12, 4, 6, 13, 5, 10]
minPlayers = 3
minLevel = 4
maxLevel = 10

result = count_valid_teams(skills, minPlayers, minLevel, maxLevel)
print(f"The number of valid teams is: {result}")
