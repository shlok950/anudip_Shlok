# Movie Rating System

# Take ratings input from user (space separated)
ratings = list(map(int, input("Enter ratings (1–5) separated by space: ").split()))

print("Original Ratings:", ratings)

# 1. Remove invalid ratings (not between 1 and 5)
valid_ratings = [r for r in ratings if 1 <= r <= 5]
print("Valid Ratings:", valid_ratings)

if len(valid_ratings) == 0:
    print("No valid ratings available.")
else:
    # 2. Find average rating
    average_rating = sum(valid_ratings) / len(valid_ratings)
    print("Average Rating:", round(average_rating, 2))

    # 3. Count how many 5-star ratings
    five_star_count = valid_ratings.count(5)
    print("Number of 5-Star Ratings:", five_star_count)

    # 4. Sort ratings in ascending order
    valid_ratings.sort()
    print("Ratings in Ascending Order:", valid_ratings)