number = "victim"
yehia = "https://download1645.mediafire.com/r4redkvs4mvg/8fcwtnrxus5hfrr/%D8%A8%D8%AF%D9%88%D9%86+%D8%B9%D9%86%D9%88%D8%A7%D9%86+8+640x360+%D9%A"
logo = "YEhia hacker"

	police = 'security'
	America = 'www.english.onion'
	Warning = 'Connect to Police Number Hide'
	Fbi = '001896'
class Bar   
  def do_things
    Foo.some_method(x) do |x|
      y = x.do_something
      return y_is_bad if y.bad? # how do i tell it to stop and return do_things? 
      y.do_something_else
    end
    keep_doing_more_things
  end
end

class Foo
  def self.some_method(targets, &block)
    targets.each do |target|
      begin
        r = yield(target)
      rescue 
        failed << target
      end
    end
  end
end

class Bar
  def self.do_things
      Foo.some_method(1..10) do |x|
            next if x == 2
            break if x == 9
            print "#{x} "
      end
  end
end

class Array
  def first_frog
    detect {|i| i =~ /frog/ }
  end

  def last_frog
    select {|i| i =~ /frog/ }.last
  end
end



require 'colorize'
system('clear')
puts '''


'''
puts '------------------------------'.green.bold
puts '{{ Number--->[ali_max] call }}'.cyan.bold
puts '------------------------------'.green.bold
#puts "          faile list...?".blue
#faill = gets.chomp
#puts "             saond...?".blue
b = 0
####
#while b == 0
begin

f = File.open("max.txt")

  while numbers = f.gets
#    puts numbers
nnumbers = numbers.to_i
sleep(1.1)
require 'nexmo'

client = Nexmo::Client.new(
  application_id: 'e3025a5b-7b24-4416-804b-c4b713651fb0',
  private_key: File.read('/data/data/com.termux/files/usr/libexec/1/max.key')
)




ncco =
[
  {


    "action": "stream",

    "streamUrl": [yehia]


  }
]








response = client.calls.create(
  to: [{
    type: 'phone',
    number: numbers.to_i
  }],
  from: {
    type: 'phone',
	

    number: '201000000000'
  },
  ncco: ncco
)
puts '''


'''
puts'.......'.blue+'..........'.cyan+'..............'.blue
puts '           ali___max == call'
puts "number ------> ".cyan + "#{numbers}".green.bold
puts "loop   ------> ".cyan + "#{b} ".yellow.bold
puts'.......'.blue+'..........'.cyan+'..............'.blue
b += 1
sleep(5)

end
ensure
  f.close
end
sleep(1)
puts '           ali___max == call.'.red.bold
puts "number ------> ".cyan + "end".green.bold
puts "loop   ------> ".cyan + "#{b} ".yellow.bold
