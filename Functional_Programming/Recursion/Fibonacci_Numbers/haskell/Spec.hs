module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.fib 3) `shouldBe` 1

    describe "Edge Cases" $ do
        it "should return 0 when negative" $ do
            (Main.fib (-1)) `shouldBe` 0

        it "should return 0 when 0" $ do
            (Main.fib 0) `shouldBe` 0

        it "should return 0 when 1" $ do
            (Main.fib 1) `shouldBe` 0

        it "should return 1 when 2" $ do
            (Main.fib 2) `shouldBe` 1

        it "should return 63245986 when 40" $ do
            (Main.fib 40) `shouldBe` 63245986
