SPAM_TAG = 'SPAM'
HAM_TAG = 'OK'


def read_classification_from_file(filepath):
    dictionary = {}

    with open(filepath, 'r', encoding='utf-8') as file:
        file_content = file.read()
        classifications = file_content.split('\n')
        for c in classifications:
            words = c.split(' ')
            if len(words) > 1:
                dictionary[words[0]] = words[1]

    return dictionary
