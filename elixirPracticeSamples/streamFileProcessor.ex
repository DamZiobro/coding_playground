#the output is the same, but the list iteration is done only once

defmodule FileProcessor do

  def large_lines!(path) do 
    File.stream!(path)    
      |> Enum.filter(&(String.length(&1)>50))
  end

  def lines_length!(path) do
    File.stream!(path)
      |> Enum.map(&(String.length(&1)))
  end

  def longest_line_length!(path) do
    File.stream!(path)
      |> Enum.reduce(0, &(max(&2, String.length(&1))))
  end

  def longest_line!(path) do
    File.stream!(path)
      |> Enum.reduce("", &longer_line/2)
  end

  defp longer_line(line1, line2) do
    if String.length(line1) > String.length(line2) do
      line1
    else
      line2
    end
  end

  def words_counts!(path) do
    File.stream!(path)
      |> Enum.map(&word_count/1)
  end
  
  defp word_count(path) do
    path 
      |> String.split(" ")
      |> length
  end

end

#print lines from current file which length is higher than 50 chars
IO.puts FileProcessor.large_lines!("./streamFileProcessor.ex")
IO.puts "=========================================================================================="
IO.inspect FileProcessor.lines_length!("./streamFileProcessor.ex")
IO.inspect FileProcessor.longest_line_length!("./streamFileProcessor.ex")
IO.inspect FileProcessor.longest_line!("./streamFileProcessor.ex")
IO.inspect FileProcessor.words_counts!("./streamFileProcessor.ex")



