import matplotlib.pyplot as plt

# Given data
data = [20, 22, 21, 19, 23]

# Plotting histogram from given data
plt.figure(figsize=(8, 6))
plt.hist(data, bins=5, edgecolor='black', color='skyblue')
plt.title("Histogram of Given Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.xticks(range(min(data), max(data) + 1))

plt.show()