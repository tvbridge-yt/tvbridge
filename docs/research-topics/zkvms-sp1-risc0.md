# zkVMs: SP1 and RISC Zero

Two general-purpose RISC-V zkVMs from the current generation:

- **SP1** (Succinct Labs) - aggressive precompiles for ECDSA, keccak,
  ed25519, and BN254 pairings. Strong tooling, public benchmarks.
- **RISC Zero** - the original RISC-V zkVM, with continuations for
  long-running proofs and a mature Rust toolchain.

Both compile unmodified Rust and produce STARK proofs that can be wrapped in
a final SNARK for on-chain verification. The design space is starting to
converge, and the interesting differences are now in the precompiles and the
proving system.
