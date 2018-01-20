add a b = a + b

main = do
    a <- readLn
    b <- readLn
    let result = add a b
    print result
