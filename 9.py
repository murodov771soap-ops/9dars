import matplotlib.pyplot as plt

hafta_kunlari = ["Dush", "Sesh", "Chor", "Pay", "Juma", "Shan", "Yak"]
faollik = [3, 5, 2, 6, 4, 7, 5]

plt.plot(hafta_kunlari, faollik, marker="o", color="darkcyan")
plt.title("Haftalik faollik grafigi")
plt.xlabel("Kunlar")
plt.ylabel("Soat")
plt.grid(True)


plt.savefig("natija.png")

plt.show()