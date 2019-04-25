# thesis 

> The files in this directory were used in my master's thesis (link to thesis will be added after submission). The data used in the thesis are discussion forum posts (Aller Media 2014), available for non-commercial research purposes. The model used is gensim's (Rehurek & Sojka 2010) application of Latent dirichlet allocation topic model (Blei, Ng & Jordan 2003).

## Conduct of analysing the data
* Fetch the usage rights
* Download the zipped json files
* Find all retirement related convesations with parse_messages_from_json_final.py
* Transfer the files onto csc-server for lemmatization. Use the lemmatize.py (HIIT digivaalit 2015) and finnish-process -module (Silfverberg et al. 2015) on the retirement discussion files and on the stopwords.
* Transfer the files back to laptop
* Modify the conversations for modeling with messages_to_bows2.py
* Model the data into topics with Latent Dirichlet allocation lda_of_messages.py
* investigate the most probable documents for the topics with get_top_topics.py
* investigate more words with /LDA/Codes/get_n_number_of_words_in_topic_x.py
* test coherence with LDA/Codes/coherence.py
* /LDA/Codes/find_messages_by_words.py

### References
Aller Media ltd. (2014). The Suomi 24 Corpus (2016H2) [text corpus]. Kielipankki. Retrieved from http://urn.fi/urn:nbn:fi:lb-2017021506

Blei, David M., Andrew Y. Ng, Michael I. Jordan (2003). Latent dirichlet allocation. Journal of machine Learning research, 3(Jan), 993-1022.

HIIT digivaalit 2015: https://github.com/HIIT/digivaalit-2015/blob/master/topics/lemmatize.py

Rehurek, Radim, Sojka, Peter (2010) Software framework for topic modelling with large corpora. In LREC Workshop on New Challenges for NLP Frameworks, pages 45–50. In GitHub: https://github.com/RaRe-Technologies/gensim

Silfverberg, Miikka, Teemu Ruokolainen, Krister Lindén & Mikko Kurimo. 2015. FinnPos: an open-source morphological tagging and lemmatization toolkit for Finnish. Language Resources and Evaluation 50(4): 863–878.
