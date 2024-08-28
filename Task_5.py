import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import plotly.express as px
df = pd.read_csv('cleaned.csv')
print(df.head())
print(df.columns)
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)
    heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]
    HeatMap(heat_data).add_to(m)
    m.save('accident_heatmap.html')
else:
    print("Latitude and Longitude columns are not available for hotspot analysis.")

plt.figure(figsize=(8, 6))  
sns.countplot(data=df, x='Road_surface_type', palette='magma', hue='Road_surface_type', legend=False)
plt.title('Accidents by Road Surface Type')
plt.xlabel('Road Surface Type')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.savefig('accidents_by_road_surface_type.png')
plt.show()
plt.figure(figsize=(8, 6))  
sns.countplot(data=df, x='Weather_conditions', palette='viridis', hue='Weather_conditions', legend=False)
plt.title('Accidents by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right')   
plt.grid(True)
plt.savefig('accidents_by_weather_conditions.png')
plt.show()
plt.figure(figsize=(8, 6))  
sns.countplot(data=df, x='Light_conditions', palette='cividis', hue='Light_conditions', legend=False)
plt.title('Accidents by Light Conditions')
plt.xlabel('Light Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right')  
plt.grid(True)
plt.savefig('accidents_by_light_conditions.png')
plt.show()
plt.figure(figsize=(8, 6))  
sns.countplot(data=df, x='Types_of_Junction', palette='crest', hue='Types_of_Junction', legend=False)
plt.title('Accidents by Types of Junction')
plt.xlabel('Types of Junction')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right')  
plt.grid(True)
plt.savefig('accidents_by_types_of_junction.png')
plt.show()
plt.figure(figsize=(8, 6))  
sns.countplot(data=df, x='Cause_of_accident', palette='rocket', hue='Cause_of_accident', legend=False)
plt.title('Accidents by Cause of Accident')
plt.xlabel('Cause of Accident')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45, ha='right')  
plt.grid(True)
plt.savefig('accidents_by_cause_of_accident.png')
plt.show()

 
fig = px.scatter(df, x='Road_surface_type', y='Weather_conditions', color='Accident_severity',
                 title='Accidents by Road Surface Type and Weather Conditions',
                 labels={'Road_surface_type': 'Road Surface Type', 'Weather_conditions': 'Weather Conditions'})
fig.write_html('interactive_dashboard.html')
