module ArrayOfN (aon) where

aon n = replicate n 1

main = do
    n <- readLn
    print $ aon n
