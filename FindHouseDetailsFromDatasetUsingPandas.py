import pandas as pd


#code by sakib
data = { 
    'Area': [2000, 1800, 2500, 2200, 1900, 2800, 2100, 1700, 2400, 2000], 
    'Bedrooms': [3, 2, 4, 3, 2, 5, 4, 2, 3, 3], 
    'Bathrooms': [2, 1.5, 3, 2.5, 2, 3.5, 2.5, 1, 3, 2], 
    'Age': [10, 5, 15, 8, 3, 20, 12, 6, 18, 9], 
    'Location': ['Suburban', 'Urban', 'Rural', 'Suburban', 'Urban', 'Rural', 'Suburban', 'Urban', 'Rural', 'Suburban'], 
    'Garage_Size': [400, 300, 500, 450, 350, 600, 400, 250, 550, 400], 
    'Yard_Size': [800, 600, 1000, 900, 700, 1200, 800, 500, 1100, 800], 
    'Amenities': [1, 0, 1, 1, 0, 1, 1, 0, 1, 1], 
    'School_Rating': [8, 7, 6, 9, 8, 5, 7, 6, 4, 8], 
    'Distance_to_City_Center': [5, 2, 10, 7, 4, 15, 6, 3, 12, 5], 
    'Price': [300000, 250000, 350000, 320000, 280000, 400000, 310000, 240000, 370000, 300000] 
}

df = pd.DataFrame(data)
print(df)

def print_house_details(index):
    print(f"House {index+1}:")
    print(f"  Area: {df.at[index, 'Area']} sq ft")
    print(f"  Bedrooms: {df.at[index, 'Bedrooms']}")
    print(f"  Bathrooms: {df.at[index, 'Bathrooms']}")
    print(f"  Age: {df.at[index, 'Age']} years")
    print(f"  Location: {df.at[index, 'Location']}")
    print(f"  Garage Size: {df.at[index, 'Garage_Size']} sq ft")
    print(f"  Yard Size: {df.at[index, 'Yard_Size']} sq ft")
    print(f"  Amenities: {'Yes' if df.at[index, 'Amenities'] == 1 else 'No'}")
    print(f"  School Rating: {df.at[index, 'School_Rating']} / 10")
    print(f"  Distance to City Center: {df.at[index, 'Distance_to_City_Center']} miles")
    print(f"  Price: ${df.at[index, 'Price']:,}\n")


for i in range(len(df)):
    print_house_details(i)