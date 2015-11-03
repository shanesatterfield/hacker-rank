module Main where

import Data.List

pascal :: Int -> [[Int]]
pascal n
    | k <= 0    = [[1]]
    | otherwise = (pascal (k)) ++ [[(fac (k)) `div` ((fac r) * fac(k-r)) | r <- [0..(k)]]]
    where k = n-1


fac :: Int -> Int
fac n = if n < 2 then 1 else n * fac (n-1)


main = do
    k <- readLn :: IO Int
    let result = map (map show) (pascal k)
    mapM_ putStrLn $ map (intercalate " ") result
