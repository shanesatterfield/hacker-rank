(require '[clojure.string :as str])

(defn maxToys [k prices]
    (loop [money k lst (sort prices) count 0]
        (if (> (first lst) money)
            count
            (recur (- money (first lst)) (rest lst) (inc count)))))

(let [k (map #(Integer/parseInt %) (str/split (read-line) #"[^0-9]"))
    prices (map #(Integer/parseInt %) (str/split (read-line) #"[^0-9]"))]
    (println (maxToys (nth k 1) prices)))
