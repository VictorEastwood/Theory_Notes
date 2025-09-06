import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set font to support Chinese characters
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Given three linearly independent vectors
v1 = np.array([1, 1, 1])
v2 = np.array([0, 1, 1])
v3 = np.array([0, 0, 1])

# Create a figure
fig = plt.figure(figsize=(18, 12))

# Step 1: First vector u1
ax1 = fig.add_subplot(231, projection='3d')
ax1.set_title('Step 1: First unit vector u1')

# Draw the original vectors
ax1.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='red', label='v1', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='blue', label='v2', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='green', label='v3', arrow_length_ratio=0.1)

# Calculate u1
u1 = v1 / np.linalg.norm(v1)
ax1.quiver(0, 0, 0, u1[0], u1[1], u1[2], color='black', linewidth=3, 
           label=f'u1 = ({u1[0]:.3f}, {u1[1]:.3f}, {u1[2]:.3f})', arrow_length_ratio=0.1)

ax1.set_xlim([-1, 1.5])
ax1.set_ylim([-1, 1.5])
ax1.set_zlim([-1, 1.5])
ax1.legend()
ax1.grid(True)

# Step 2: Calculation of the second vector w2
ax2 = fig.add_subplot(232, projection='3d')
ax2.set_title('Step 2: Compute second orthogonal vector w2')

# Retain the result from the previous step
ax2.quiver(0, 0, 0, u1[0], u1[1], u1[2], color='black', linewidth=3, 
           label='u1', arrow_length_ratio=0.1)

# Calculate projection of v2 onto u1 and then calculate w2
proj_v2_u1 = np.dot(v2, u1) * u1
w2 = v2 - proj_v2_u1

# Draw v2 and its projection onto u1
ax2.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='blue', label='v2', arrow_length_ratio=0.1)
ax2.quiver(0, 0, 0, proj_v2_u1[0], proj_v2_u1[1], proj_v2_u1[2], color='orange', 
           label='projection component', arrow_length_ratio=0.1)
ax2.quiver(proj_v2_u1[0], proj_v2_u1[1], proj_v2_u1[2], 
           w2[0], w2[1], w2[2], color='purple', 
           label=f'w2 = ({w2[0]:.3f}, {w2[1]:.3f}, {w2[2]:.3f})', arrow_length_ratio=0.1)

ax2.set_xlim([-1, 1.5])
ax2.set_ylim([-1, 1.5])
ax2.set_zlim([-1, 1.5])
ax2.legend()
ax2.grid(True)

# Step 3: Second vector u2
ax3 = fig.add_subplot(233, projection='3d')
ax3.set_title('Step 3: Second unit vector u2')

# Retain the previous results
ax3.quiver(0, 0, 0, u1[0], u1[1], u1[2], color='black', linewidth=3, 
           label='u1', arrow_length_ratio=0.1)

# Calculate and draw u2
u2 = w2 / np.linalg.norm(w2)
ax3.quiver(0, 0, 0, u2[0], u2[1], u2[2], color='red', linewidth=3, 
           label=f'u2 = ({u2[0]:.3f}, {u2[1]:.3f}, {u2[2]:.3f})', arrow_length_ratio=0.1)

ax3.set_xlim([-1, 1.5])
ax3.set_ylim([-1, 1.5])
ax3.set_zlim([-1, 1.5])
ax3.legend()
ax3.grid(True)

# Step 4: Calculation of the third vector w3
ax4 = fig.add_subplot(234, projection='3d')
ax4.set_title('Step 4: Compute third orthogonal vector w3')

# Retain the previous results
ax4.quiver(0, 0, 0, u1[0], u1[1], u1[2], color='black', linewidth=3, 
           label='u1', arrow_length_ratio=0.1)
ax4.quiver(0, 0, 0, u2[0], u2[1], u2[2], color='red', linewidth=3, 
           label='u2', arrow_length_ratio=0.1)

# Calculate projections of v3 onto u1 and u2, then calculate w3
proj_v3_u1 = np.dot(v3, u1) * u1
proj_v3_u2 = np.dot(v3, u2) * u2
w3 = v3 - proj_v3_u1 - proj_v3_u2

# Draw v3 and its projections onto u1 and u2
ax4.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='green', label='v3', arrow_length_ratio=0.1)
ax4.quiver(0, 0, 0, proj_v3_u1[0], proj_v3_u1[1], proj_v3_u1[2], color='orange', 
           label='projection onto u1', arrow_length_ratio=0.1)
