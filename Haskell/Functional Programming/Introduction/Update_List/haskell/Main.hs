module Main where

-- Returns a list with the absolute values of all of its elements.
update :: Num a => [a] -> [a]
update arr = map abs arr

main :: IO()
main = do
    inputData <- getContents
    mapM_ print $ update $ map (read :: String -> Int) (words inputData)
