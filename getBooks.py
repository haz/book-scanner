from BarcodeScanner import BarcodeScanner
from BookTool import BookTool
import os, tqdm

scanner = BarcodeScanner()
bt = BookTool()
images = os.listdir("images")
outFile = "books.csv"

# Loop through all the images in the images directory
for image in tqdm.tqdm(images):
    path = "images/" + image

    # Get the barcode (ISBN) of the image
    ISBN = scanner.getCode(path)

    if not ISBN:
        print("No barcode found in image: " + path)
        continue

    # Get the book
    book = bt.getBookInfo(ISBN)

    # If the book info was recovered correctly, write to file
    if book:
        bt.writeInfo(book, outFile, image)
    else:
        print("No book found with ISBN: " + ISBN)
