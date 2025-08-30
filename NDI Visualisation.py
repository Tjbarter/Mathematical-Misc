import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Main Script ---

# Let a = pos, b = neg
# Create a grid of values for a (positive probability) and b (negative probability)
a_vals = np.linspace(0, 1, 101)
b_vals = np.linspace(0, 1, 101)
A, B = np.meshgrid(a_vals, b_vals)

# Using the simplified formula S = (a - b) / (a + b)
# We handle the division-by-zero case (where a=0, b=0) by setting the output to NaN
S = np.divide(A - B, A + B, out=np.full_like(A, np.nan), where=(A + B) != 0)

# The valid region for probabilities is a + b <= 1.
# We set the score outside this region to NaN so it is not plotted.
S[A + B > 1] = np.nan

# Create the figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
surf = ax.plot_surface(A, B, S, cmap='viridis', edgecolor='none')

# Set labels for the axes and a title for the plot
ax.set_xlabel('a (Positive Probability)')
ax.set_ylabel('b (Negative Probability)')
ax.set_zlabel('Sentiment Score')
ax.set_title('Sentiment Score vs. Positive and Negative Probabilities')
ax.view_init(elev=35, azim=-45) # Adjust viewing angle for clarity

# Add a color bar to map values to colors
fig.colorbar(surf, shrink=0.5, aspect=10, label='Sentiment Score')

# To display the plot
plt.show()