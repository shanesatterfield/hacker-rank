module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.maxToys 50 [1,12,5,111,200,1000,10]) `shouldBe` 4
