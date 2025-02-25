import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\abhin\OneDrive\Documents\SIC\SIC\Car_Wash_Hackathon\data.csv"
df = pd.read_csv(file_path)

total_social_media_users = 40  
converted_social_media_users = df[df["Referral Source"] == "Social Media"].shape[0]
social_media_conversion_rate = (converted_social_media_users / total_social_media_users) * 100 if total_social_media_users > 0 else 0

print(f"Total Users from Social Media (Fixed): {total_social_media_users}")
print(f"Converted Users from Social Media: {converted_social_media_users}")
print(f"Social Media Conversion Rate: {social_media_conversion_rate:.2f}%")

fig, ax = plt.subplots(figsize=(7, 6), subplot_kw={"projection": "rectilinear"})
sizes = [total_social_media_users - converted_social_media_users, converted_social_media_users]
labels = ["Not Converted", "Converted"]
colors = ["lightcoral", "lightgreen"]

ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140, shadow=True, explode=[0.1, 0], wedgeprops={"edgecolor": "black"})
ax.set_title("Social Media Conversion (3D Styled Pie Chart)")
plt.show()

df.rename(columns={"Numer of Referrals": "Number of Referrals"}, inplace=True)
avg_referrals = df["Number of Referrals"].mean()
top_referrers = df[["Customer Name", "Number of Referrals"]].sort_values(by="Number of Referrals", ascending=False).head(5)

print(f"Average Referrals per User: {avg_referrals:.2f}")
print("Top 5 Referrers:\n", top_referrers)

plt.figure(figsize=(7, 5))
sns.histplot(df["Number of Referrals"], bins=10, kde=True, color="green")
plt.title("Distribution of Referrals per User")
plt.xlabel("Number of Referrals")
plt.ylabel("User Count")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

referral_counts = df["Referral Source"].value_counts()
print("\nReferral Source Breakdown:\n", referral_counts)

plt.figure(figsize=(7, 5))
sns.barplot(x=referral_counts.index, y=referral_counts.values, palette="coolwarm")
plt.title("Who Recommended the Car Wash?")
plt.xlabel("Referral Source")
plt.ylabel("Number of Customers")
plt.xticks(rotation=20)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
