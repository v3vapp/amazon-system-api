# from checksheet import generate

# generate("sample/12345.txt")

from python.cs import AmazonCheckSheet

sheet = AmazonCheckSheet("static/unshipped.txt")
sheet.generate()