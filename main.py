#import pyplot to generate charts and visualize data
# import numpy to create arrays for number of people and costs
import matplotlib.pyplot as plt
import numpy as np

# nutritional cost problem data
profiles = ['Persona Enferma', 'Adulto Joven', 'Intolerante']
unit_costs = [4.10, 2.80, 3.70] # USD per person/day
quantities = [5, 10, 5] # numbers of people per profile
# Total cost per profile (unit cost x number of people)
total_costs = [4.10*5, 2.80*10, 3.70*5]

# Create a new figure to display the charts,
# and define the size in inches
plt.figure(figsize=(15, 5))

# === Chart 1: Unit cost per profile ===
# Create a figure 1 row x 3 columns, position 1
plt.subplot(1, 3, 1)
# Create a bar chart x-axis, y-axis and colors
plt.bar(profiles, unit_costs, color=['#FF9999','#66B2FF','#99FF99'])
plt.title('Costo diario por persona') # title's name
plt.ylabel('USD') # y-axis' name
# Display backgorund grid with the level of transparency
plt.grid(True, linestyle='--', alpha=0.6)

# === Chart 2: Total cost distribution ===
# 1 row x 3 columns, position 2
plt.subplot(1, 3, 2)
# pie chart' distribution:
# - totalcosts' size, slice' labels, slice' percent with one decimal
# - start angle in the 90 grades position, slice' colors
plt.pie(total_costs, labels=profiles, autopct='%1.1f%%', startangle=90,
        colors=['#FFB6B9','#A2CFFE','#C9F0DD'])
plt.title('Distribución del costo total') # pie chart' name

# === Chart 3: Cartesian plot (Total cost vs number of people) ===
x = np.arange(0, 21) # Generate a sequence (0 to 20 persons)
plt.subplot(1, 3, 3) # 1 row x 3 columns in third position
#traverse the range of the list of profiles with index i
#that will take the values 0,1,2
for i in range(len(profiles)):
    y = unit_costs[i] * x #multiply each array value  per unit cost
#draw a line with numbers of persons, total costs, lines' names
# draw a (x,y)point and the point' size
    plt.plot(x, y, label=f'{profiles[i]} (${unit_costs[i]:.2f}/persona)', marker='o', markersize=4)
plt.title('Costo Total vs Número de Personas') # chart' name
plt.xlabel('Número de personas') #x-axis's name
plt.ylabel('Costo diario (USD)') #y-axis's name
#background grid and level
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend() #show the legend with the support of plt.plot
plt.tight_layout() # fix the chart's size automatically
plt.show() # shows the charts
