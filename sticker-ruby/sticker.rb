# Problem Statement:
#
# You have a sticker machine that can only print stickers with the word "wpengine". Write a function to calculate how many "wpengine" stickers would need to be printed to spell a given other word out of the letters on the sticker. For example, it would take 2 stickers to get the word "winning" from "wpengine" stickers (need 2 i's and 3 n's).
#

# Create a hash in the fashion of a Python Counter object
def make_counter(string)
    final_dict = {}
    string.split('').each do |letter|
        if final_dict[letter]
            final_dict[letter] += 1
        else
            final_dict[letter] = 1
        end
    end

    final_dict
end

def possible_anagram?(input_word, sticker_word)
    input_word.split('').each do |letter|
        unless sticker_word.include? letter
            return false
        end
    end
    return true
end

# Given two hashes with Numeric values for its keys,
# subtract the value of hash2 from hash1 for any keys they have in common
# Example:
#   hash1 = {'a' => 2, 'b' => 0, 'c' => 1}
#   hash2 = {'a' => 1, 'b' => 2}
#   hash_value_subtract(hash1, hash2)
#   
#   hash1
#   > {'a' => 1, 'b' => -2, 'c' => 1}
def hash_value_subtract(hash1, hash2)
    hash2.each do |key, value|
        if hash1.keys.include? key
            hash1[key] -= value
        end
    end

    hash1
end

def empty_of_letters?(counter)
    counter.each do |key, value|
        if value > 0
            return false
        end
    end
    return true
end

def number_of_stickers_required(input_word, sticker_word='wpengine')
    sticker_counter = make_counter(sticker_word)
    input_word_counter = make_counter(input_word)

    if !possible_anagram?(input_word, sticker_word)
        return -1
    end

    sticker_count = 0
    until empty_of_letters?(input_word_counter)
        sticker_count += 1
        input_word_counter = hash_value_subtract(input_word_counter, sticker_counter)
    end

    return sticker_count
end
