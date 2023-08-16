import csv

#read the spam csv file into a list
def read_data_from_file():
    global data
    data = []
    with open('spam.csv', 'r', encoding="latin-1") as csv_file:
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

def predict_spam(length_of_text, does_have_spammy_words, does_have_links):
    if length_of_text <= 99:
        if does_have_links == "TRUE":
            return "spam"
        else:
            return "ham"
    else:
        if does_have_spammy_words == "TRUE":
            if length_of_text > 164:
                if length_of_text <= 184:
                    return "spam"
                else:
                    return "ham"
            else:
                if length_of_text > 130:
                    return "spam"
                else:
                    if length_of_text > 124:
                        return "ham"
                    else:
                        if length_of_text > 105:
                            return "spam"
                        else:
                            if length_of_text <= 101:
                                return "spam"
                            else:
                                return "ham"
        else:
            if does_have_links == "TRUE":
                return "spam"
            else:
                if length_of_text > 164:
                    return "ham"
                else:
                    if length_of_text > 160:
                        return "spam"
                    else:
                        return "ham"

def main():
    read_data_from_file()
    for message in data:
        length_of_text(message)
        does_have_spammy_words(message)
        does_have_links(message)
    for message in data:
        print(predict_spam(length_of_text(message), does_have_spammy_words(message), does_have_links(message)))

main()