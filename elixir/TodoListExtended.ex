defmodule TodoList do
  defstruct auto_id: 1, entries: Map.new

  def new, do: %TodoList{}
  
  def add_entry(%TodoList{entries: entries, auto_id: auto_id} = todo_list, entry) do
    entry = Map.put(entry, :id, auto_id)
    new_entries = Map.put(entries, auto_id, entry)

    %TodoList{todo_list | entries: new_entries, auto_id: auto_id + 1}
  end 

  def get_entries(%TodoList{entries: entries}, date) do 
    entries 
    |> Stream.filter(fn({_, entry}) -> entry.date == date end)
    |> Enum.map(fn({_, entry}) -> entry end)
  end

end

todo_list = 
  TodoList.new 
  |> TodoList.add_entry(%{date: {2017, 06, 07}, title: "Solve issue PROJ-123"})
  |> TodoList.add_entry(%{date: {2017, 06, 08}, title: "Solve issue PROJ-124"})
  |> TodoList.add_entry(%{date: {2017, 06, 08}, title: "Solve issue PROJ-125"})
  |> TodoList.add_entry(%{date: {2017, 06, 09}, title: "Birthday party"})
  |> TodoList.get_entries({2017,06,08})

IO.inspect todo_list
