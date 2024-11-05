def rebuild_sentence(words, lengths):
    
    reconstructed_words = []
       
    for length in lengths:
        word = words.pop(0) # Take the first word from the list
        reconstructed_words.append(word[:length])  # Take the first 'length' characters of the word

    # Join the reconstructed words with a space and return
    return ' '.join(reconstructed_words)

print(rebuild_sentence(["the", "sky", "is", "blue"], [3, 2, 2, 1]))  
