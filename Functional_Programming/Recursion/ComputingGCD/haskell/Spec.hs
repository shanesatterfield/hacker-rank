module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.computeGCD 1 5) `shouldBe` 1

        it "Test Case 2" $ do
            (Main.computeGCD 10023 123123) `shouldBe` 39
