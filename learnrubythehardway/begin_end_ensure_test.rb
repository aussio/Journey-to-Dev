def foo_bar(error=false)
    name = "foo"
    puts name

    begin
        name = "bar"
        puts "within begin/end"
        puts name
    end

    puts "after begin/end"
    puts name

    if error
        raise StandardError
    end

    rescue
        puts "within rescue"
        puts name

    ensure
        puts "within ensure"
        puts name

    puts "at the end"
    puts name
end
       
error = ARGV.first || false

foo_bar(error)
