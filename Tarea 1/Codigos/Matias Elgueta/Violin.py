import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset of Concerns for Privacy Information Practices and Consumer Behavior in Online Market_A survey in Vietnam.csv")

df["USU_avg"] = df[["USU1", "USU2", "USU3", "USU4"]].mean(axis=1)

age_labels = {
    1: "18–25",
    2: "26–35",
    3: "36–45",
    4: "46+"
}
df["Age Group"] = df["age"].map(age_labels)

df = df[df["Age Group"].notna()]

data = [df[df["Age Group"] == group]["USU_avg"] for group in age_labels.values()]

plt.figure(figsize=(10, 6))
plt.violinplot(data, showmedians=True, showmeans=True)
plt.xticks(ticks=range(1, len(age_labels)+1), labels=age_labels.values())
plt.title("Nivel promedio de preocupación por uso no autorizado de datos (USU) por grupo etario")
plt.ylabel("Promedio USU (1–5)")
plt.xlabel("Grupo etario")
plt.grid(True)
plt.tight_layout()
plt.show()
