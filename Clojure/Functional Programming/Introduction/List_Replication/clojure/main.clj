(def inputData (map #(Integer/parseInt %) (line-seq (java.io.BufferedReader. *in*))))

(defn replicant [n arr]
    (reduce (fn [x y] (concat x (repeat n y))) [] arr))

(dorun (map println (replicant (first inputData) (rest inputData))))
