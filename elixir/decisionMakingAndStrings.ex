IO.puts("check if string is empty")
a = ""
if String.length(a) === 0 do
  IO.puts("string a is empty");
end
IO.puts("======================================================================")

IO.puts("string interpolation")
a=2; 
b="value"; 
c="#{b}=#{a}"
IO.puts(c)
IO.puts("======================================================================")

IO.puts("string concatenation")
a="Hello" 
b="World" 
IO.puts(a <> " " <> b)
IO.puts("======================================================================")

IO.puts("check string length + int to string convertion")
a="Hello" 
IO.puts("length of string a="<> a <> " is: " <> Integer.to_string(String.length(a)))
IO.puts("======================================================================")

IO.puts("reversing string")
a="Hello" 
IO.puts("reverse of string a="<> a <> " is: " <> (String.reverse(a)))
IO.puts("======================================================================")

IO.puts("string matching")
a="Hello9" 
IO.puts(String.match?(a, ~r/ello/))
IO.puts(String.match?(a, ~r/lla/))
IO.puts("======================================================================")
