module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.pascal 4) `shouldBe` [[1],[1,1],[1,2,1],[1,3,3,1]]
