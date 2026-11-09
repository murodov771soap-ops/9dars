import matplotlib.pyplot as plt

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 78, 90, 88]

plt.bar(fanlar, ballar, color="skyblue")
plt.title("Fanlardan olingan ballar")
plt.xlabel("Fanlar")
plt.ylabel("Ballar")
plt.grid(axis="y", linestyle="--")

plt.show()