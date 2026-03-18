# IBC overview

The Inter-Blockchain Communication protocol is the Cosmos-native interop
standard. It is a stack of three layers:

1. **TAO (transport, authentication, ordering)** - light client verification,
   connections, channels.
2. **Application layer** - ICS-20 fungible token transfer, ICS-27 interchain
   accounts, ICS-721 NFT transfer, etc.
3. **Relayer infrastructure** - permissionless off-chain processes that move
   packets and proofs between chains.

IBC is the cleanest example of "trust the consensus, not the multisig." It
also predates most modern bridges and influenced their security models.
