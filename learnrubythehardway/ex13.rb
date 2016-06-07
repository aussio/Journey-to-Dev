first, second, third = ARGV
puts "Your first variable is: #{first}"
puts "Your second variable is: #{second}"
puts "Your third variable is: #{third}"

print "Can you give me another thing please? "
thing = $stdin.gets.chomp
puts "You gave me #{thing}."
