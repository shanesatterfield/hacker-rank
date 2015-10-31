module Main where

fib :: Int -> Int
fib n = fastFib n 1 0 0

fastFib :: Int -> Int -> Int -> Int -> Int
fastFib n i curr prev
    | i <= 1    = fastFib n (i+1) 0 0
    | i >  n    = curr
    | i == 2    = fastFib n (i+1) 1 0
    | otherwise = fastFib n (i+1) (curr + prev) (curr)

main = do
    n <- readLn :: IO Int
    print $ fib n
