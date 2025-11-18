import requests
from env import api_key
from textblob import TextBlob

# News API URL with Sanna Marin query
url = f"https://newsapi.org/v2/everything?q='Sanna Marin'&language=en&apiKey={api_key}"

# Make the request
response = requests.get(url)

# Check if the HTTP request was successful (status code 200 means OK)
if response.status_code == 200:

# Convert the API response from JSON format into a Python dictionary
    data = response.json()

    
 # Extract the 'title' from each article in the 'articles' list
# If 'articles' key doesn't exist, use an empty list as default
    titles = [article['title'] for article in data.get('articles', [])]
else:
    # If the request failed, print the error code and the response text
    print(f"Error: {response.status_code}, Response: {response.text}")
    
    # So by setting titles = [] (an empty list), we make sure the program doesn’t crash. 
    # Instead, it will just continue with an empty list, meaning no titles to analyze.
    titles = []

# Limit to first 50 titles
limited_titles = titles[:50]

# Sentiment analysis function
# Define a function to analyze sentiment of a given text
def analyze_sentiment(text):
# Create a TextBlob object from the text
    analysis = TextBlob(text)
    
 # Return the polarity score (a number between -1 and 1)
# -1 = very negative, 0 = neutral, +1 = very positive
    return analysis.sentiment.polarity

# Lists for categories
positive_titles = []
negative_titles = []
neutral_titles = []

# Analyze and categorize
for title in limited_titles:
    polarity = analyze_sentiment(title)
    if polarity > 0:
        positive_titles.append((title, polarity))
    elif polarity < 0:
        negative_titles.append((title, polarity))
    else:
        neutral_titles.append((title, polarity))

# Print results
print("\n--- Positive Titles ---")
for t, p in positive_titles:
    print(f"{t} | Polarity: {p}")

print("\n--- Negative Titles ---")
for t, p in negative_titles:
    print(f"{t} | Polarity: {p}")

print("\n--- Neutral Titles ---")
for t, p in neutral_titles:
    print(f"{t} | Polarity: {p}")

# Summary
print("\nSummary:")
print(f"Positive: {len(positive_titles)}")
print(f"Negative: {len(negative_titles)}")
print(f"Neutral: {len(neutral_titles)}")