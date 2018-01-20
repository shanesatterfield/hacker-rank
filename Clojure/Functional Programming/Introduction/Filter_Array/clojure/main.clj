(def inputData (map #(Integer/parseInt %) (line-seq (java.io.BufferedReader. *in*))))

(defn filtArr [delim lst]
    (filter (fn [x] (< x delim)) lst))
    
(dorun (map println (filtArr (first inputData) (rest inputData))))
