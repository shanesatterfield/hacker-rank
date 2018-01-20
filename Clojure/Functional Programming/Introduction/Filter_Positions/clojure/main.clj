(def inputData (map #(Integer/parseInt %) (line-seq (java.io.BufferedReader. *in*))))

(defn filt
    "Returns a list of only the even elements (starts at 1 not 0)."
    [arr]
    (loop [lst arr acc []]
        (if (empty? lst)
            acc
            (recur
                (rest (rest lst))
                (conj acc (first (rest lst)))))))

(dorun (map println (filt inputData)))
