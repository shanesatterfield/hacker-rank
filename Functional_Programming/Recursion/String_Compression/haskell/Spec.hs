module Spec where

import Test.Hspec
import qualified Main

main :: IO ()
main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.compress "abcaaabbb") `shouldBe` "abca3b3"

        it "Test Case 2" $ do
            (Main.compress "abcd") `shouldBe` "abcd"

        it "Test Case 3" $ do
            (Main.compress "aaabaaaaccaaaaba") `shouldBe` "a3ba4c2a4ba"
