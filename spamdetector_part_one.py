import csv

def read_data_from_file():
    global data
    data = []
    with open("spam.csv", encoding="latin-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip the first row
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data

def does_have_links(sms_message):
    # This function returns the string “TRUE” if a SMS message has links and
    # “FALSE” if a SMS message doesn’t have links
    domains_list = ["http", "www."]
    if any(domains in sms_message[1] for domains in domains_list):
        return "TRUE"
    else:
        return "FALSE"

def does_have_spammy_words(sms_message):
    # This function returns the string “TRUE” if the SMS contains spammy words and
    # “FALSE” if a SMS message does not have spammy words
    words_list = ['WINNER','URGENT', 'FreeMsg','Congrats!','free','FREE', 'winner','PRIVATE!', 'URGENT!','4U', 'Free trial']
    if any(words in sms_message[1] for words in words_list):
        return "TRUE"
    else:
        return "FALSE"

def length_of_text(sms_message):
    # This function returns the number of characters including spaces in the text message
    return int(len(sms_message[1]))

# Add Header
def write_header():
    header = ["LENGTH_OF_TEXT", "DOES_HAVE_SPAMMY_WORDS", "DOES_HAVE_LINKS", "CLASS_LABEL"]
    features = open("features.csv", 'a')
    writer = csv.DictWriter(features, fieldnames=header)
    writer.writeheader()
    features.close()

# write features to a file
def write_features_to_file(text_length, does_have_spammy_words, does_have_links, class_label):
    # writing to csv file
    row = [text_length, does_have_spammy_words, does_have_links, class_label]
    with open("features.csv", 'a', newline='', encoding='utf-8') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerow(row)

def main():
    # Read data from the csv file
    read_data_from_file()
    # Convert each SMS message into a set of features (does_have_links, does_have_spammy_words, length_of_text)
    for message in data:
        length_of_text(message)
        does_have_spammy_words(message)
        does_have_links(message)
    # Write these features to a file named features.csv using the write_features_to_filefunction
    for message in data:
        write_features_to_file(length_of_text(message), does_have_spammy_words(message), does_have_links(message), message[0])


main()