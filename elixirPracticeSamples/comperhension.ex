list = [5,10,15]
squareList = for x <- list, do: x*x

IO.inspect squareList

multiplicationTable = for x <- 1..10, y <- 1..10, do: {x, y, x*y}

IO.inspect multiplicationTable
