defmodule TodoList do

  def new, do: Map.new
  
  def add_entry(todo_list, entry) do
    Map.update(todo_list, entry.date, [entry.title], fn(titles) -> [entry.title | titles] end)
  end 

  def entries(todo_list, date) do 
    Map.get(todo_list, date, [])
  end

end

todo_list = 
  TodoList.new 
  |> TodoList.add_entry(%{date: {2017, 06, 07}, title: "Solve issue PROJ-123"})
  |> TodoList.add_entry(%{date: {2017, 06, 08}, title: "Solve issue PROJ-124"})
  |> TodoList.add_entry(%{date: {2017, 06, 08}, title: "Solve issue PROJ-125"})
  |> TodoList.add_entry(%{date: {2017, 06, 09}, title: "Birthday party"})
  |> TodoList.entries({2017,06,08})

IO.inspect todo_list
