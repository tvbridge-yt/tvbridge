# Wormhole and VAAs

A VAA (Verified Action Approval) is a message signed by the Wormhole
guardian set. Once a quorum of guardians has signed, any chain that knows
the guardian set's public keys can verify the VAA on-chain.

The model is simple, fast, and centralized on the guardian set. Wormhole
has been steadily moving toward more permissionless verification through
the **Native Token Transfers** framework and ZK guardian proofs, but the
guardian-signed VAA is still the workhorse.
