'''
This script uses the model of 200 topics to find messages behind topics. The criteria is, the message must be at least
0.5 % of the topic and include at least 5 of the 15 most common words in it. The length of the message is also limited
to no more than 300 words.
'''

from gensim import corpora, models
import random
import re




topic_74 = '0.252*"nuori" + 0.100*"vanha" + 0.053*"porukka" + 0.027*"eläkeläinen" + 0.025*"pitää" + 0.019*"päästä" + 0.018*"tehdä" + 0.016*"ryppy" + 0.015*"jäädä" + 0.015*"juosta" + 0.014*"työ" + 0.014*"pelastua" + 0.013*"parasta" + 0.012*"alkaa" + 0.011*"taitaa"'

topic_122 = '0.108*"vuotias" + 0.097*"eläkeikä" + 0.038*"täyttää" + 0.036*"nostaa" + 0.033*"päästä" + 0.032*"ikä" + 0.029*"jäädä" + 0.027*"työ" + 0.025*"ansiosidonnainen" + 0.023*"päiväraha" + 0.020*"iätä" + 0.016*"työelämä" + 0.015*"eläke#putki" + 0.015*"pitää" + 0.014*"syntyä"'


def main():

    model_version = 200

    data = corpora.MmCorpus('/Users/tirri/LDA/%stopics.mm' % (model_version))
    dictionary = corpora.Dictionary.load('/Users/tirri/LDA/%stopics.dict' % (model_version))
    model = models.LdaModel.load('/Users/tirri/LDA/%stopics.model' % (model_version))

    all_relevant_messages_in_all_topics = []
    sample_of_relevant_messages_in_all_topics = []

    topics = {
                 74 : topic_74,
                 122 : topic_122
    }


    for i in list(topics.keys()):
        words_in_topic = do_the_regex(topics[i]) # a list of words
        print('Defining the documents for the topic number : %s' % i)
        messages_for_topic = get_messages_for_topic(i, model, dictionary, data) # a list of message ids
        print(words_in_topic)
        all_relevant_messages = get_relevant_messages(messages_for_topic, words_in_topic) # a list of message ids
        print(all_relevant_messages)
        all_relevant_messages_in_all_topics.append('The topic number %s has the messages number %s before the sampling.' % (i, all_relevant_messages))
        randomly_selected_relevant_messages = random_sample_of_message_ids(all_relevant_messages) # an integer
        sample_of_relevant_messages_in_all_topics.append('Topic number: %s ' % i)
        sample_of_relevant_messages_in_all_topics.append(' and its messages: %s' % randomly_selected_relevant_messages)
        print('At the end of for loop; found the message number %s for the topic.' % randomly_selected_relevant_messages)
    print(all_relevant_messages_in_all_topics)
    print('Here is the list of the selected messages in order of the topic dict: %s ' % sample_of_relevant_messages_in_all_topics)
    
    
# Cleans the words in topic from anything but the word itself, returns a list of words
def do_the_regex(topic_words):
    regex = r'\"\w{1,}\"'
    words_in_hips = re.findall(regex, topic_words)
    only_words = [word.replace('"', '') for word in words_in_hips]
    return only_words


# Retrieve a message by its index. Return it as list of words.
def message_to_list_of_words(n_of_message):
    with open('/Users/tirri/LDA/bows/file%s.txt.lemma' % (n_of_message)) as file:
        text = file.readline()
        message = [word for word in text.split()]
    return message


# Change the message into a bag of words, get the topics for it, return list of topic ids.
def get_topics_for_message(message, dictionary, model):
    bow = dictionary.doc2bow(message)
    topics = model.get_document_topics(bow, minimum_probability=0.05)
    return topics


# Return a list of message ids in which the topic is relevant.
def get_messages_for_topic(topic_n, model, dictionary, message_matrix):
    messages_for_topic = []  # a list of message_id, topic_probability -tuples
    for message_id in range(1, len(message_matrix)):
        message = message_to_list_of_words(message_id)
        topics_for_message = get_topics_for_message(message, dictionary, model)

        for top in topics_for_message:
            if top[0] == topic_n:
                message_with_topic_prob = (message_id, top[1])
                messages_for_topic.append(message_with_topic_prob)

    return messages_for_topic


# Are there more than 4 same words in the message and topic's 15? Returns boolean.
def words_match_message(words_to_match, message):
    if len(message) < 301:
        if len(set(words_to_match) & set(message)) > 4:
            print('a match: %s' % message)
            return True
    else:
        print('no match: %s' % message)
        return False


# Get all the messages that match the criteria of <300, >4/15. Returns a list.
def get_relevant_messages(selected_messages, words_to_match):
    relevant_messages = []
    for message_id in range(1, len(selected_messages)):
        message = message_to_list_of_words(message_id)
        if words_match_message(words_to_match, message):
            relevant_messages.append(message_id)
    return relevant_messages


# Take a random sample of 14 message id's from the relevant_messages. Returns a list.
def random_sample_of_message_ids(ids):
    try:
        random_items = random.sample(ids, 14)
    except:
        print('sry, no required amount found. try another number!')
        random_items = ['none']
    return random_items


main()



