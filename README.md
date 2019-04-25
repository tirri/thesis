# thesis 

> The files in this directory were used in my master's thesis (link to thesis will be added after submission). The data used in the thesis are discussion forum posts (Aller Media 2014), available for non-commercial research purposes.

## Conduct of analysing the data
* Fetch the usage rights
* Download the zipped json files
* /LDA/Codes/parse_messages_from_json_final.py
* Transfer the files onto csc-server for lemmatization. Use the lemmatize.py (https://github.com/HIIT/digivaalit-2015/blob/master/topics/lemmatize.py) and finnish-process -module (Silfverberg, Miikka, Teemu Ruokolainen, Krister Lindén & Mikko Kurimo. 2015. FinnPos: an open-source morphological tagging and lemmatization toolkit for Finnish. Language Resources and Evaluation 50(4): 863–878.) on the retirement discussion files and on the stopwords.
* Transfer the files back to laptop
* /lda_with_gensim/messages_to_bows2.py
* /lda_with_gensim/lda_of_messages.py <-- edit correct number of words to print!!
* investigate the most probable documents for the topics with /lda_with_gensim/get_top_topics.py <-- clean this!
* investigate more words with /LDA/Codes/get_n_number_of_words_in_topic_x.py
* test coherence with LDA/Codes/coherence.py
* /LDA/Codes/find_messages_by_words.py

### References
Aller Media ltd. (2014). The Suomi 24 Corpus (2016H2) [text corpus]. Kielipankki. Retrieved from http://urn.fi/urn:nbn:fi:lb-2017021506
