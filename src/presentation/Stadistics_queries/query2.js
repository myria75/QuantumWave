var countInitialization = db.accepted_code.find({ "patterns.initialization": { $type: "array" } }).count();
var countSuperposition = db.accepted_code.find({ "patterns.superposition": { $type: "array" } }).count();
var countEntanglement = db.accepted_code.find({ "patterns.entanglement": { $type: "array" } }).count();
var countOracle = db.accepted_code.find({ "patterns.oracle": { $type: "array" } }).count();
var countUncompute = db.accepted_code.find({ "patterns.uncompute": { $type: "array" } }).count();

print("Tipo de Patrón\tCantidad de Elementos Contados");
print("Initialization\t" + countInitialization);
print("Superposition\t" + countSuperposition);
print("Entanglement\t" + countEntanglement);
print("Oracle\t" + countOracle );
print("Uncompute\t" + countUncompute);
