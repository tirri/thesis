'''
Modifies a folder '/Volumes/Macintosh HD/Users/tirri/lemmat/',
'/Volumes/Transcend/Documents/GRADU/Tiedostot/Koodit/test_folder_gensim/' ,
'/Volumes/Transcend/Documents/GRADU/Tiedostot/testilemmat/'
'/Volumes/Transcend/Documents/GRADU/Tiedostot/uudet_lemmat/'
containing txt files so that it is ready to be modelled.
no below = 20, no above = 0.33
'''
import glob
from natsort import natsorted
from gensim import corpora
from six import iteritems

def main():
    corpus_memory_friendly = MyCorpus()
    corpora.MmCorpus.serialize('/Users/tirri/LDA/200topics.mm', corpus_memory_friendly)

class MyCorpus(object):
    def __iter__(self):
        path = '/Users/tirri/LDA/indexed_lemmas/'
        dictionary = dictionary_of_words_in_texts(path)
        dictionary.compactify()
        dictionary.save('/Users/tirri/LDA/200topics.dict')
        for file in natsorted(glob.glob('{}*.lemma'.format(path))): #lemma tai txt
            with open(file) as text:
                for line in text:
                    yield dictionary.doc2bow(line.split()) #returns vectors one by one, thus memory friendly


def dictionary_of_words_in_texts(path):
    dictionary = corpora.Dictionary()
    for file in glob.glob('{}*.lemma'.format(path)): #lemma tai txt
        dictionary.add_documents(line.split(' ') for line in open(file))
    rm_unique_words(dictionary)
    rm_stopwords(dictionary)
    rm_common_words(dictionary)
    return dictionary

def rm_stopwords(dictionary):
    with open('/Volumes/Transcend/Documents/GRADU/Tiedostot/Koodit/testit/stopwords_fi.txt.lemma') as stop_file:
        temp = stop_file.read().splitlines()
        stopwords = [line for line in temp]
    stop_ids = [dictionary.token2id[stopword] for stopword in stopwords if stopword in dictionary.token2id]
    dictionary.filter_tokens(stop_ids)
    dictionary.compactify()
    return dictionary

def rm_unique_words(dictionary):
    once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]
    dictionary.filter_tokens(once_ids)
    dictionary.compactify()
    return dictionary

def rm_common_words(dictionary):
    # dictionary.filter_extremes(no_below=20, no_above=0.33, keep_n=None, keep_tokens=None)
    dictionary.filter_extremes(no_below=20, no_above=0.33, keep_n=None, keep_tokens=None)
    return dictionary

main()