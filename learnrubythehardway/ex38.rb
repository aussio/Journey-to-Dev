def create_a_list_of_ten(list)
    return_list = []
    while return_list.length != 10
        item = list.pop
        return_list.push(item)
        puts "Adding #{item} to return_list."
    end
    
    return return_list
end

list = create_a_list_of_ten(ARGV)
puts "The final created list is: [#{list.join(', ')}]"
puts "The last item in the list is #{list[-1]} and its type is #{list[-1].class}."
