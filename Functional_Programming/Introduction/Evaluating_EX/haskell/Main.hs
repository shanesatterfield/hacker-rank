module Main where

import Numeric

ex :: Float -> Float
ex x = formFit $ exRec x 0 1

exRec x i fac
    | i <  10 = (x ** i) / (nextFac) + (exRec x (i+1) nextFac)
    | i >= 10 = 0.0
    where nextFac = max 1 $ fac * i

formFit :: Float -> Float
formFit num = read $ showFFloat (Just 4) num "" :: Float

main :: IO ()
main = do
    inputData <- getContents
    mapM_ print $ map ex (map read (tail $ words inputData) :: [Float])
