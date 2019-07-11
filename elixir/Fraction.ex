defmodule Fraction do 
  defstruct a: nil, b: nil  
  
  def new(a,b), do: %Fraction{a: a, b: b}

  def value(fraction), do: fraction.a/fraction.b

  def add(f1, f2) do
    new(f1.a*f2.b+f2.a*f1.b, f1.b*f2.b)
  end
end

Fraction.add(%{a: 1, b: 3}, %{a: 1, b: 6}) 
|> Fraction.value
|> IO.puts
