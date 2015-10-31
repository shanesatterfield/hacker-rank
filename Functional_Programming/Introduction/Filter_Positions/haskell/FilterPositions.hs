module FilterPositions (filt) where

filt :: [Int] -> [Int]
filt arr = [arr !! x | x <- [1,3 .. (length arr)-1]]

main = do
   inputdata <- getContents
   mapM_ (putStrLn. show). filt. map read. lines $ inputdata
