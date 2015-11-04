module Spec where

import Test.Hspec
import qualified Main

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test case 1" $ do
            (Main.permutate "abcdpqrs") `shouldBe` "badcqpsr"

        it "Test Case 2" $ do
            (Main.permutate "az") `shouldBe` "za"
