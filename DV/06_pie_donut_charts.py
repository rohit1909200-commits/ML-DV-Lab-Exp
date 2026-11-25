# Experiment 6: Pie and Donut Charts for Category Proportion
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"Country": ["India", "USA", "China", "Japan"],
                   "Medals": [40, 30, 20, 10]})
plt.pie(df["Medals"], labels=df["Country"], autopct="%1.1f%%", startangle=90)
plt.title("Medal Share by Country"); plt.axis("equal"); plt.show()

fig, ax = plt.subplots()
ax.pie(df["Medals"], labels=df["Country"], autopct="%1.1f%%", startangle=90,
       wedgeprops={"width": 0.42})
ax.set_title("Donut Chart: Medal Share"); plt.show()
