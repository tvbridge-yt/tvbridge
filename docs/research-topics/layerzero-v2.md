# LayerZero v2

LayerZero v2 splits the messaging stack into a **DVN** (decentralized
verifier network) layer and an **executor** layer. Applications choose their
own DVN set and threshold, which lets each app pick its own security model.

Key concepts:

- **OApp** - the application contract that sends and receives messages.
- **DVN** - signs the message hash on the destination chain.
- **Executor** - delivers the message once the DVN quorum is reached.

The configurability is the headline feature, and also the footgun.
