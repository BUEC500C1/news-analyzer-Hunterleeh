def search_goalfiles(keywords, sentiments, test_flag):
    #The test_flag is only useful in the first phase
    if test_flag == 0:
        return "Searching Successed!"
    else:
        return "Searching Failed!"

def add_newsfeed_source2database(source):
    if source == []:
        return "Adding Failed!"
    else:
        return "Adding Successed!"

def find_uesful_part(files):
    interests = "EC500A2"
    if files == []:
        return "Finding Failed!"
    else:
        return interests

def add_content2database(contents):
    if contents == []:
        return "Adding Contents Failed!"
    else:
        return "Adding Contents Successed!"

def read_filesname_and_sources(database):
    #The parameter database is only useful in the first phase
    if database == []:
        return "There is no valid files!"
    else:
        return database