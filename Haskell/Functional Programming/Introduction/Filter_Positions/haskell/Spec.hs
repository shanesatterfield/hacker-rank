import Test.Hspec
import FilterPositions

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (filt [2,5,3,4,6,7,9,8]) `shouldBe` [5,4,7,8]

        it "Test Case 2" $ do
            (filt [8,15,22,1,10,6,2,18,18,1]) `shouldBe` [15,1,6,18,1]

    describe "Edge Cases" $ do
        it "works with empty list" $ do
            (filt []) `shouldBe` []

        it "should return empty list given 1 element list" $ do
            (filt [1]) `shouldBe` []

        it "should return the second elemnt of two element list" $ do
            (filt [1,2]) `shouldBe` [2]

        it "should work infinitely" $ do
            (filt [0..10000]) `shouldBe` [1,3..10000]
