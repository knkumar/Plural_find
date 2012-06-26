import nltk

class plural_Find:

    # set the hash and load download the corpus in case its not there
    # in: Object
    # open file "pcent_plurals.txt" for output
    def __init__(self):
        print("Please Install the brown-corpus and wordnet on your machine : ")
        nltk.download()
        self.pfile = open("pcent_plurals.txt","w")
        self.pfile.write("%s %s \n" % ("Plurals".ljust(20),"Percentages"))
        self.plural_dict = {}
        self.single_dict = {}

    # set the list of words to work on
    # in: Object
    def set_plist(self):
        self.p_list = nltk.corpus.brown.tagged_words()


    # insert into the plural dictionary
    # in: Object, item, tag
    def pl_insert_dict(self, item , tag):
        if item in self.plural_dict:
            stem = self.plural_dict[item][0]
            count = self.plural_dict[item][1]
            self.plural_dict[item] = [stem, count+1]
        else:
            self.plural_dict[item] = [nltk.stem.wordnet.WordNetLemmatizer().lemmatize(item.lower()), 1]

    # insert into the singular dictionary
    # in: Object, item, tag
    def sn_insert_dict(self, item , tag):
        stem = nltk.stem.wordnet.WordNetLemmatizer().lemmatize(item.lower())
        if stem in self.single_dict:
            self.single_dict[stem] = self.single_dict[stem]+1
        else:
            self.single_dict[stem] = 1

    # Function to check tags and insert into the plural or singular dictionary
    # in: Object, item, tag
    def check_tags(self, item, tag):
        if tag == "DTS" or tag == "NNS" or tag == "NNS$" or tag == "NPS" or tag == "NPS$" or tag == "PPLS":
            self.pl_insert_dict(item, tag)
        elif (tag == "ABL" or tag == "ABN" or tag == "ABX" or tag == "AP" or tag == "AT" or tag == "BE" 
        or tag == "BED" or tag == "BEDZ" or tag == "BEG" or tag == "BEM" or tag == "BEN" or tag == "BER" 
        or tag == "BEZ" or tag == "CC" or tag == "CD" or tag == "CS" or tag ==  "DO" or tag == "DOD" 
        or tag == "DOZ" or tag == "DT" or tag == "DTS" or tag == "DTX" or tag == "EX" or tag == "FW" 
        or tag == "HV" or tag == "HVD" or tag == "HVG" or tag == "HVN" or tag == "IN" or tag == "JJ"
        or tag == "JJR" or tag == "JJS" or tag == "JJT" or tag == "MD" or tag == "NC" or tag == "NN"
        or tag ==  "NN$" or tag == "NP" or tag == "NP$" or tag == "NR" or tag == "OD" or tag == "PN"
        or tag ==  "PN$" or tag == "PP$" or tag == "PP$$" or tag == "PPL" or tag == "PPO" or tag == "PPS"
        or tag ==  "PPSS" or tag == "QL" or tag == "QLP" or tag == "RB" or tag == "RBR" or tag == "RBT"
        or tag == "RN" or tag == "RP" or tag == "TO" or tag == "UH" or tag == "VB" or tag == "VBD" 
        or tag == "VBG" or tag == "VBN" or tag == "VBZ" or tag == "WDT" or tag == "WP$" or tag == "WPO"
        or tag == "WPS" or tag == "WQL" or tag == "WRB"):
            self.sn_insert_dict(item, tag)

    # The function to be called from outside
    # in: Object
    def check_plurals(self):
        map(lambda item: self.check_tags(item[0], item[1]), self.p_list)
        
    # The function computes the percentage and writes the output to the file
    # in: Object
    def compute_percentage(self):
        for key,value in self.plural_dict.items():
            if value[0] in self.single_dict:
                pcent = ( float(value[1]) / (value[1]+self.single_dict[value[0]]) ) * 100
                self.pfile.write("%s %s \n" % (key.ljust(20),pcent))

    def __del__(self):
        self.pfile.close()

def main():
    plurals = plural_Find()
    plurals.set_plist()
    plurals.check_plurals()
    plurals.compute_percentage()


if __name__ == "__main__":
    main()
