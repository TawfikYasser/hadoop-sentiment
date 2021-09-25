# This file to parse data from Amazon_Data_Modified then applying Sentiment Analysis.

# Reading Amazon_Data_Modified.csv

import csv

# Data Structures
product_id = []
product_name = []
product_asin = []
product_review_date = []
product_review_rate = []
product_review_text = []
product_review_title = []

with open('Amazon_Data_Modified.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'Product_ID {row[0]} - Product_Name {row[1]} - Product_ASIN {row[2]}.')
            product_id.append(row[0])
            product_name.append(row[1])
            product_asin.append(row[2])
            product_review_date.append(row[3])
            product_review_rate.append(row[4])
            product_review_text.append(row[5])
            product_review_title.append(row[6])
            line_count += 1
    print(f'Processed {line_count} lines.')

# for i in range(len(product_id)):
#     print("="*100)
#     print(f"Product ID: {product_id[i]} - Product Name: {product_name[i]} - Product ASIN: {product_asin[i]} ")
#     print("*"*100)
#     print(f"Review Title: {product_review_title[i]} - Review Text: {product_review_text[i]} - Review Rate: {product_review_rate[i]} - Review Date: {product_review_date[i]}")
#     print("="*100)


# Applying Sentiment Analysis

from textblob import TextBlob

# tb = TextBlob("I hate and do not like python")

# print(tb.sentiment)

# Writing the main data file 'bucket_hs'


hsb = open('bucket_hs.txt','a')
for i in range(5000):
    sentiment_p = TextBlob(product_review_title[i]+product_review_text[i])

    if sentiment_p.sentiment.polarity > 0.1:
        
        hsb.write(
        product_review_date[i][:10]+"^"+product_review_rate[i]+"^"+"+"+
        str(float("{:.2f}".format(float(sentiment_p.sentiment.polarity)*100)))+"%"+"^"+
        str(float("{:.2f}".format(float(sentiment_p.sentiment.subjectivity)*100)))+"%"+"^"+
        product_id[i]+"^"+product_asin[i]+"^"+product_name[i]+"^"+
        product_review_title[i]+"^"+product_review_text[i]+"^"+"POSITIVE_REVIEW"+"\n"
        )

    else:

        hsb.write(

        product_review_date[i][:10]+"^"+product_review_rate[i]+"^"+
        str(float("{:.2f}".format(float(sentiment_p.sentiment.polarity)*100)))+"%"+"^"+
        str(float("{:.2f}".format(float(sentiment_p.sentiment.subjectivity)*100)))+"%"+"^"+
        product_id[i]+"^"+product_asin[i]+"^"+product_name[i]+"^"+
        product_review_title[i]+"^"+product_review_text[i]+"^"+"NEGATIVE_REVIEW"+"\n"
        )

print("DONE")