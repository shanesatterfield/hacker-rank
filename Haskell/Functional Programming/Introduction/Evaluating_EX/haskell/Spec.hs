module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.ex 20.0000) `shouldBe` 2423600.1887
        it "Test Case 2" $ do
            (Main.ex 5.0000) `shouldBe` 143.6894
        it "Test Case 3" $ do
            (Main.ex 0.5000) `shouldBe` 1.6487
        it "Test Case 4" $ do
            (Main.ex (-0.5000)) `shouldBe` 0.6065
