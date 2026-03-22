# Recursive proof composition

A recursive proof is a proof whose statement asserts the validity of another
proof. The result is a single short proof that summarizes an arbitrarily long
chain of computation.

Notable approaches:

- **Cycle of curves** for pairing-based recursion (Pasta, BN254 / Grumpkin).
- **Nova / SuperNova / HyperNova** for incrementally verifiable computation
  using folding schemes instead of SNARK recursion.
- **STARK-in-STARK** with a final SNARK wrap for on-chain verification.

Recursion is what makes "prove all of Ethereum in a few seconds" plausible.
