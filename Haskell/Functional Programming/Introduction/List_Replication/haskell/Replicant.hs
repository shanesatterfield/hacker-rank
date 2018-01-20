module Replicant (replicant) where

replicant n arr = foldl (\x y -> x ++ (replicate n y)) [] arr

main :: IO ()
main = getContents >>=
       mapM_ print. (\(n:arr) -> replicant n arr). map read. words
