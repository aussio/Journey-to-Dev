filename = ARGV.first

if not filename
    puts "Provide a file to open please: "
    filename = $stdin.gets.chomp
end

text = open(filename)

puts "The contents of the #{filename} file are: "
print text.read
