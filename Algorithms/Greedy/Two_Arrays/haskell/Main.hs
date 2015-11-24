module Main where

import Data.List

tarrs :: Int -> [Int] -> [Int] -> Bool
tarrs k a b = tarrsRec k (sort a) (reverse $ sort b)

tarrsRec :: Int -> [Int] -> [Int] -> Bool
tarrsRec k a b
    | null a = True
    | ((head a) + (head b)) >= k = tarrsRec k (tail a) (tail b)
    | otherwise = False

processInput :: Int -> [[Int]] -> [Bool]
processInput n inputData
    | n >= 1 = (tarrs k a b) : (processInput (n-1) (drop 3 inputData))
    | otherwise = []
    where [[_,k],a,b] = take 3 inputData

printOutput :: Bool -> IO ()
printOutput True  = putStrLn "YES"
printOutput False = putStrLn "NO"

main :: IO ()
main = do
    t <- readLn :: IO Int
    inputData <- getContents
    mapM_ printOutput $ processInput t $ (map (\x -> map read x :: [Int]) $ map words $ lines inputData)
