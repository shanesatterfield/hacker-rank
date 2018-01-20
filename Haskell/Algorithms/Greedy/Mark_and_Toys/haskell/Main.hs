module Main where

import Data.List

maxToys k prices = maxToysRec k (sort prices) 0

maxToysRec k prices count
    | k < head prices = count
    | otherwise = maxToysRec (k - (head prices)) (tail prices) (count+1)

main = do
    inputData <- getContents
    let [[_,a], b] = map (\x -> map read x :: [Int]) $ map words $ lines inputData
    print $ maxToys a b
