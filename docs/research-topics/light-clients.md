# ZK light clients

A light client verifies the consensus of a chain without storing the full
state. A *zk* light client wraps that verification in a succinct proof, so
that another chain can verify the source consensus in constant gas.

The dream: trust-minimized bridges where the only thing the destination chain
trusts is the source chain's consensus and a single succinct proof.

The reality: proving consensus is expensive, especially for chains with large
validator sets and BLS aggregation. Most production systems batch a window
of headers and amortize the proving cost.
