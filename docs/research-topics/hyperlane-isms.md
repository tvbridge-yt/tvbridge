# Hyperlane and ISMs

Hyperlane's central idea is the Interchain Security Module (ISM). An ISM is a
contract on the destination chain that decides whether to accept an incoming
message. Applications can install whichever ISM matches their threat model:

- **Multisig ISM** - simple validator set.
- **Aggregation ISM** - requires multiple ISMs to agree.
- **Routing ISM** - per-origin policy.
- **CCIP-Read ISM** - off-chain lookup with on-chain verification.

The point is that interchain security is no longer a property of the bridge,
it is a property of the application.
