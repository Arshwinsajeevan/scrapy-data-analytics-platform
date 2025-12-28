import sqlite3
import pandas as pd
from collections import Counter

# Connect
conn = sqlite3.connect("../database/data.db")

# Load table
df = pd.read_sql_query("SELECT * FROM quotes", conn)

print("Total quotes:", len(df))

# ---------- TOP AUTHORS ----------
top_authors = df["author"].value_counts().head(5)
print("\nTop Authors:")
print(top_authors)

# ---------- TAG FREQUENCY ----------
all_tags = []

for t in df["tags"]:
    if t:
        all_tags.extend(t.split(","))

tag_counts = Counter(all_tags).most_common(10)

print("\nTop Tags:")
for tag, count in tag_counts:
    print(tag, ":", count)
 
 #--------- LONGEST QUOTES ----------   
df["length"] = df["quote"].str.len()
longest = df.sort_values(by="length", ascending=False).head(5)
longest.to_csv("../data/reports/longest_quotes.csv", index=False)
print("\nLongest quotes saved.")

# ----------Author Productivity----------
author_counts = df["author"].value_counts()
author_counts.to_csv("../data/reports/author_quote_counts.csv")
print("\nAuthor quote counts saved.")



# ---------- SAVE REPORT ----------
report = pd.DataFrame(tag_counts, columns=["tag", "count"])
report.to_csv("../data/reports/top_tags.csv", index=False)

print("\nTag report saved to data/reports/top_tags.csv")

conn.close()


import matplotlib.pyplot as plt

# Convert to DataFrame for plotting
author_df = top_authors.reset_index()
author_df.columns = ["author", "count"]

plt.figure(figsize=(6,4))
author_df.plot(kind="bar", x="author", y="count", legend=False)
plt.title("Top 5 Most Quoted Authors")
plt.xlabel("Author")
plt.ylabel("Quote Count")
plt.tight_layout()
plt.savefig("../data/reports/top_authors.png")
plt.close()
