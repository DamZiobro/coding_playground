
IO.puts "Define for loop in elixir using recursion"

defmodule MyLoop do 
  def print_multile_times(msg, n) when n<=1 do 
    IO.puts(msg)
  end

  def print_multile_times(msg, n) do
    IO.puts(msg)
    print_multile_times(msg, n-1)
  end
end

IO.puts "=========================================================================================="
MyLoop.print_multile_times("Text", 20)

defmodule Numbers do
  def print(n) when n<1 do
    IO.puts n
  end

  def print(n) do
    IO.puts n
    print(n-1)
  end
end

Numbers.print(20)

a = 20

IO.puts "=========================================================================================="
IO.puts a

IO.puts "=========================================================================================="

defmodule ListCalculator do 
  def sum([]), do: 0
  def sum([head | tail]), do: head + sum(tail)

  #sum list with tail recursive
  def sum_tail_recursive(list), do: do_sum(0, list)
  defp do_sum(current_sum, []), do: current_sum
  defp do_sum(current_sum, [head | tail]) do 
    new_sum = head + current_sum
    do_sum(new_sum, tail)
  end


  #no-tail-recursive list_len
  def list_len([]), do: 0
  def list_len([head | tail]), do: list_len(tail) + 1

  #tail-recursive list_len
  def list_len_tail_recursive(list), do: do_len(0,list)
  defp do_len(len,[]), do: len
  defp do_len(len,[head | tail]) do 
    new_len = len + 1
    do_len(new_len, tail)
  end

  #no-tail-recursive-range
  def range(a,b) when a<b, do: range(a,b-1) ++ [b] 
  def range(a,b), do: [a]

  #tail-recursive-range
  def range_tail_recursive(a,b), do: do_range([a],a,b)
  defp do_range(list, a, b) when a<b do
    new_list = list ++ [a+1]
    do_range(new_list,a+1,b)
  end
  defp do_range(list, a, b), do: list

  #no-tail-positive
  def positive([]), do: []
  def positive([head | tail]) when head>0, do: [head] ++ positive(tail) 
  def positive([head | tail]), do: positive(tail)

  #tail-recursive-positive
  def positive_tail_recursive(list), do: do_positive([], list)
  defp do_positive(ret, []), do: ret
  defp do_positive(ret, [head | tail]) when head>0 do
    new_ret = ret ++ [head]
    do_positive(new_ret, tail)
  end
  defp do_positive(ret, [head | tail]), do: do_positive(ret, tail)
end

list = [1,2,3,4,5]
list2 = [1,-2,3,-4,5]

IO.puts ListCalculator.sum(list)
IO.puts ListCalculator.sum_tail_recursive(list)
IO.puts ListCalculator.list_len(list)
IO.puts ListCalculator.list_len_tail_recursive(list)
IO.inspect ListCalculator.range(2,5)
IO.inspect ListCalculator.range_tail_recursive(2,5)
IO.inspect ListCalculator.positive(list2)
IO.inspect ListCalculator.positive_tail_recursive(list2)

