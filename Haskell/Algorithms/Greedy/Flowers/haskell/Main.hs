module Main where

import Data.List

flowers:: Int -> [Int] -> Int
flowers k prices = flowersRec k (reverse $ sort prices) 0

flowersRec :: Int -> [Int] -> Int -> Int
flowersRec k prices i
    | null prices = 0
    | otherwise = ((sum $ take k prices) * (succ i)) + (flowersRec k (drop k prices) (succ i))

main :: IO ()
main = do
    inputData <- getContents
    let [[_, k], prices] = map (\x -> map read x :: [Int]) $ map words $ lines inputData
    print $ flowers k prices
