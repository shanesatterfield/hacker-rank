(defn n-times [n]
    (dorun (map println (take n (repeat "Hello World")))))

(n-times (Integer/parseInt (read-line)))
