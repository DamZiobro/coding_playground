
list = [10,25,30]

#2x for each element of list
IO.inspect Enum.map(list, fn(x) -> 2*x end) 
IO.inspect Enum.map(list, &(2*&1))

#print list of odd numbers
IO.inspect Enum.filter(list, &(rem(&1,2) == 1))

#calculate sum of elems using Enum.reduce
IO.inspect Enum.reduce(list, 0, fn(x,sum) -> sum + x end )
IO.inspect Enum.reduce(list, 0, &+/2)

#calculate sum of elems using Enum.sumk
IO.inspect Enum.sum(list)

# pass function to Enum.reduce
defmodule NumSummer do

  def sum_nums(list) do
    Enum.reduce(list, 0, &add_num/2)
  end

  defp add_num(x, sum) when is_number(x), do: sum + x
  defp add_num(_, sum), do: sum
end

list2 = [10,15,:atom, 20, "test"]
IO.inspect NumSummer.sum_nums(list2)
