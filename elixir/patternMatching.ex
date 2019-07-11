# using pattern matching to match structure data 
[var_1, _ignore_var, var_2] = ["Test string 1", 20, "Test string 2"]

IO.puts(var_1)
#IO.puts(_ignore_var) #this will invoke warning as we try to use ignored variable (staring from underscore)
IO.puts(var_2)
# Output:
# "Test string 1"
# "Test string 2"
IO.puts("================================================================================")

#using pattern matching to unwrap structure
[_, [_, {a}]] = ["string", [:an_atom, {3}]]
IO.puts(a)
# Output: 
# 3
IO.puts("================================================================================")

#using left site pattern matching
a = 25
b = 25
IO.puts("Left hand site matching properly...")
^a = b
#IO.puts("Left hand site matching - it would be compilation error...")
#a = 15
#^a = b
