module Ex25

    # This function will break up words for us.
    def Ex25.break_words(stuff)
        words = stuff.split(' ')
        return words
    end

    # Sorts the words.
    def Ex25.sort_words(words)
        return words.sort
    end

    # Prints the first word after shifting it off
    def Ex25.print_first_word(words)
        word = words.shift
        puts word
    end

    # Prints the last word after popping it off
    def Ex25.print_last_word(words)
        word = words.pop
        puts word
    end

    # Prins the first and last words of the sentence.
    def Ex25.print_first_and_last(sentence)
        words = Ex25.break_words(sentence)
        Ex25.print_first_word(words)
        Ex25.print_last_word(words)
    end
end
