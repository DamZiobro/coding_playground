
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

MyLoop.print_multile_times("Text", 20)

a = 10
a = 20

IO.puts a
