
def read_file(filepath):
    '''
    Docstring for read_file
    Reads the given file and returns line by line in the file in a list form
    :param filepath: Description
    '''
    with open(filepath, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def tokenize(sentence):
    '''
    Docstring for tokenize
    COnverts the ssentence into tokens by removing the white spaces 
    and returning them in form of list
    :param sentence: sentence in the form of a string(preferrable)
    '''
    return sentence.lower().strip().split()

def train_naive_bayes_classifier(positive_sentences, negative_sentences):
    '''
    Docstring for train_naive_bayes_classifier
    this calculates the prior probabilites of the model 
    :param positive_sentences: positive sentences data in form of list
    :param negative_sentences: negative sentences data in form of list
    '''
    #dictionaries for storing wordcounts in both pos and neg sentence dataset
    positive_word_counts={}
    negative_word_counts={}

    total_pos_words=0
    total_neg_words=0

    Vocabulary= set()

    for sentence in positive_sentences:
        #tokenize the sentence
        words= tokenize(sentence)
        for word in words:
            #adding the word to vocabulary
            Vocabulary.add(word)
            #if the word already exists in postivie word count dictionary we will add the count by 1
            # else we create a new key and increase count by 1
            positive_word_counts[word]= positive_word_counts.get(word,0)+1
            total_pos_words+= 1
    
    for sentence in negative_sentences:
        #tokenize the sentence
        words= tokenize(sentence)
        for word in words:
            #adding the word to vocabulary
            Vocabulary.add(word)
            #if the word already exists in negative word count dictionary we will add the count by 1
            # else we create a new key and increase count by 1
            negative_word_counts[word]= negative_word_counts.get(word,0)+1
            total_neg_words+= 1
    
    total_sentences= len(positive_sentences)+ len(negative_sentences)
    #calculate the prior probabilities aka prob(pos_sentence)/prob(total_sentences)..etc
    positive_prior= len(positive_sentences)/ total_sentences
    negative_prior= len(negative_sentences)/ total_sentences

    model = {
        "pos_counts": positive_word_counts,
        "neg_counts": negative_word_counts,
        "pos_total": total_pos_words,
        "neg_total": total_neg_words,
        "vocab_size": len(Vocabulary),
        "pos_prior": positive_prior,
        "neg_prior": negative_prior,
    }
    return model

def predict(sentence, model):
    '''
    Docstring for predict
    This func calculates the posterior prob and 
    classifies the sentence either as positive or negative
    :param sentence: new_sentence
    :param model: Description
    '''
    #tokenize the new sentence and then calculate the posteriors 
    words= tokenize(sentence)
    pos_score= model["pos_prior"]
    neg_score= model["neg_prior"]

    for word in words:
        pos_count= model["pos_counts"].get(word,0)
        neg_count= model["neg_counts"].get(word,0)

        #apply laplace smoothing
        pos_prob = (pos_count+1)/ (model["pos_total"]+ model["vocab_size"])
        neg_prob= (neg_count+1)/ (model["neg_total"]+ model["vocab_size"])

        # actually i thought of using log here but it isnt specified anywhere in assignment
        # so i refrain myself from doing it even though it is the best method
        pos_score*= pos_prob
        neg_score*= neg_prob
    
    if pos_score> neg_score:
        return "POSITIVE"
    else:
        return "NEGATIVE"

def train_validation_split(data, split_ratio=0.8):
    '''splits the data based on split ratio to train and validation sets'''
    n= int(len(data)* split_ratio)
    return data[:n], data[n:]

def evaluate_validation_data(model, pos_data, neg_data):
    '''
    Docstring for evaluate_validation_data
    THIS EVALUATE S THE VALIDATION SET AND RETURNS ACCURACY
    :param model: trained model
    :param pos_data: positive validation data
    :param neg_data: negative validation data
    '''
    correct=0
    total= len(pos_data)+len(neg_data)

    for sentence in pos_data:
        if predict(sentence,model) == "POSITIVE":
            correct +=1
    
    for sentence in neg_data:
        if predict(sentence,model) == "NEGATIVE":
            correct+=1
    
    return correct/total

def main():
    print("-----NAIVE BAYES CLASSIFIER-----")
    print(f"Make sure pos.txt and neg.txt files are avaialble in the directory")
    print(f"reading data.......")
    #read the pos.txt and neg.txt files and form the lists
    positive_sentences= read_file("pos.txt")
    negative_sentences= read_file("neg.txt")

    #splitting the data
    pos_train, pos_validation= train_validation_split(positive_sentences)
    neg_train, neg_validation= train_validation_split(negative_sentences)

    #train the classifier
    print(f"Training the classifier......")
    model= train_naive_bayes_classifier(pos_train,neg_train)
    print(f"Training Done!!")

    #evaluate the validation set
    print(f"Validation Accuracy: {evaluate_validation_data(model, pos_validation, neg_validation)}")
    print("Enter a sentence to classify.")
    user_input= input(">> ").strip()
    print(predict(user_input, model))

if __name__ =="__main__":
    main()