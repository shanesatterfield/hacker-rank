module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.funny "acxz") `shouldBe` True

        it "Test Case 2" $ do
            (Main.funny "bcxz") `shouldBe` False
