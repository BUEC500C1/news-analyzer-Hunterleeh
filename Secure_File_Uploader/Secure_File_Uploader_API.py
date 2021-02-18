fittable_formats = ["pdf", "txt", "words"]

def upload_files(files):
    #the parameter files is a list of files
    if files == []:
        return "Uploading Failed!"
    else:
        return "Uploading Successed!"

def formats_judgement(files):
    #the parameter files is a list of files
    error_files = []
    for i in range(len(files)):
        if files[i] in fittable_formats:
            continue
        error_files.append(i+1)
    if error_files == []:
        return upload_files(files)
    else:
        return "Uploading Failed! Files are not fittable, please reupload!"

def input_keywords(keywords):
    if keywords == []:
        return "There is no keyword!"
    else:
        return keywords

def browse_uploaded_files(files):#The files should be read from database
    return files
    