import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog'", "Shakar"]
sotilgan = [95, 50, 60, 30, 20]

plt.bar(mahsulotlar, sotilgan, color=["purple", "teal", "coral", "gold", "pink"])
plt.title("Do'konda bir haftada sotilgan mahsulotlar soni")
plt.xlabel("Mahsulotlar")
plt.ylabel("Soni")
plt.grid(axis="y", linestyle="--")

plt.show()

