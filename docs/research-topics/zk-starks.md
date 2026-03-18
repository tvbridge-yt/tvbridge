# zk-STARKs

STARKs are hash-based, transparent (no trusted setup), and post-quantum
friendly. The trade-off is proof size: STARK proofs are typically tens to
hundreds of kilobytes where SNARK proofs are a few hundred bytes.

The core machinery is FRI, a low-degree test for Reed-Solomon codes. Most
production zkVMs use STARKs internally and then wrap a final SNARK around the
STARK proof to shrink it for on-chain verification.
