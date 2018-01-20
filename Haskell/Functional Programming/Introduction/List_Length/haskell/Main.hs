module Main where

arrLen :: [a] -> Int
arrLen arr = foldl (\x y -> succ x) 0 arr

main = do
    inputData <- getContents
    print $ arrLen (map read (words inputData) :: [Int])
