'''
I have the original documents in a directory, with the same indexing as the Mm-corpus.
I also have the models for 30, 100 and 200 topics. Now I want to get from the individual topics
to the documents that have the highest probabilities to belong to the topic.

Apparently, ths works but test when you have the models ready.
'''

from gensim import corpora, models

def main():

    model_version = 200 # which version of the model are we investigating? 30, 100 or 200 topics?

    #load the respecting corpus, gensim-dictionary and lda-model:
    corpus = corpora.MmCorpus('/Users/tirri/LDA/%stopics.mm' % (model_version))
    dictionary = corpora.Dictionary.load('/Users/tirri/LDA/%stopics.dict' % (model_version))
    model = models.LdaModel.load('/Users/tirri/LDA/%stopics.model' % (model_version))

    # path_to_originals = '/Users/tirri/LDA/bows4/'
    topic_n = 3 # which topic are we investigating?

    documents_for_topic = get_documents_for_topic(topic_n, model, dictionary, corpus)
    print(documents_for_topic)


def get_document(n_of_document):
    with open('/Users/tirri/LDA/bows/file%s.txt.lemma' % (n_of_document)) as file:
        text = file.readline()
        document = [word for word in text.split()]
    return document

def get_topics_for_document(document, dictionary, model):
    bow = dictionary.doc2bow(document)
    topics = model.get_document_topics(bow, minimum_probability = 0.25)
    return topics

def get_documents_for_topic(topic_n, model, dictionary, document_matrix):
    documents_for_topic = []  # a list of doc_id, topic_probability -tuples
    for doc_id in range(1, len(document_matrix)):
        document = get_document(doc_id)
        topics_for_document = get_topics_for_document(document, dictionary, model)

        for topic in topics_for_document:
            if topic[0] == topic_n:
                tuple = (doc_id, topic[1])
                documents_for_topic.append(tuple)
                # print(documents_for_topic)

    return documents_for_topic

main()
