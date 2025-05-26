from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

# Load image
try:
    array = ft_load("landscape.jpg")
except Exception as e:
    print(e)
    exit()

# Apply filters
effects = {
    "Original": array,
    "Inverted": ft_invert(array),
    "Red only": ft_red(array),
    "Green only": ft_green(array),
    "Blue only": ft_blue(array),
    "Grayscale": ft_grey(array),
}

# Display each result
plt.figure(figsize=(12, 8))
for i, (name, img) in enumerate(effects.items()):
    plt.subplot(2, 3, i + 1)
    if len(img.shape) == 2:  # Grayscale
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    plt.title(name)
    plt.axis('off')
plt.tight_layout()
plt.savefig("output.png")
plt.show()

# Print docstrings
print("\nDocstrings:\n")
print("ft_invert:", ft_invert.__doc__)
print("ft_red   :", ft_red.__doc__)
print("ft_green :", ft_green.__doc__)
print("ft_blue  :", ft_blue.__doc__)
print("ft_grey  :", ft_grey.__doc__)
