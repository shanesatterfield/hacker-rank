module Main where

computeGCD :: Integral a => a -> a -> a
computeGCD a b
    | r == 0    = y
    | x >  y    = computeGCD y r
    | otherwise = 1
    where
        r = x `mod` y
        x = max a b
        y = min a b

main = do
    inputData <- getContents
    let [a,b] = (map read $ words inputData :: [Int])
    print $ computeGCD a b

-- Provided Main Loop

-- main = do
--   input <- getLine
--   print . uncurry gcd' . listToTuple . convertToInt . words $ input
--  where
--   listToTuple (x:xs:_) = (x,xs)
--   convertToInt = map (read :: String -> Int)
