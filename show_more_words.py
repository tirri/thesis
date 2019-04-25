from gensim import corpora, models

def main():

    model_version = 200 # which version of the model are we investigating? 30, 100 or 200 topics?

    #load the respective corpus, gensim-dictionary and lda-model:
    # corpus = corpora.MmCorpus('/Users/tirri/LDA/%stopics.mm' % (model_version))
    # dictionary = corpora.Dictionary.load('/Users/tirri/LDA/%stopics.dict' % (model_version))
    model = models.LdaModel.load('/Users/tirri/LDA/%stopics.model' % (model_version))

    # path_to_originals = '/Users/tirri/LDA/bows4/'
    topic_n = 74 # which topic are we investigating?
    num_of_words = 100 # how many words do we want to see?
    words = (model.print_topic(topic_n, num_of_words))

    print(words)

main()