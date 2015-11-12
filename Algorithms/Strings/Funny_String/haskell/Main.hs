module Main where

import Data.Char

funny :: String -> Bool
funny text
    | null text = True
    | (abs (a - b)) == (abs (c - d)) = funny $ tail $ tail text
    | otherwise = False
    where
        a = ord $ head text
        b = ord $ head $ tail text
        r = reverse text
        c = ord $ head r
        d = ord $ head $ tail r

funnyPrint :: Bool -> IO ()
funnyPrint True  = putStrLn "Funny"
funnyPrint False = putStrLn "Not Funny"

main = getContents >>= (mapM_ funnyPrint) . (map funny) . words . tail
