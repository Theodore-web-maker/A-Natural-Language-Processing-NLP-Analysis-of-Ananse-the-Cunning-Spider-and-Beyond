import nltk
from nltk.tokenize import word_tokenize, sent_tokenize  
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt 
import re
from matplotlib import style
style.use('fivethirtyeight')
nltk.download('stopwords')
#nltk.download('punkt')     
#load the text corpus
with open('Afro_folktale_legends.txt', 'r', encoding = 'utf-8') as file:
    text = file.read()

# Tokenize the text into words and sentences
words = word_tokenize(text)
sentences = sent_tokenize(text)

# Remove punctuation from the text
stopwords = set(stopwords.words('english')) 
filtered_words = [word for word in words if word.lower() not in stopwords]
 #remove punctuation

# Perform stemming using NLTK's WordNetLemmatizer
nltk.download('wordnet')    
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]  

remove_special_characters = re.compile(r'[^a-zA-Z0-9\s]') #remove special characters
#remove special characters from the lemmatized words    
lemmatized_words = [remove_special_characters.sub('', word) for word in lemmatized_words]
#remove empty strings from the lemmatized words 
lemmatized_words = [word for word in lemmatized_words if word] #remove empty strings


cleaned_words_1 = [words.strip('.,!:;\'"\'"/ ') for words in lemmatized_words] #ensure that the words are stripped of punctuation and whitespace
#save the cleaned words to a text file      
with open('cleaned_words_3.txt', 'w',encoding = 'utf-8') as file:
        print(cleaned_words_1, file=file)
    

# Count the frequency of each word
word_counts = Counter(cleaned_words_1)

# Print the most common words and their frequencies
print("Most common words:")      
print("Total words:", len(words))
print("Total sentences:", len(sentences))
for word, count in word_counts.most_common(20):
    print(f"{word}: {count}")

#Word cloud visualization
# Create a word cloud from the word frequencies 
from wordcloud import WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='black', max_words = None).generate_from_frequencies(word_counts)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.imsave('wordcloud.jpeg', wordcloud, format='png')
plt.axis('off')
plt.show() # Display the word cloud
             

