# zk-SNARKs

Succinct Non-interactive ARguments of Knowledge. The "succinct" part is the
interesting one: a verifier can check a proof in time roughly independent of
the size of the underlying computation.

The two flavors most often seen in production:

- **Groth16** - pairing-based, three group elements, requires a per-circuit
  trusted setup. Smallest proofs and fastest verification.
- **PLONK** - universal trusted setup with KZG commitments, custom gates and
  the plookup family of extensions. Slower verification than Groth16 but
  much friendlier to circuit upgrades.

Further reading lives in the topic catalog under the `groth16` and `plonk`
slugs.