ax4.quiver(proj_v3_u1[0], proj_v3_u1[1], proj_v3_u1[2], 
           proj_v3_u2[0], proj_v3_u2[1], proj_v3_u2[2], color='yellow', 
           label='projection onto u2', arrow_length_ratio=0.1)
ax4.quiver(proj_v3_u1[0] + proj_v3_u2[0], 
           proj_v3_u1[1] + proj_v3_u2[1], 
           proj_v3_u1[2] + proj_v3_u2[2], 
           w3[0], w3[1], w3[2], color='purple', linewidth=2, 
           label=f'w3 = ({w3[0]:.3f}, {w3[1]:.3f}, {w3[2]:.3f})', arrow_length_ratio=0.1)

ax4.set_xlim([-1, 1.5])
ax4.set_ylim([-1, 1.5])
ax4.set_zlim([-1, 1.5])
ax4.legend()
ax4.grid(True)

# Step 5: Third vector u3
ax5 = fig.add_subplot(235, projection='3d')
ax5.set_title('Step 5: Third unit vector u3')

# Retain the previous results
ax5.quiver(0, 0, 0, u1[0], u1[1], u1[2], color='black', linewidth=3, 
           label='u1', arrow_length_ratio=0.1)
ax5.quiver(0, 0, 0, u2[0], u2[1], u2[2], color='red', linewidth=3, 
           label='u2', arrow_length_ratio=0.1)

# Calculate and draw u3
u3 = w3 / np.linalg.norm(w3)
ax5.quiver(0, 0, 0, u3[0], u3[1], u3[2], color='blue', linewidth=3, 
           label=f'u3 = ({u3[0]:.3f}, {u3[1]:.3f}, {u3[2]:.3f})', arrow_length_ratio=0.1)

ax5.set_xlim([-1, 1.5])
ax5.set_ylim([-1, 1.5])
ax5.set_zlim([-1, 1.5])
ax5.legend()
ax5.grid(True)

# Step 6: Final result - Standard orthogonal basis
ax6 = fig.add_subplot(236, projection='3d')
ax6.set_title('Step 6: Final orthonormal basis')

# Draw the final standard orthonormal basis
ax6.quiver(0, 0, 0, u1[0], u1[1], u1[2], color='black', linewidth=3, 
           label=f'u1 = ({u1[0]:.3f}, {u1[1]:.3f}, {u1[2]:.3f})', arrow_length_ratio=0.1)
ax6.quiver(0, 0, 0, u2[0], u2[1], u2[2], color='red', linewidth=3, 
           label=f'u2 = ({u2[0]:.3f}, {u2[1]:.3f}, {u2[2]:.3f})', arrow_length_ratio=0.1)
ax6.quiver(0, 0, 0, u3[0], u3[1], u3[2], color='blue', linewidth=3, 
           label=f'u3 = ({u3[0]:.3f}, {u3[1]:.3f}, {u3[2]:.3f})', arrow_length_ratio=0.1)

# Add a unit sphere to show the length of the unit vectors
phi = np.linspace(0, np.pi, 30)
theta = np.linspace(0, 2 * np.pi, 30)
x = np.outer(np.sin(phi), np.cos(theta))
y = np.outer(np.sin(phi), np.sin(theta))
z = np.outer(np.cos(phi), np.ones_like(theta))
ax6.plot_wireframe(x, y, z, color='gray', alpha=0.1)

ax6.set_xlim([-1, 1.5])
ax6.set_ylim([-1, 1.5])
ax6.set_zlim([-1, 1.5])
ax6.legend()
ax6.grid(True)

plt.tight_layout()
plt.show()

# Print numerical results
print("Original vectors:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}\n")

print("Gram-Schmidt results:")
print(f"u1 = {u1}")
print(f"u2 = {u2}")
print(f"u3 = {u3}\n")

print("Verify orthogonality:")
print(f"u1·u2 = {np.dot(u1, u2):.6f}")
print(f"u1·u3 = {np.dot(u1, u3):.6f}")
print(f"u2·u3 = {np.dot(u2, u3):.6f}\n")

print("Verify unit length:")
print(f"||u1|| = {np.linalg.norm(u1):.6f}")
print(f"||u2|| = {np.linalg.norm(u2):.6f}")
print(f"||u3|| = {np.linalg.norm(u3):.6f}")