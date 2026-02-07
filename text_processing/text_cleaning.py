import pandas as pd
import re
from collections import Counter

STOPWORDS = {
    "the", "and", "was", "is", "but", "very", "was", "to", "of"
}

# Load data
df = pd.read_csv("reviews.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = text.split()
    words = [w for w in words if w not in STOPWORDS]
    return words

all_words = []

for text in df["review_text"]:
    all_words.extend(clean_text(text))

word_counts = Counter(all_words)

# Convert to DataFrame
keywords_df = (
    pd.DataFrame(word_counts.items(), columns=["keyword", "frequency"])
    .sort_values("frequency", ascending=False)
)

keywords_df.to_csv("keywords.csv", index=False)

print("✅ Text processing completed. Keywords extracted.")