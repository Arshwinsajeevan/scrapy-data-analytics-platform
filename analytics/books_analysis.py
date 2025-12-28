import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("../database/data.db")

# Load table into DataFrame
df = pd.read_sql_query("SELECT * FROM books", conn)

print("Total books:", len(df))

# ---------- CLEAN PRICE ----------
df["price_num"] = df["price"].str.replace("£", "").astype(float)

# ---------- SUMMARY STATS ----------
print("\nPrice Statistics:")
print(df["price_num"].describe())

# ---------- TOP 5 EXPENSIVE BOOKS ----------
top5 = df.sort_values(by="price_num", ascending=False).head(5)
top5.to_csv("../data/reports/top5_expensive_books.csv", index=False)
print("\nTop 5 Expensive Books saved.")

# ---------- AVERAGE PRICE BY RATING ----------
avg_price_by_rating = df.groupby("rating")["price_num"].mean()
avg_price_by_rating.to_csv("../data/reports/avg_price_by_rating.csv")
print("\nAverage Price by Rating saved.")


# ---------- RATING DISTRIBUTION ----------
rating_counts = df["rating"].value_counts()
print("\nRating Counts:")
print(rating_counts)

# ---------- AVAILABILITY ----------
availability = df["availability"].value_counts()
print("\nAvailability:")
print(availability)

# ---------- SAVE REPORT ----------
summary = {
    "total_books": len(df),
    "avg_price": df["price_num"].mean(),
    "max_price": df["price_num"].max(),
    "min_price": df["price_num"].min(),
    "most_common_rating": df["rating"].mode()[0],
}

report_df = pd.DataFrame([summary])
report_df.to_csv("../data/reports/books_summary.csv", index=False)

print("\nReport saved to data/reports/books_summary.csv")

conn.close()


#__PLOTTING__#
import matplotlib.pyplot as plt

# ---------- RATING DISTRIBUTION ----------
plt.figure(figsize=(6,4))
df["rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("../data/reports/book_rating_distribution.png")
plt.close()

# ---------- PRICE DISTRIBUTION ----------
plt.figure(figsize=(6,4))
df["price_num"].plot(kind="hist", bins=20)
plt.title("Book Price Distribution (£)")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../data/reports/book_price_distribution.png")
plt.close()
