module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (Main.update [2,-4,3,-1,23,-4,-54]) == [2,4,3,1,23,4,54]
