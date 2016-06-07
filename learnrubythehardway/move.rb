def move(from_file, to_file)
    from_contents = open(from_file).read
    #from_file.close

    puts "The input file #{from_file} is #{from_contents.length} bytes long."

    puts "Does the output file #{to_file} exist?: #{File.exist?(to_file)}"

    out_file = open(to_file, 'w')
    out_file.write(from_contents)
    out_file.close

    puts "Alrighty, all done!"

end

from_file, to_file = ARGV
move(from_file, to_file)
