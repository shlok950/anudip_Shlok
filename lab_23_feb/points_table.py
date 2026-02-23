# Sports Tournament Points Table

# Take team points input from user (space separated)
points = list(map(int, input("Enter team points separated by space: ").split()))

print("Original Points:", points)

# 1. Replace negative points with 0
points = [p if p >= 0 else 0 for p in points]
print("After Replacing Negative Points with 0:", points)

if len(points) == 0:
    print("No teams available.")
else:
    # 2. Sort leaderboard in descending order
    leaderboard = sorted(points, reverse=True)
    print("Leaderboard (Descending):", leaderboard)

    # 3. Find winner and runner-up
    winner = leaderboard[0]
    runner_up = leaderboard[1] if len(leaderboard) > 1 else None

    print("Winner Points:", winner)
    if runner_up is not None:
        print("Runner-up Points:", runner_up)
    else:
        print("No Runner-up Available")