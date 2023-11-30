db.getCollection("qiskit").find({"circuit":{$regex : "\".*\""}, "patterns.initialization": { $type: "array" } })
