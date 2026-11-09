import matplotlib.pyplot as plt

tillar = ["Python", "C++", "JavaScript", "Java"]
oqquvchilar = [25, 8, 12, 5]

plt.figure(figsize=(6, 6))
plt.pie(
    oqquvchilar,
    labels=tillar,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
)
plt.title("Sinf o'quvchilarining sevimli dasturlash tillari")

plt.show()