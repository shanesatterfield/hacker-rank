module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.arrLen [2,5,1,4,3,7,8,6,0,9]) `shouldBe` 10
