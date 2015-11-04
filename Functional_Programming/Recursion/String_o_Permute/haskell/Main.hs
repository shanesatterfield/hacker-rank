module Main where

permutate :: String -> String
permutate "" = []
permutate text = (head $ tail text) : (head text) : (permutate $ tail $ tail text)

main = do
    -- Number of test cases.
    t <- readLn :: IO Int
    inputData <- getContents
    mapM_ putStrLn $ map permutate $ take t $ words inputData
