IO.puts("prints list 'a' as ASCII chars of relative codes")
a = [100, 101, 102, 103]
IO.puts(a)  
IO.puts("======================================================================")

IO.puts("list concatenation")
a = [100, 101, 102]
b = [102, 103, 104]
IO.puts(a ++ b);
IO.puts("======================================================================")

IO.puts("list subtraction")
a = [100, 102, 103]
b = [100, 103, 104]
IO.puts(a -- b);
IO.puts("======================================================================")

IO.puts("head and tail of list")
a = [100, 102, 103]
b = [100, 103, 104]
IO.puts(hd(a));
IO.puts(tl(b));
IO.puts("======================================================================")

IO.puts("tuple size")
tup = {:ok, "test"}
IO.puts(tuple_size(tup));
IO.puts("======================================================================")

IO.puts("tuple append value")
tup = {:ok, "test"}
Tuple.append(tup, "world")
IO.puts(tuple_size(tup));
IO.puts("======================================================================")
