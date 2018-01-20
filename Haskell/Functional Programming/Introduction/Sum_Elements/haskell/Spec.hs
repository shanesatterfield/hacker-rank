import Test.Hspec
import SumElements

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (sooe [3,2,4,6,5,7,8,0,1]) `shouldBe` 16
