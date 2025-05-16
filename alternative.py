word="Hello world"
#store final result in final_word
final_word=""

#Get length of the word
word_length=len(word)

#iterate over each character
for i in range(word_length):
    #calculate for even values
    if i % 2 ==0:
        #convert the character to uppercase 
        final_word +=word[i].upper()
        
    else:
        #convert the character to lowercase
        final_word+=word[i].lower()
       
print(final_word)

sent="I am learning to code"

#store final result in final_word
final_sent=""

#split the sentence into words
sent_w=sent.split()

#iterate over each word
for i in range(len(sent_w)):
    #calculate for even values
    if i % 2 ==0:
        #convert the word to uppercase 
        final_sent +=sent_w[i].upper()
        
    else:
        #convert the wordto lowercase
        final_sent+=sent_w[i].lower()
        
print(final_sent)
