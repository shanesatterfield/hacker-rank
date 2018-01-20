module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.pangram "We promptly judged antique ivory buckles for the next prize") `shouldBe` True

        it "Test Case 2" $ do
            (Main.pangram "We promptly judged antique ivory buckles for the prize") `shouldBe` False
