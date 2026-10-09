# Standalone MCRT Portal Timeline Language Profile

## Identity

- Language ID: `mcrt.portal.timeline`
- Version represented by the corpus: `0.3`
- Preferred source extension: `.mcrt`
- Execution posture: deterministic, provenance-preserving, and no-network by default

## Core semantic objects

A program declares a rational timebase, one or more timelines, nested sequences, tracks, clips, keys, markers, events, transitions, synchronization groups, branches, checkpoints, portal bindings, and replay/restoration requirements.

## Required evidence path

```text
source → typed timeline AST → semantic judgment → safety gate
       → normalized timeline IR → optimization equivalence
       → R12 record → MCRT receipt → deterministic runtime trace
```

A conforming implementation must distinguish static acceptance from native playback. A source can be structurally valid while its modeled validation record expects a controlled rejection at name resolution, semantic validation, runtime validation, or certification.

## Safety profile

The default suite profile prohibits undeclared networking and unknown-code execution. Portal and scene bindings must be explicit. Time values must be rational and nonnegative where required. Synchronization must be deadlock-checked. Replay requires stable hashes and checkpoint closure.
