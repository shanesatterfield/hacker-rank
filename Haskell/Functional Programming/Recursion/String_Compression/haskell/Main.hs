module Main where

-- compress :: String -> String
-- compress text = compressList $ compressSplit text []
compress text = compressSplit text []

compressList :: [(Char, Integer)] -> String
compressList lst = foldl
    (\x y -> x ++ [(fst y)] ++ (if (snd y) == 1 then "" else (show $ snd y)))
    ""
    lst

compressSplit :: String -> [(Char, Integer)] -> [(Char, Integer)]
compressSplit text acc
    | null text = acc
    | null acc || a /= (fst c) = compressSplit b ((a, 1) : acc)
    | a == (fst c) = compressSplit b ((a, (snd c)+1) : (drop 1 acc))
    where
        a = last text
        b = init text
        c = head acc

main :: IO ()
main = getLine >>= print . compress
