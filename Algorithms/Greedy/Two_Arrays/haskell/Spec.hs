module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.tarrs 10 [2,1,3] [7,8,9]) `shouldBe` True

        it "Test Case 2" $ do
            (Main.tarrs 5 [1,2,2,1] [3,3,3,4]) `shouldBe` False
