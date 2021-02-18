def read_in(contents):
    if contents == []:
        return "There is no valid files!"
    else:
        return contents

def find_keywords(contents):
    if contents == []:
        return "No Keywords!"
    else:
        return contents

def find_sentiments(contents):
    if contents == 1:
        return "Positive"
    elif contents == 2:
        return "Negative"
    else:
        return "Neutral"

def modify_sentiments(contents, sentiments, opinions):
    if opinions == 1:
        return "Positive"
    elif opinions == 2:
        return "Negative"
    else:
        return "Neutral"   