'''
inputs: list of 15 or 20 or 30 words, data, how many of the words must
be in the message
outputs: list of messages id's

1. define requisites
2. get the messages
3. seek for messages that match the requisites
4. return a list
'''

from gensim import corpora

def main():
    model_version = 200
    data = corpora.MmCorpus('/Users/tirri/LDA/%stopics.mm' % (model_version))
    words_in_topic = 'pärjätä hankkia tehdä raha tarvita elää riittää käydä vaate kulku koto pari pitää kunto kämppä'.split()
    print(get_relevant_messages(data, words_in_topic))

def message_to_list_of_words(n_of_message):
    with open('/Users/tirri/LDA/bows/file%s.txt.lemma' % (n_of_message)) as file:
        text = file.readline()
        message = [word for word in text.split()]
    return message

def words_match_message(words_to_match, message):
    if len(set(words_to_match) & set(message)) > 11:
        print(set(words_to_match) & set(message))
        return True
    else:
        return False

def get_relevant_messages(data, words_to_match):
    relevant_messages = []
    for message_id in range(1, len(data)):
        message = message_to_list_of_words(message_id)
        if words_match_message(words_to_match, message):
            relevant_messages.append(message_id)
            print(relevant_messages)
    return relevant_messages

main()

