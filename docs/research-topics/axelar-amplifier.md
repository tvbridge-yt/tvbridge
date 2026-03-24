# Axelar Amplifier

Axelar Amplifier turns the Axelar network into a routing layer. Each
connected chain plugs in its own verifier set, gateway contract and prover.
Axelar itself coordinates message delivery and provides the GMP (General
Message Passing) interface.

It is the most "modular" of the production interop stacks: a new chain can
be added without changing the core protocol, as long as it ships its own
verifier and gateway.
