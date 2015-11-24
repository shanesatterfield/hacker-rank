(require '[clojure.test :refer :all] '[clojure.string :as str])

(defn flowers [k prices]
    (let [startingList (reverse (sort prices))]
        (loop [lst startingList i 0 result 0]
            (if (empty? lst)
                result
                (recur (drop k lst) (inc i) (+ result (* (inc i) (reduce + (take k lst)))))))))

(let [[_,k] (map #(Integer/parseInt %) (str/split (read-line) #"[^0-9]"))
    prices  (map #(Integer/parseInt %) (str/split (read-line) #"[^0-9]"))]
    (println (flowers k prices)))

(testing "Provided Test Cases"
    (testing "Test Case 1"
        (is (= 13 (flowers 3 [2 5 6]))))
    (testing "Test Case 2"
        (is (= 15 (flowers 2 [2 5 6])))))
