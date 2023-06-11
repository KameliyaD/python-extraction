import PyPDF2
import re

def word_page_count(file_name: str, search:str):
    #Assign a file
    doc = PyPDF2.PdfFileReader(file_name)

    print(type(doc))

    #Number of pages
    pages = doc.getNumPages()

    #List of tuples (all accurances, page number)
    list_pages = []

    for i in range(pages):
        current_page = doc.getPage(i)
        text = current_page.extractText()
        #print(text)
        if re.findall(search, text):
            count_page = len(re.findall(search, text))
            list_pages.append((count_page, i))

    #result
    print(list_pages)

    #Number of pages that contain search term at least once
    count = len(list_pages)

    #Total word count
    total = sum([tup[0] for tup in list_pages])

    return(total, count)

#Application
file_name = "foo.pdf"

#Search term
search = 'speed'

#Call the function
result = word_page_count(file_name, search)

print(f"The word '{search}' was found {result[0]} times on {result[1]} pages!")

#Refactoring (creating a function because of reusability)
