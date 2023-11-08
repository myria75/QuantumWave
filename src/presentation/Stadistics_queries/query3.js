db.accepted_code.find({
  $and: [
    { "patterns.uncompute": { $type: "array" } },
    { "patterns.superposition": { $type: "array" } },
    { "patterns.initialization": { $type: "array" } },
    { "patterns.oracle": { $type: "array" } },
    { "patterns.entanglement": { $type: "array" } }
  ]
}, { "path": 1 })
