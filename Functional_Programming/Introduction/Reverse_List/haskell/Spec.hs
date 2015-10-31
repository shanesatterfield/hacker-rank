import Test.Hspec
import ReverseList

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (rev [19,22,3,28,26,17,18,4,28,0]) `shouldBe` [0,28,4,18,17,26,28,3,22,19]
