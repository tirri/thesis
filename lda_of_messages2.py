import numpy
from gensim import corpora, models
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

def main():
    model = get_model()
    topics = (model.print_topics(200, 10))
    with open('200topics.txt', 'w') as file:
        file.write(str(topics))


def get_corpus():
    corpus = corpora.MmCorpus('/Users/tirri/LDA/200topics.mm')
    return corpus

def get_dictionary():
    dictionary = corpora.Dictionary.load('/Users/tirri/LDA/200topics.dict')
    return dictionary

def get_model():
    corpus = get_corpus()
    print(str(corpus))
    dictionary = get_dictionary()
    print(dictionary)
    model = models.LdaModel(corpus, id2word=dictionary, num_topics=200, minimum_probability=0.01, alpha='auto', eta='auto', iterations = 1000, eval_every=10,
                            random_state=numpy.random.RandomState(10))
    model.save('/Users/tirri/LDA/200topics.model')
    return model

main()
