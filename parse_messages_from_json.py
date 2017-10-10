'''
Clean message chains from all but text. Store the message chains with retirement-related words,
each to own file under two folders:
a. as they are;
b. without anything but words.
'''

import os
import json, pprint
import re
import glob


def main():
    path = '/Volumes/Transcend/Documents/GRADU/Tiedostot/test_json_files/'

    for file in glob.glob('{}*.json'.format(path)):
        file_of_json = json.load(open(file))

        # Go through the messages within the data. The first message in the conversation
        # has a special tagging, that is why they are separated here first too.
        messages_dict = { 'data':
                [

                ]
            }

        for json_data in file_of_json:
            message_chain = {'entry_message': [],
                            'comments': []}

            # Get the text after the 'body'-tag:
            entry_message = cleanhtml(json_data['body'])

            # If retirement-related word is in the message, store it to list in dictionary:
            if is_retirement_in(entry_message):
                message_chain['entry_message'].append(entry_message)

            # Then get the comments in the message chain and do the same:
            comments = json_data['comments']

            for c in comments:

                # Get the text after the 'body'-tag:
                comment_txt = cleanhtml(c['body'])

                if comment_txt in 'This message has been removed by admin.':
                    continue

                # If retirement-related word is in the message, store it to list in dictionary:
                if is_retirement_in(comment_txt):
                    message_chain['comments'].append(comment_txt)

            if message_chain['comments'] or message_chain['entry_message']:

                messages_dict['data'].append(message_chain)

        # In case something breaks, this should save the work done this far with the file:
        with open ('./valivaihe_1.json', 'w') as new_file:
            json.dump(messages_dict, new_file)

    # Store all the original message chains with a retirement-related word in separate files into a directory.
    # The messages in a chain are separated by 'end'.
    messages_as_list = dict_to_list(messages_dict)
    store_to_dir(messages_as_list, '/Volumes/Transcend/Documents/GRADU/Tiedostot/test_json_files/test_originals', ' end ')

    # Clean the message chains. Leave only words without capitals, punctuation or numbers.
    # The messages in the chain will no longer be separated.
    # Also, no message will appear twice in the data.
    no_doubles_list = rm_double_messages(messages_dict)
    nothing_but_words_list = remove_punctuation(no_doubles_list)
    store_to_dir(nothing_but_words_list, '/Volumes/Transcend/Documents/GRADU/Tiedostot/test_json_files/test_bows', ' ')
    
def is_retirement_in(message):
    retirement_related_words = 'eläke eläkke syytink syyting eläköi'.split()
    for word in retirement_related_words:
        if word in message.lower():
            return True
    return False

# Remove all the messages that are more than once in the message chain
# and return a the chains as a list:
def rm_double_messages(dict):

    # The list where all the message chains are added in and what will be returned:
    no_double_messages = []

    for item in dict.values():

        for message_chain in item:

            # The list where all the messages in the message chain are stored in:
            chain_list = []

            # Whatever the entry message is, if it exists, put it in the list as string:
            if message_chain['entry_message']: ## CHANGE!
                entry_message = message_chain['entry_message'][0]
                entry_message = entry_message.lower()
                chain_list.append(entry_message)

            # The comments have three options:
            for comment in message_chain['comments']:
                comment = comment.lower()

                # 1. If comment already in the list of messages, do nothing
                if comment in chain_list:
                    continue

                # Duplicate of the list messages in order to avoid eternal loop:
                previous_comments = chain_list[:]

                # 2. If part of the comment is already in any message in the list of messages,
                # store only the part of the comment that is not there yet:
                for previous_comment in previous_comments:
                    previous_comment = previous_comment.lower()
                    if previous_comment in comment:
                        comment_without_previous = comment.replace(previous_comment, "")
                        chain_list.append(comment_without_previous)
                        continue

                    # 3. Otherwise, add the comment to the list:
                    elif comment not in chain_list:
                        chain_list.append(comment)

            no_double_messages.append(chain_list)

    return no_double_messages

# Give a dictionary of message chains and get a list of them:
def dict_to_list(dict):
    messages_as_list = []

    for item in dict.values():

        for message_chain in item:
            chain_list = []
            if message_chain['entry_message']:
                chain_list.append(message_chain['entry_message'][0])

            for comment in message_chain['comments']:
                chain_list.append(comment)

            messages_as_list.append(chain_list)

    return messages_as_list

# Remove punctuation and numbers:
def remove_punctuation(list):
    cleaned_list = []
    for l in list:
        chain_list = []
        for word in l:
            w = re.compile('[^a-ö]|[|]')
            m = w.findall(word)
            if not m:
                chain_list.append(word)
            else:
                for i in re.split(w, word):
                    if i != '':
                        chain_list.append(i)

        cleaned_list.append(chain_list)
    return cleaned_list

# Store message chains, each to own file, under a directory:
def store_to_dir( list_to_store, path, in_between_words ):

    i = 1

    for message_chain in list_to_store:

        with open(os.path.join(path, "file%s.txt" % (i)), "w") as file:

            for word in message_chain:
                file.write( "%s%s" % (word, in_between_words))

        i += 1

# Return text after html-tags:
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

if __name__ == '__main__':
    main()
