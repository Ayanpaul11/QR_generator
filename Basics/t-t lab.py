import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [30, 20, 15, 35]  # Percentages for each label

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add a title
ax.set_title('Fruit Distribution')

# Show the chart
plt.show()
