module Main where

mingle :: String -> String -> String
mingle "" "" = []
mingle a b = (head a) : (head b) : (mingle (tail a) (tail b))

main = do
    a <- getLine
    b <- getLine
    putStrLn $ mingle a b
