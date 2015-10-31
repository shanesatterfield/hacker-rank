module SumElements (sooe) where

sooe :: [Int] -> Int
sooe arr = sum (filter (\x -> x `mod` 2 == 1) arr)

main = do
   inputdata <- getContents
   putStrLn $ show $ sooe $ map (read :: String -> Int) $ lines inputdata
