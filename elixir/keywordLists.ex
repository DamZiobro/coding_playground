
IO.puts("keyword list")
klist = [{:a, "test"}, {:b, "test2"}]
klist2 = [a: "test", b: "test2", b: "test3"]
IO.puts(klist == klist2);
IO.puts(klist[:b]);
IO.puts(Keyword.get_values(klist2, :b))
IO.puts("======================================================================")

IO.puts("keyword list - insert key")
klist = [{:a, "test"}, {:b, "test2"}]
klist = Keyword.put_new(klist, :d, 3)
IO.puts(Keyword.get(klist, :d))
IO.puts("======================================================================")

IO.puts("map - insert key")
map = %{ :a => "test", :b => "test2" }
map = Dict.put_new(map, :c, "test3")
IO.puts(map[:c])
IO.puts("======================================================================")

IO.puts("map - update key")
map = %{ :a => "test", :b => "test2" }
map = %{ map | :b => "test2_updated" }
IO.puts(map[:b])
IO.puts("======================================================================")

IO.puts("map - pattern matching")
map = %{ :a => "test", :b => "test2" }
%{:a => x} = map
IO.puts(x)
IO.puts("======================================================================")
