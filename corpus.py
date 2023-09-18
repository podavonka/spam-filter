import os


class Corpus:

    def __init__(self, path_to_emails):
        self.path = path_to_emails

    def emails(self):
        filenames = os.listdir(self.path)
        for filename in filenames:
            if filename[0] == '!':
                continue
            with open(self.path + '/' + filename, 'r', encoding='utf-8') as file:
                email_body = file.read()
                yield filename, email_body

# if __name__ == '__main__':
#     # Create corpus from a directory
#     corpus = Corpus ('/path/to/directory/with/emails')
#     count = 0
#     # Go through all emails and print the filename and the message body
#     for fname, body in corpus.emails ():
#         print (fname)
#         print (body.encode())
#         print ('-------------------------')
#         count += 1
#     print ('Finished: ', count, 'files processed.')
