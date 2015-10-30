import Test.Hspec
import Replicant

main :: IO ()
main = hspec $ do
   describe "Test Cases" $ do
       it "Test Case 1" $ do
           (replicant 3 [1,2,3,4]) `shouldBe` [1,1,1,2,2,2,3,3,3,4,4,4]
