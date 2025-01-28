import isbnlib
import csv
import os

class BookTool:
    # Returns a book object with all the data recovered
    def getBookInfo(self, bookCode):

        for service in ['goob', 'openl', 'wiki']:
            try:
                book = isbnlib.meta(bookCode, service=service)
                if book:
                    break
            except:
                book = None

        # Add a description, if it's available and if the book was recovered
        if book:
            try:
                book['Description'] = isbnlib.desc(bookCode)
            except:
                book['Description'] = "N/A"

        return book

    # Writes the info of a book to a csv file
    def writeInfo(self, book, output, image):
        # Write header if it's the first time writing the file
        writeHeader = True if not os.path.exists(output) else False

        with open(output, "a") as outfile:
            # Init writer
            writer = csv.writer(outfile)

            # Write book info
            if writeHeader: writer.writerow(['Image', 'ISBN', 'Title', 'Author', 'Year', 'Description'])
            writer.writerow([image, book['ISBN-13'], book['Title'], book['Authors'][0], book['Year'], book['Description']])
