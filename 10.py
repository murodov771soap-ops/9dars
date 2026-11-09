import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]


plt.bar(ismlar, ballar, color="royalblue", edgecolor="black")
plt.title("O'quvchilarning ballari tahlili")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(axis="y", linestyle="--")


eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = sum(ballar) / len(ballar)

print(f"Eng yuqori ball: {eng_yuqori}")
print(f"Eng past ball: {eng_past}")
print(f"O'rtacha ball: {ortacha:.2f}")

plt.savefig("oquvchilar_natijasi.png")

plt.show()

