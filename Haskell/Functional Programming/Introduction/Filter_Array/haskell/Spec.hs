import Test.Hspec
import FilterArray

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (filt 3 [10,9,8,2,7,5,1,3,0]) `shouldBe` [2,1,0]

        it "Test Case 2" $ do
            (filt 25 [25,-41,46,-28,21,52,83,-29,84,27,40]) == [-41,-28,21,-29]
