people = ["Damian", "Madzia", "Other"]

#format people using pipeline operator
people
  |> Enum.with_index 
  |> Enum.each(fn({person, number}) -> IO.puts("#{number+1}. #{person}") end)

#the above code iterate too much
#let's format people using streams
people
  |> Stream.with_index 
  |> Stream.each(fn({person, number}) -> IO.puts("#{number+1}. #{person}") end);

