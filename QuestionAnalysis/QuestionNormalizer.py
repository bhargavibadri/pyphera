import re
def normalize(question):
    '''Normalizes a question string by removing abundant whitespaces, replacing
       short forms and dropping filler words.'''
    question = re.sub(r'\s+',' ',strip(question))
    question = replace_short_forms(question)
    question = drop_fillers(question)
    return question

def replace_short_forms(question):
    '''Replace short forms of "is" and "are" that occur in combination with
    interrogatives'''
    is_pattern = re.compile("(how|what|which|when|where|who|why)('s)")
    are_pattern = re.compile("(how|what|which|when|where|who|why)('re)")
    is_match = is_pattern.search(question)
    are_match = are_pattern.search(question)
    if is_match:
        question = question.replace(m.group(), m.group(1)+' is')
    if are_match:
        question = question.replace(m.group(), m.group(1)+' are')
    return question

def drop_fillers(question):
    '''Drops filler words from question string'''
    fillers = re.compile("(approximate|approximately|one of|so-called) ")
    return fillers.sub("", question)
