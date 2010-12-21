from nltk import word_tokenize
import re

bad_keywords = re.compile("(give|tell|list)")
function_words = open('indices/functionwords_nonumbers').read().strip().split('\r\n')

def get_keywords(question):
    '''Extract keywords from a verb modified string'''
    tokens = [x for x in word_tokenize(question)]
    tokens = drop_single_chars(tokens)
    tokens = drop_bad_keywords(tokens)
    tokens = drop_function_words(tokens)
    return drop_duplicates(tokens)

def drop_single_chars(tokens):
    return filter(lambda x: len(x) > 1, tokens)
    
def drop_bad_keywords(tokens):
    return filter(lambda x: not bad_keywords.match(x), tokens)

def drop_function_words(tokens):
    return filter(lambda x: x not in function_words, tokens)

def drop_duplicates(tokens):
    unique = []
    for x in tokens:
        if x not in uniq:
            unique.append(x)
    return unique
