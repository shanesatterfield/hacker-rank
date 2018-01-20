module Main where

import Data.Char
import Data.List

pangram :: String -> Bool
pangram text = length (nub $ map toLower $ filter isAlpha text) == 26

pagramText True = "pangram"
pagramText False = "not pangram"

main = getContents >>= putStrLn . pagramText . pangram
