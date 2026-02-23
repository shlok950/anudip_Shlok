# Temperature Monitoring System

# Take daily temperatures input (space separated)
temperatures = list(map(float, input("Enter daily temperatures separated by space: ").split()))

print("Original Temperatures:", temperatures)

if len(temperatures) == 0:
    print("No temperature data available.")
else:
    # 1. Find hottest and coldest day
    hottest = max(temperatures)
    coldest = min(temperatures)

    hottest_day = temperatures.index(hottest) + 1
    coldest_day = temperatures.index(coldest) + 1

    print(f"Hottest Day: Day {hottest_day} ({hottest}°C)")
    print(f"Coldest Day: Day {coldest_day} ({coldest}°C)")

    # 2. Replace temperatures above 45°C with "Heat Alert"
    modified_temps = []
    for temp in temperatures:
        if temp > 45:
            modified_temps.append("Heat Alert")
        else:
            modified_temps.append(temp)

    print("After Heat Alert Replacement:", modified_temps)

    # 3. Count number of extreme days (> 40°C)
    extreme_days = sum(1 for temp in temperatures if temp > 40)
    print("Number of Extreme Days (> 40°C):", extreme_days)
    