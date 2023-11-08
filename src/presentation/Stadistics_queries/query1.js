db.accepted_code.aggregate([
  {
    $match: {
      "circuit.error": { $ne: null }
    }
  },
  {
    $group: {
      _id: "$circuit.error",
      count: { $sum: 1 }
    }
  },
  {
    $sort: { count: -1 }
  }
])

db.accepted_code.aggregate([
  {
    $group: {
      _id: "$metrics.error",
      count: { $sum: 1 }
    }
  },
  {
    $match: {
      _id: { $ne: null }
    }
  },
  {
    $sort: { count: -1 }
  }
])

db.accepted_code.aggregate([
  {
    $match: {
      "extension": "qiskit",
      "patterns.err_msg": { $ne: null }
    }
  },
  {
    $group: {
      _id: "$patterns.err_msg",
      count: { $sum: 1 }
    }
  },
  {
    $sort: { count: -1 }
  }
])