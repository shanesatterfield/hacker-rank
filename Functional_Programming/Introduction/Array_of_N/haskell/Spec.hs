import Test.Hspec
import ArrayOfN

main = hspec $ do
    describe "Provided Test Cases" $ do
        it "Test Case 1" $ do
            (length (aon 3)) `shouldBe` 3
