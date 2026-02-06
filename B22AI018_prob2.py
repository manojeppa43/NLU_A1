##Byte Pair Encoding Tokenization
import sys
from collections import Counter, defaultdict

def read_corpus_file(filename):
    '''
    Docstring for read_corpus_file
    it returns a dictionary where key is space seperated characters of a word
    and values is the frequency of that word in corpus file
    :param filename: filelocation aka path
    '''
    vocabulary= defaultdict(int)

    with open(filename,'r', encoding='utf-8') as file:
        for line in file:
            #remove white spaces and select each word
            words= line.strip().split()
            for word in words:
                #converting the each word to characters 
                # and adding a EOW symbol(</w>) at the end
                chars= " ".join(list(word))+ " </w>"
                vocabulary[chars]+= 1
    
    return vocabulary

def calculate_pair_frequencies(vocabulary):
    '''
    Docstring for calculate_pair_frequencies
    this calculates the pair frequncies for all adjacent characters in vocabulary
    and returns it in the form of a dictionary
    :param vocabulary: vocab in form of dictionary
    '''
    pairs= Counter()
    for word, freq in vocabulary.items():
        #remove the word by spaces
        chars= word.split() 
        for i in range(len(chars)-1):
            pair= (chars[i],chars[i+1]) #considering adjacent chars as a pair
            pairs[pair]+= freq
        
    return pairs

def merge_pair(freq_pair, vocabulary):
    '''
    Docstring for merge_pair
    this merges a frequent character pair in the entite vocabulary
    :param freq_pair: pair of symbols to merge
    :param vocabulary: current vocabulary in the form of dictionary
    and returns updated vocabulary ater merging the new pair
    '''
    new_vocabulary= {}
    merged_char= "".join(freq_pair) #creating the merged char

    for word, freq in vocabulary.items():
        #split the word into chars
        chars= word.split()
        i=0
        new_chars=[]

        while i< len(chars):
            #checking if current char and next chat matches the pair
            if i< len(chars) -1 and chars[i]== freq_pair[0] and chars[i+1] == freq_pair[1]:
                #merge the pair
                new_chars.append(merged_char)
                i+= 2
            else:
                #keep as it is
                new_chars.append(chars[i])
                i +=1

            #new vocab with updated freq
        new_vocabulary[" ".join(new_chars)] = freq
    return new_vocabulary


def byte_pair_encoding(vocabulary, k):
    '''
    Docstring for byte_pair_encoding
     This is the byte pair encoding algorithm
    :param vocabulary: vocabulary in dictionary form
    :param k: No of merges
    '''
    for _ in range(k):
        # we need to calculate the pair frequencies
        pair_frequncies= calculate_pair_frequencies(vocabulary)
        #edge case if there were no pairs reamining
        if not pair_frequncies:
            break

        #we need to select the most frequent pair and merge it
        freq_pair= max(pair_frequncies, key=pair_frequncies.get)
        #merge this freq pair
        vocabulary= merge_pair(freq_pair, vocabulary)
    return vocabulary

def main():
    #check for valid arguments in CLI
    if len(sys.argv)!= 2:
        print("Usage: python B22AI018_prob2.py corpus.txt")
        sys.exit(1)

    filename= sys.argv[1]
    print(f"Number of Merge operations: ")
    k= int(input()) #taking input from user for no of merge ops

    #read the corpus and build the vocab(initial)
    vocabulary = read_corpus_file(filename)

    #run the byte pair encoding on this dictionary
    final_vocabulary= byte_pair_encoding(vocabulary, k)

    tokens= set()
    for word in final_vocabulary:
        for token in word.split():
            tokens.add(token)
    
    for token in sorted(tokens):
        print(token)

if __name__ == "__main__":
    main()