from Secure_File_Uploader import Secure_File_Uploader_API
from Text_NLP_Analysis import Text_NLP_Analysis_API
from News_Feed_Ingester import News_Feed_Ingester_API
#import pytest


#===================Unit Tests for Uploader===================#
def test_upload_files():
    assert Secure_File_Uploader_API.upload_files(['pdf']) == "Uploading Successed!"
    assert Secure_File_Uploader_API.upload_files([]) == "Uploading Failed!"

def test_formats_judgement():
    assert Secure_File_Uploader_API.formats_judgement(["pdf", "words", "txt"]) == "Uploading Successed!"
    assert Secure_File_Uploader_API.formats_judgement(["pdf", ",mp3", "txt"]) =="Uploading Failed! Files are not fittable, please reupload!"

def test_input_keywords():
    assert Secure_File_Uploader_API.input_keywords(['Unit Tests']) == ['Unit Tests']
    assert Secure_File_Uploader_API.input_keywords(['A', '123']) == ['A', '123']
    assert Secure_File_Uploader_API.input_keywords([]) == "There is no keyword!"

def test_browse_uploaded_files():
    assert Secure_File_Uploader_API.browse_uploaded_files(['pdf', 'txt', 'words']) == ['pdf', 'txt', 'words']

#===================Unit Tests for Ingester===================#
def test_add_source2database():
    assert News_Feed_Ingester_API.add_newsfeed_source2database(["pdf", "words", "txt"]) == "Adding Successed!"
    assert News_Feed_Ingester_API.add_newsfeed_source2database([]) == "Adding Failed!"

def test_search_goalfiles():
    assert News_Feed_Ingester_API.search_goalfiles('keywords', 'sentiments', 0) == "Searching Successed!"
    assert News_Feed_Ingester_API.search_goalfiles('keywords', 'sentiments', 1) == "Searching Failed!"

def test_find_uesful_part():
    assert News_Feed_Ingester_API.find_uesful_part(["pdf", "words", "txt"]) == "EC500A2"
    assert News_Feed_Ingester_API.find_uesful_part([]) == "Finding Failed!"

def test_add_content2database():
    assert News_Feed_Ingester_API.add_content2database(["My name is Yuhang Li"]) == "Adding Contents Successed!"
    assert News_Feed_Ingester_API.add_content2database([]) == "Adding Contents Failed!"

def test_read_filesname_and_sources():
    assert News_Feed_Ingester_API.read_filesname_and_sources(["pdf", "words", "txt"]) == ['pdf', 'words', 'txt']
    assert News_Feed_Ingester_API.read_filesname_and_sources([]) == "There is no valid files!"

#===================Unit Tests for NLP===================#
def test_read_in():
    assert Text_NLP_Analysis_API.read_in(["pdf", "words", "txt"]) == ['pdf', 'words', 'txt']
    assert Text_NLP_Analysis_API.read_in([]) == "There is no valid files!"

def test_find_keywords():
    assert Text_NLP_Analysis_API.find_keywords(["pdf", "words", "txt"]) == ['pdf', 'words', 'txt']
    assert Text_NLP_Analysis_API.find_keywords([]) == "No Keywords!"

def test_find_sentiments():
    assert Text_NLP_Analysis_API.find_sentiments(1) == "Positive"
    assert Text_NLP_Analysis_API.find_sentiments(2) == "Negative"
    assert Text_NLP_Analysis_API.find_sentiments(3) == "Neutral"

def test_modify_sentiments():
    assert Text_NLP_Analysis_API.modify_sentiments(["pdf", "words", "txt"], "Positive", 1) == "Positive"
    assert Text_NLP_Analysis_API.modify_sentiments(["pdf", "words", "txt"], "Negative", 2) == "Negative"
    assert Text_NLP_Analysis_API.modify_sentiments(["pdf", "words", "txt"], "Neutral", 3) == "Neutral"

test_read_in()
test_find_keywords()
test_find_sentiments()
test_modify_sentiments()