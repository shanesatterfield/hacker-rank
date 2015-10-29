hello_worlds n = mapM_ putStrLn (take n (repeat "Hello World"))

main = do
    n <- readLn :: IO Int
    hello_worlds n
