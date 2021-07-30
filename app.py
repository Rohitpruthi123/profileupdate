# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:39:56 2021

@author: dodwadmathp
"""

#!/usr/bin/env python
# coding: utf-8

import re
import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import string
import os

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel



import matplotlib.pyplot as plt

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter


# In[4]:
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.util import ngrams

from nltk import word_tokenize,sent_tokenize

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import streamlit as st

from streamlit import components

#### Function definition for reading data ####
def read_data(w):
    
    dataread = pd.read_csv(w, encoding = 'unicode_escape')
    
    return dataread

#### Function definition for subsetting data #####
def subset_data(dataread, filterval,filtercol):
    
    datasub = dataread[dataread[filtercol].isin(filterval)]
    
    return datasub

#### function to clean data #####
def clean_data(dataset, column_name):
    
    text_data = dataset[column_name].str.cat()
    
    text_data = text_data.translate(str.maketrans('','',string.punctuation))
    
    text_data = re.sub("\n","", text_data)
       
    return text_data

#### stop words static def ######
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'nan'])

##### extract words #######
def extract_words(text, stopwords, min_length):
    words = nltk.word_tokenize(text)
    
    words = [w for w in words if w not in stopwords if len(w)> min_length]
      
    text = ' '.join(words)

    return text

##### create dictionary ######
def create_dict(text, n_gram):
    
    gram_list = list(nltk.ngrams(text.split(" "), n_gram))
       
    dictionary = [' '.join(tup) for tup in gram_list]
    
    vectorizer = CountVectorizer(ngram_range=(n_gram,n_gram))
    
    bag_of_words = vectorizer.fit_transform(dictionary)
    
    sum_words = bag_of_words.sum(axis=0) 
    
    words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    
    return dict(words_freq)

##### create word cloud ######
def create_wc(dictionary, maxwords):
    
    wc = WordCloud(background_color="white", 
                   colormap="hot", 
                   max_words=maxwords,
                   stopwords=stop_words)
    
    fig = plt.figure()
    wc.generate_from_frequencies(dictionary)
    # show the figure
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(fig)
    
###### send to words ########
def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
        
####### remove stopwords ########
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]

###### build topic model ########
def build_topic_model(dataset, column_name,ntopics):
    
    data = dataset[column_name].values.tolist()
    data_words = list(sent_to_words(data))
    # remove stop words
    data_words = remove_stopwords(data_words)
    
    import gensim.corpora as corpora
    # Create Dictionary
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    
    from pprint import pprint
    # number of topics
    num_topics = ntopics
    # Build LDA model
    
    lda_model = gensim.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)
    # Print the Keyword in the 10 topics
    pprint(lda_model.print_topics())
    doc_lda = lda_model[corpus]
     
    
       
    return lda_model


st.title("CSAT Analytics - Powered by R2DL")
st.subheader("Please use the side bar for analysis steps and main screen for outputs")


st.sidebar.title("Please start here with your analysis")

file_upload = st.sidebar.file_uploader("Please upload your file here, ensure all personal information has been removed")

if file_upload:
    
    raw_data = read_data(file_upload)
    
    st.write("1. The file you read is ", file_upload.name)
    
    st.write("2. This file has a total of ", raw_data.shape[0], "comments")
    
    st.write("3. The columns in the file are as below", raw_data.columns) 
    
    textcol = st.sidebar.selectbox("The column with text is", raw_data.columns)
    
    st.write("4. The column with text to be analysed is", textcol)
       
        
############################################################################################################   
    servicecol = st.sidebar.selectbox("The column with service area is", raw_data.columns)
    
    service_sel = st.sidebar.multiselect("Select the service area", (raw_data[servicecol].unique()))
  
    all_options = st.sidebar.checkbox("Select all services")
    

    if all_options:
        service_sel = raw_data[servicecol].unique() 
    
    else:
        service_sel = service_sel

    
        
    st.write("5. You have selected", service_sel, "service areas")
    
    subset_service = subset_data(raw_data,service_sel, 'Service Area')
    
    st.write("6. This file has a total of ", subset_service.shape[0], "comments")
        
############################################################################################################   
    satisfactioncol = st.sidebar.selectbox("The column with satisfaction level is", raw_data.columns)
    
    sat_sel = st.sidebar.multiselect("Select the satisfaction level of interest", (raw_data[satisfactioncol].unique()))
    
    all_options_sat = st.sidebar.checkbox("Select all satisfaction levels")
    

    if all_options_sat:
        sat_sel = raw_data[satisfactioncol].unique() 
    
    else:
        sat_sel = sat_sel

    
    
    st.write("7. You have selected", sat_sel, "satisfaction levels")
    
    subset_satisfaction = subset_data(subset_service,sat_sel, 'Satisfaction')
    
    st.write("8. This file has a total of ", subset_satisfaction.shape[0], "comments")

###############################################################################################################   
    countrycol = st.sidebar.selectbox("The column with country is", raw_data.columns)
    
    country_sel = st.sidebar.multiselect("Select the countries of interest", (raw_data[countrycol].unique()))
    
    all_options_country = st.sidebar.checkbox("Select all countries")
    

    if all_options_country:
        country_sel = raw_data[countrycol].unique() 
    
    else:
        country_sel = country_sel

    
    st.write("9. You have selected", country_sel, "countries")
    
    subset_country = subset_data(subset_satisfaction,country_sel,  'Country')
    
    st.write("10. This file has a total of ", subset_country.shape[0], "comments")

################################################################################################################
    
#     cleanup = st.sidebar.button('BUTTON - Click to Clean Data')
    
#     if cleanup:
               
#         text_clean = clean_data(subset_country, textcol)
        
#         st.write("11. Performing data cleaning, total number of clean text words", len(text_clean))

################################################################################################################
    
    small_word = st.sidebar.slider("Set a threshold for small words", min_value = 1, max_value = 6)
    
#     extractword = st.sidebar.button('BUTTON - Click to Extract Words')
    
#     if extractword:
        
#         text_clean = clean_data(subset_country, textcol)
        
#         st.write("11. Performing data cleaning, total number of clean text words", len(text_clean))

               
#         text_word = extract_words(text_clean, stop_words, small_word)
        
#         st.write("12. Extracting words, total number of extracted words", len(text_word))        

################################################################################################################
    
    n_gram = st.sidebar.slider("How many words to combine", min_value = 1, max_value = 4)

    
    wordcloud = st.sidebar.button('BUTTON - Click to create wordcloud')
    
    if wordcloud:
        
        text_clean = clean_data(subset_country, textcol)
        
        st.write("11. Performing data cleaning, total number of clean text words", len(text_clean))

               
        text_word = extract_words(text_clean, stop_words, small_word)
        
        st.write("12. Extracting words, total number of extracted words", len(text_word))        
        
        dictionary = create_dict(text_word, n_gram)
        
        create_wc(dictionary, 20)

################################################################################################################
    
    n_topics = st.sidebar.slider("How many topics do you want create", min_value = 2, max_value = 15)

    
    ldatopic = st.sidebar.button('BUTTON - Click to create topic model')
    
    if ldatopic:
        
        st.write("11. Building topic model with ", n_topics, "topics")
        
        lda_model = build_topic_model(subset_country, textcol, n_topics)
        
        topics = lda_model.print_topics()
        
        st.subheader('Topic Word-Weighted Summaries')
        
        for topic in topics:
            st.markdown(f'**Topic #{topic[0]}**: _{topic[1]}_')
            
         
        st.subheader('Top N Topic Keywords Wordclouds')
        
        topics = lda_model.show_topics(formatted=False, num_topics=n_topics)
        cols = st.beta_columns(2)

        for index, topic in enumerate(topics):
            wc = WordCloud(background_color="white", 
                   colormap="hot", 
                   max_words=20,
                   stopwords=stop_words)
            
            with cols[index % 2]:
                wc.generate_from_frequencies(dict(topic[1]))
                st.image(wc.to_image(), caption=f'Topic #{index}', use_column_width=True)
                
        #LDAvis_prepared = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
        
        #html_string = pyLDAvis.prepared_data_to_html(LDAvis_prepared)
               
        #components.v1.html("<html><body><h1>Topic Modeling Visualization</h1></body></html>", width=200, height=200)
        
        # st.markdown("<html><body><h1>Topic Modeling Visualization</h1></body></html>", unsafe_allow_html=True)
        
        # st.write(lda_model.print_topics())
        
#         vis = build_topic_model(subset_country, textcol, n_topics)
#         html_string = pyLDAvis.prepared_data_to_html(vis)
#         from streamlit import components
#         components.v1.html(html_string, width=1300, height=800)
    


# ### add text box for user entry
# ### extend storwords to include user entry
# user_text = st.sidebar.text_area("If you want to add stopwords, add here with no space, separated by comma")
# user_word_list = user_text.strip().split(",")

# stop_words.extend(user_word_list)

# st.write("The new added stop words are", user_word_list)


# In[234]:



# In[235]:
