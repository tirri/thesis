# Investigate the different model's topics' top documents.

from gensim import corpora, models

def main():

    model_version = 200 

    #load the respective corpus, gensim-dictionary and lda-model:
    corpus = corpora.MmCorpus('/Users/tirri/LDA/%stopics.mm' % (model_version))
    dictionary = corpora.Dictionary.load('/Users/tirri/LDA/%stopics.dict' % (model_version))
    model = models.LdaModel.load('/Users/tirri/LDA/%stopics.model' % (model_version))

    topic_n = 151 # or another integer from 0 to 199

    documents_for_topic = get_documents_for_topic(topic_n, model, dictionary, corpus)
    most_probables = get_5_most_probable(documents_for_topic)
    print(most_probables)


def get_document(n_of_document):
    with open('/Users/tirri/LDA/bows/file%s.txt.lemma' % (n_of_document)) as file:
        text = file.readline()
        document = [word for word in text.split()]
    return document

def get_topics_for_document(document, dictionary, model):
    bow = dictionary.doc2bow(document)
    topics = model.get_document_topics(bow, minimum_probability = 0.24)
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

# Take only the 5 most probable documents
def get_5_most_probable(original_list):
    most_probables_list = []
    for document in (original_list):
        if len(most_probables_list) < 5:
            most_probables_list.append(document)
        else:
            most_probables_list = sorted(most_probables_list, key=lambda tup: tup[1])
            print(most_probables_list)
            if document[1] > most_probables_list[0][1]:
                most_probables_list[0] = document
    return most_probables_list

main()
