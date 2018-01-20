module ReverseList (rev) where

rev :: (Ord a) => [a] -> [a]
rev []  = []
rev arr = (last arr) : (rev (init arr))

main :: IO ()
main = do
    inputData <- getContents
    mapM_ print $ rev (map read (words inputData) :: [Int])
