# Experiment 7: Heatmaps and Tree Maps
# Run: pip install pandas seaborn squarify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

df = pd.DataFrame({
    "Sales": [100, 150, 120, 180, 90, 130],
    "Profit": [20, 35, 25, 50, 15, 28],
    "Quantity": [5, 8, 6, 9, 4, 7]
})
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap"); plt.tight_layout(); plt.show()

sizes = [500, 300, 200, 150]
labels = ["Furniture", "Technology", "Office Supplies", "Accessories"]
squarify.plot(sizes=sizes, label=labels, alpha=0.8)
plt.axis("off"); plt.title("Category-wise Sales Treemap"); plt.show()
