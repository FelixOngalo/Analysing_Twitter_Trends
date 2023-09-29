# Get global trending topics
trends = api.get_place_trends(id=1)  # ID 1 corresponds to the global trends

# Print the trending topics
for trend in trends[0]['trends']:
    print(trend['name'])
