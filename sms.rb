system('clear')
require 'colorize'
puts '''


'''
b = 0
puts '------------------------------'.green.bold
puts '{{ Number--->[ali_max] SMS }}'.cyan.bold
puts '------------------------------'.green.bold
#puts "          faile list...?".blue
#faill = gets.chomp
puts "           sms list...?".blue
ssss = gets.chomp

begin
  f = File.open("max.txt")
  while line = f.gets
    #puts line
    sleep(4)


require 'nexmo'

client = Nexmo::Client.new(
  api_key: "ead2abaf",
  api_secret: "lArd8fWUjeeMtHsS"
)

#puts"""
# *********************
# ali____________max
#********************"""
#puts line
#num = gets.chomp.to_i
#begin
 # f = File.open 'ii.txt'
  #while line = f.gets
   # puts line
    #sleep(3)


client.sms.send(
 # from: "Nexmo",
  from: "max",
  to: line,
  text: ssss
)
puts'.......'.blue+'..........'.cyan+'..............'.blue
puts '           ali___max == SMS'
puts "number ------> ".cyan + "#{line}".green.bold
puts "loop   ------> ".cyan + "#{b} ".yellow.bold
puts "SMS    ------> ".cyan + "#{ssss}".green.bold
#puts('𝔸𝕋𝕋𝕔𝕜 '.magenta.bold + '  B͓̽y͓̽  '.blue.bold + 'A̳l̳i̳͓̽'.y>
puts'.......'.blue+'..........'.cyan+'..............'.blue
b += 1
  end
ensure
  f.close
end
sleep(1)
puts '           ali___max == call.'.red.bold
puts "number ------> ".cyan + "end".green.bold
puts "loop   ------> ".cyan + "#{b} ".yellow.bold
puts "SMS    ------> ".cyan + "#{ssss}".green.bold
