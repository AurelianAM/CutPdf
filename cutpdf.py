from PyPDF2 import PdfReader, PdfWriter
from sys import argv

def extractPages(inputFile, outputFile, firstPage, lastPage):
    with open(inputFile, 'rb') as infile:

        reader = PdfReader(infile)
        writer = PdfWriter()
        for i in range(firstPage, lastPage):
            writer.add_page(reader.pages[i])

        with open(outputFile, 'wb') as outfile:
            writer.write(outfile)

if __name__ == "__main__":
    inputFile = argv[1]

    try:
        if inputFile == '' or inputFile == '-?' or inputFile == '-h' or inputFile== '/h' or inputFile == '/?':
            print('Arguments: inputFile.pdf outputFile.pdf startPage endPage')
        else:
            outputFile = argv[2]
            firstPage = int(argv[3])
            lastPage = int(argv[4])
            extractPages(inputFile, outputFile, firstPage, lastPage)
    except:
        print('Something went wrong...')
