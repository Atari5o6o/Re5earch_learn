#code to find keywords in a scientific paper
from extract_pdf import all_text
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

def extract_keywords_with_preference(text, title, abstract):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Initialize an empty dictionary to store keywords and their scores
    keywords = {}

    # Define the set of allowed POS tags (specific to your needs)
    allowed_pos = ['NN', 'NNS']  # Example: Common nouns only

    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Process each sentence
    for sentence in sentences:
        # Tokenize the sentence into words
        words = word_tokenize(sentence)

        # Perform POS tagging and lemmatization on the words
        pos_tags = nltk.pos_tag(words)
        lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word, pos in pos_tags]

        # Filter out stopwords, words that are not nouns, and apply additional filtering criteria
        filtered_words = [word for word, pos in pos_tags if word.lower() not in stopwords.words('english')
                          and pos in allowed_pos
                          and len(word) > 2]  # Example: Exclude words with less than 3 characters

        # Assign scores to the filtered words based on their presence in title and abstract
        for word in filtered_words:
            score = 1  # Default score
            if word in title.lower():
                score += 1  # Increase score if word appears in the title
            if word in abstract.lower():
                score += 1  # Increase score if word appears in the abstract

            # Update the keyword dictionary with the word and its score
            if word in keywords:
                keywords[word] += score
            else:
                keywords[word] = score

    return keywords

paper_title = input("Enter the title of the paper")
paper_abstract = input("Enter the abstract")

# Extract keywords with preference to words in the title and abstract
keywords_with_preference = extract_keywords_with_preference(all_text, paper_title, paper_abstract)

# Sort the keywords by their scores in descending order
sorted_keywords = sorted(keywords_with_preference.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 keywords with their scores
print("Keywords with Preference (Top 10):")
for keyword, score in sorted_keywords[:10]:
    print(keyword, ":", score)

