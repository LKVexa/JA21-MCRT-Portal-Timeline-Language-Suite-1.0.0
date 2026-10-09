# JA21 MCRT Portal Timeline Language Textbook

## Publication statement

This textbook treats MCRT Portal Timeline as a JA21 programming-language component for deterministic temporal authoring, portal transitions, scene coupling, replay, and evidence. Smithson 8S Coupled Mechanics is presented as a proposed computational framework, not as established physical law. Corpus compiler and runtime outcomes are modeled evidence unless a native tool explicitly appends observed results.

## Contents

1. Language Identity and Evidence-Bearing Timelines
2. Program Anatomy, Modules, Metadata, and Policy
3. Rational Timebases, Durations, and Rates
4. Timelines, Sequences, and Nested Structure
5. Tracks, Clips, Keys, Markers, and Events
6. Clip Trimming, Easing, and Transitions
7. Temporal Constraints and Interval Analysis
8. Synchronization Groups and Multitrack Barriers
9. Scene Binding and Synchronized Motion/VFX
10. Branching and Deterministic Choice
11. Branched Narrative and Interactive Cinematics
12. Procedural Timelines
13. Portal Transitions
14. Checkpoints and Checkpointed Sequences
15. Replay Plans, Replay, and Restoration
16. Typed Timeline AST and Semantic Judgments
17. Compiler Pipeline and Safety Gates
18. Optimization Without Temporal Drift
19. R12 Lowering and MCRT Emission
20. Diagnostics, Negative Cases, and Recovery
21. Certification and Smithson 8S Coupled Mechanics
22. Standalone Portal Timeline Toolchain Capstone

## Chapter 1: Language Identity and Evidence-Bearing Timelines

### Purpose

Establish the distinction between a timeline description, its compiler evidence, and a native playback claim. This chapter is anchored in `timeline_header`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_00004
policy no_network
metadata { timebase: 60/1 deterministic: true }
timeline Timeline00004 {
  duration: 9s
  sequence Sequence00004 {
    track Main {
      clip Clip00004 from 0s to 6s rate 1/1
      key 4/10s value 0.7
      marker Mark4 at 5s
      event Event4 at 6s payload { topic: "timeline_header" }
    }
  }
}
```

The example is `EX-MPTL-00004`, tier 1 (`basic_syntax`), class `positive`, and topic `timeline_header`. Its source identity is `sha256:9458b8fb2c2934cd15fc34c98585a1a2ed1b476adc5d163f5202e01f085375ac` and semantic identity is `sha256:def8305049189f8fde06fe9df900dc545765760df36865b02172e6191c11d84c`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 2: Program Anatomy, Modules, Metadata, and Policy

### Purpose

Read the header, module identity, deterministic metadata, and no-network posture as executable governance. This chapter is anchored in `timeline_header`, `rational_timebase`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_00004
policy no_network
metadata { timebase: 60/1 deterministic: true }
timeline Timeline00004 {
  duration: 9s
  sequence Sequence00004 {
    track Main {
      clip Clip00004 from 0s to 6s rate 1/1
      key 4/10s value 0.7
      marker Mark4 at 5s
      event Event4 at 6s payload { topic: "timeline_header" }
    }
  }
}
```

The example is `EX-MPTL-00004`, tier 1 (`basic_syntax`), class `positive`, and topic `timeline_header`. Its source identity is `sha256:9458b8fb2c2934cd15fc34c98585a1a2ed1b476adc5d163f5202e01f085375ac` and semantic identity is `sha256:def8305049189f8fde06fe9df900dc545765760df36865b02172e6191c11d84c`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 3: Rational Timebases, Durations, and Rates

### Purpose

Treat time as exact rational data and reject invalid duration or rate domains before scheduling. This chapter is anchored in `rational_timebase`, `duration_rate`, `negative_duration`, `non_rational_time`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_00003
policy no_network
metadata { timebase: 48/1 deterministic: true }
timeline Timeline00003 {
  duration: 8s
  sequence Sequence00003 {
    track Main {
      clip Clip00003 from 0s to 5s rate 1/1
      key 3/10s value 0.6
      marker Mark3 at 4s
      event Event3 at 5s payload { topic: "rational_timebase" }
    }
  }
}
```

The example is `EX-MPTL-00003`, tier 1 (`basic_syntax`), class `positive`, and topic `rational_timebase`. Its source identity is `sha256:347438dc3fab0420833129c67123fc7035f1db45c045133ed0dd6fd154e7718a` and semantic identity is `sha256:768a0065c90de29f40f4c02c6f0fff484d1e99a5e984d62a7d09ea393fb620b0`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 4: Timelines, Sequences, and Nested Structure

### Purpose

Model temporal containment, local coordinate systems, and deterministic nested ordering. This chapter is anchored in `sequence`, `nested_sequence`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_00002
policy no_network
metadata { timebase: 30/1 deterministic: true }
timeline Timeline00002 {
  duration: 7s
  sequence Sequence00002 {
    track Main {
      clip Clip00002 from 0s to 4s rate 1/1
      key 2/10s value 0.5
      marker Mark2 at 3s
      event Event2 at 4s payload { topic: "sequence" }
    }
  }
}
```

The example is `EX-MPTL-00002`, tier 1 (`basic_syntax`), class `positive`, and topic `sequence`. Its source identity is `sha256:cc07246f1545d00f6c0d190f46b7716de286307ab7c27371b105da2df8f74078` and semantic identity is `sha256:143f36ae6c22fecfc5ce9dee129c4f968e28a644a86de50488901aa0fe3940be`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 5: Tracks, Clips, Keys, Markers, and Events

### Purpose

Build the fundamental authored timeline surface and distinguish sampled values from named temporal events. This chapter is anchored in `track`, `clip`, `key`, `marker`, `event`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_00001
policy no_network
metadata { timebase: 25/1 deterministic: true }
timeline Timeline00001 {
  duration: 6s
  sequence Sequence00001 {
    track Main {
      clip Clip00001 from 0s to 3s rate 1/1
      key 1/10s value 0.4
      marker Mark1 at 2s
      event Event1 at 3s payload { topic: "track" }
    }
  }
}
```

The example is `EX-MPTL-00001`, tier 1 (`basic_syntax`), class `positive`, and topic `track`. Its source identity is `sha256:daf1989c0ca8793ff74dc3ef25804c8f08adcc3dc42be4c81ef8e11be69235d2` and semantic identity is `sha256:d51ea7023868852e718831321b4ffe78c058e05cd3be647c777da4d14c6b7fae`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 6: Clip Trimming, Easing, and Transitions

### Purpose

Preserve intent while editing intervals, interpolation laws, and transition envelopes. This chapter is anchored in `clip_trimming`, `easing`, `transition`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_01001
policy no_network
metadata { timebase: 25/1 deterministic: true }
timeline Timeline01001 {
  sequence Sequence01001 {
    track Camera bind scene.MainCamera { clip Establish from 0s to 4s easing ease_in_out }
    track Portal bind scene.PortalA { clip Open from 3s to 7s trim 0.25s..3.75s }
    transition Establish -> Open duration 1s mode crossfade
    branch Choice1 at 5s { when flag("authorized") -> Open otherwise -> Establish }
    sync group Sync0 { Camera, Portal }
    checkpoint CP01001 at 6s restore [Camera, Portal]
  }
}
```

The example is `EX-MPTL-01001`, tier 2 (`intermediate_constructs`), class `positive`, and topic `clip_trimming`. Its source identity is `sha256:fd1017d9e09b12171866b2ca1beabee3fecb26253f184450530d006829a1bf41` and semantic identity is `sha256:3ba155f1982be0d294789aba1f20f3e56040c19deb54476347dc2bf808804cfb`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 7: Temporal Constraints and Interval Analysis

### Purpose

Prove interval relations and detect contradictions such as forbidden exclusive overlap. This chapter is anchored in `temporal_constraint`, `interval_analysis`, `exclusive_overlap`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_02504
policy no_network
metadata { timebase: 60/1 deterministic: true }
timeline Timeline02504 {
  procedural sequence Sequence02504 seed 2504 {
    track Scene { clip PortalArrival from 0s to 8s bind scene.PortalScene20 }
    track Motion { clip Walk from 1s to 7s bind motion.Actor5 }
    track VFX { clip PortalGlow from 2s to 6s bind vfx.Portal7 }
    barrier AllReady at 2s requires [Scene, Motion, VFX]
    branch Outcome at 6s deterministic_by "state_hash" {
      when state.success -> Success
      otherwise -> Restore
    }
    checkpoint Restore at 5s
    replay hash sha256("timeline:02504")
  }
}
```

The example is `EX-MPTL-02504`, tier 3 (`advanced_composition`), class `positive`, and topic `temporal_constraint`. Its source identity is `sha256:835e9caf39773e82d060371098db4aa14ae357949df046e4df897e0ce52fc2dc` and semantic identity is `sha256:a95e9676a555db562c02a041d157e89484308051b6bc298f3245a3857f0b9b38`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 8: Synchronization Groups and Multitrack Barriers

### Purpose

Coordinate concurrent tracks without introducing circular waits or nondeterministic release order. This chapter is anchored in `sync_group`, `multitrack_barrier`, `sync_deadlock`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_01004
policy no_network
metadata { timebase: 60/1 deterministic: true }
timeline Timeline01004 {
  sequence Sequence01004 {
    track Camera bind scene.MainCamera { clip Establish from 0s to 4s easing ease_in_out }
    track Portal bind scene.PortalA { clip Open from 3s to 7s trim 0.25s..3.75s }
    transition Establish -> Open duration 1s mode crossfade
    branch Choice4 at 5s { when flag("authorized") -> Open otherwise -> Establish }
    sync group Sync3 { Camera, Portal }
    checkpoint CP01004 at 6s restore [Camera, Portal]
  }
}
```

The example is `EX-MPTL-01004`, tier 2 (`intermediate_constructs`), class `positive`, and topic `sync_group`. Its source identity is `sha256:d7c5bc882f587cb65846f86e5b58290596d91ba837f8cd3b2bdecb153eb805bd` and semantic identity is `sha256:7e1ea976eda9611b392392b4f20955c155374685c33a178c8a0ed994676a651f`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 9: Scene Binding and Synchronized Motion/VFX

### Purpose

Bind timeline outputs to scene entities, motion channels, and VFX with stable identity and units. This chapter is anchored in `scene_binding`, `track_binding`, `synchronized_scene_motion_vfx`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_02518
policy no_network
metadata { timebase: 48/1 deterministic: true }
timeline Timeline02518 {
  procedural sequence Sequence02518 seed 2518 {
    track Scene { clip PortalArrival from 0s to 8s bind scene.PortalScene11 }
    track Motion { clip Walk from 1s to 7s bind motion.Actor2 }
    track VFX { clip PortalGlow from 2s to 6s bind vfx.Portal10 }
    barrier AllReady at 2s requires [Scene, Motion, VFX]
    branch Outcome at 6s deterministic_by "state_hash" {
      when state.success -> Success
      otherwise -> Restore
    }
    checkpoint Restore at 5s
    replay hash sha256("timeline:02518")
  }
}
```

The example is `EX-MPTL-02518`, tier 3 (`advanced_composition`), class `positive`, and topic `scene_binding`. Its source identity is `sha256:54eff5e13b9dbb18711257f782a9782714c791c9e758dbc4783b8b7d3ddce47a` and semantic identity is `sha256:67edb89cfa4b10c6271e10fab709869c3a3f09309a7d3c59016af5d4f4446bd4`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 10: Branching and Deterministic Choice

### Purpose

Represent branch conditions, prove reachability, and make choice replayable. This chapter is anchored in `branching`, `deterministic_branch`, `unreachable_branch`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_01003
policy no_network
metadata { timebase: 48/1 deterministic: true }
timeline Timeline01003 {
  sequence Sequence01003 {
    track Camera bind scene.MainCamera { clip Establish from 0s to 4s easing ease_in_out }
    track Portal bind scene.PortalA { clip Open from 3s to 7s trim 0.25s..3.75s }
    transition Establish -> Open duration 1s mode crossfade
    branch Choice3 at 5s { when flag("authorized") -> Open otherwise -> Establish }
    sync group Sync2 { Camera, Portal }
    checkpoint CP01003 at 6s restore [Camera, Portal]
  }
}
```

The example is `EX-MPTL-01003`, tier 2 (`intermediate_constructs`), class `positive`, and topic `branching`. Its source identity is `sha256:9ca728f12707666c2ca1afa730e47cffb92a4ea84fd05f05ca6bf46fe2ab491f` and semantic identity is `sha256:a46cc91061779c961d01602a881abbe77d4d45dc1ece95cc12ca8434c3bf0bae`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 11: Branched Narrative and Interactive Cinematics

### Purpose

Compose authored narrative, user interaction, and playback state without losing evidence. This chapter is anchored in `branched_narrative`, `interactive_cinematic`, `cinematic_playback`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_05003
policy no_network
metadata { timebase: 48/1 deterministic: true }
timeline Timeline05003 {
  sequence Intro { track Camera { clip FlyIn from 0s to 5s } track VFX { clip Weather from 0s to 12s } }
  sequence PortalCrossing {
    track Scene { clip OpenPortal from 0s to 4s }
    track Motion { clip Traverse from 2s to 8s }
    track VFX { clip Distortion from 1s to 9s }
    sync group PortalSync { Scene, Motion, VFX }
    checkpoint BeforeCrossing at 1s restore [Scene, Motion, VFX]
  }
  branch Narrative5 at 10s { when choice("left") -> Intro otherwise -> PortalCrossing }
  cinematic playback deterministic replayable true
}
```

The example is `EX-MPTL-05003`, tier 4 (`large_integrated_examples`), class `positive`, and topic `branched_narrative`. Its source identity is `sha256:848729ef3dfe4b691f09a84d2fb5d90012c91413b5fd53c39dd42ef2cdf7b60c` and semantic identity is `sha256:c8623cb5cdc8bb5dc56ab5b6a35eecf1e7b74c0ab792749286344ae84bdb01a3`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 12: Procedural Timelines

### Purpose

Generate timeline structure from deterministic inputs while retaining source-to-generated provenance. This chapter is anchored in `procedural_timeline`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_02505
policy no_network
metadata { timebase: 24/1 deterministic: true }
timeline Timeline02505 {
  procedural sequence Sequence02505 seed 2505 {
    track Scene { clip PortalArrival from 0s to 8s bind scene.PortalScene21 }
    track Motion { clip Walk from 1s to 7s bind motion.Actor6 }
    track VFX { clip PortalGlow from 2s to 6s bind vfx.Portal8 }
    barrier AllReady at 2s requires [Scene, Motion, VFX]
    branch Outcome at 6s deterministic_by "state_hash" {
      when state.success -> Success
      otherwise -> Restore
    }
    checkpoint Restore at 5s
    replay hash sha256("timeline:02505")
  }
}
```

The example is `EX-MPTL-02505`, tier 3 (`advanced_composition`), class `positive`, and topic `procedural_timeline`. Its source identity is `sha256:fb17f0e9a7677c6579e1a216dc3bb2413135977106efa64cbf9673b33d2aafb9` and semantic identity is `sha256:413020d9b810554df8c1d131648d18cb591fbebad6d4f7308a4568515254e00e`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 13: Portal Transitions

### Purpose

Coordinate source scene, destination scene, transition phase, and continuity guarantees. This chapter is anchored in `portal_transition`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_05002
policy no_network
metadata { timebase: 30/1 deterministic: true }
timeline Timeline05002 {
  sequence Intro { track Camera { clip FlyIn from 0s to 5s } track VFX { clip Weather from 0s to 12s } }
  sequence PortalCrossing {
    track Scene { clip OpenPortal from 0s to 4s }
    track Motion { clip Traverse from 2s to 8s }
    track VFX { clip Distortion from 1s to 9s }
    sync group PortalSync { Scene, Motion, VFX }
    checkpoint BeforeCrossing at 1s restore [Scene, Motion, VFX]
  }
  branch Narrative4 at 10s { when choice("left") -> Intro otherwise -> PortalCrossing }
  cinematic playback deterministic replayable true
}
```

The example is `EX-MPTL-05002`, tier 4 (`large_integrated_examples`), class `positive`, and topic `portal_transition`. Its source identity is `sha256:44c5080a127008a3b5f6db9067dc38ad35b639323412c79cbeb066fb011d2902` and semantic identity is `sha256:e894ede9488b7cc568d25bbf5f9d20cb2846caac0e47f49bd49cba07858432c3`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 14: Checkpoints and Checkpointed Sequences

### Purpose

Declare recovery points and require closure before irreversible transitions. This chapter is anchored in `checkpoint`, `checkpointed_sequence`, `missing_checkpoint`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_01021
policy no_network
metadata { timebase: 25/1 deterministic: true }
timeline Timeline01021 {
  sequence Sequence01021 {
    track Camera bind scene.MainCamera { clip Establish from 0s to 4s easing ease_in_out }
    track Portal bind scene.PortalA { clip Open from 3s to 7s trim 0.25s..3.75s }
    transition Establish -> Open duration 1s mode crossfade
    branch Choice1 at 5s { when flag("authorized") -> Open otherwise -> Establish }
    sync group Sync6 { Camera, Portal }
    checkpoint CP01021 at 6s restore [Camera, Portal]
  }
}
```

The example is `EX-MPTL-01021`, tier 2 (`intermediate_constructs`), class `positive`, and topic `checkpoint`. Its source identity is `sha256:f090f677a2d7b3ae81094b9b5b9e8bf6f5ebfbbb3f42110f3c538a939b695280` and semantic identity is `sha256:14bf59ef333a0a74899799bb9c9ef4bc0f8382d41ba30cf790a183c281a8d2ad`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 15: Replay Plans, Replay, and Restoration

### Purpose

Turn execution into a verifiable receipt and restore state only from hash-consistent evidence. This chapter is anchored in `replay_plan`, `replay`, `restoration`, `replay_hash_mismatch`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_07501
policy no_network
metadata { timebase: 25/1 deterministic: true }
timeline Timeline07501 {
  sequence Sequence07501 {
    track A { clip Static from 0/1s to 120/24s key 0/24s value 1 key 24/24s value 1 }
    track Dead { clip Unbound from 0/1s to 24/24s enabled false }
    branch B at 48/24s { when true -> A otherwise -> Dead }
    checkpoint CP at 60/24s
  }
}
optimize timeline Timeline07501 using [time_normalization, interval_analysis, dead_track_removal, key_reduction(0.001), checkpoint_indexing]
lower Timeline07501 to PORTAL_TIMELINE_R12
```

The example is `EX-MPTL-07501`, tier 5 (`compiler_optimization`), class `positive`, and topic `replay_plan`. Its source identity is `sha256:ad9f0fd55eed1d05260c508f9aec2a2cadfb0bb12b4e2036a0576377a64f4e10` and semantic identity is `sha256:c18d91eca05ce252a5d15182da32ed031cba028e534ac8236c5bc556ab86928a`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 16: Typed Timeline AST and Semantic Judgments

### Purpose

Understand how syntax becomes typed nodes, effects, preconditions, postconditions, and policy requirements. This chapter is anchored in `timeline_header`, `temporal_constraint`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_00004
policy no_network
metadata { timebase: 60/1 deterministic: true }
timeline Timeline00004 {
  duration: 9s
  sequence Sequence00004 {
    track Main {
      clip Clip00004 from 0s to 6s rate 1/1
      key 4/10s value 0.7
      marker Mark4 at 5s
      event Event4 at 6s payload { topic: "timeline_header" }
    }
  }
}
```

The example is `EX-MPTL-00004`, tier 1 (`basic_syntax`), class `positive`, and topic `timeline_header`. Its source identity is `sha256:9458b8fb2c2934cd15fc34c98585a1a2ed1b476adc5d163f5202e01f085375ac` and semantic identity is `sha256:def8305049189f8fde06fe9df900dc545765760df36865b02172e6191c11d84c`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 17: Compiler Pipeline and Safety Gates

### Purpose

Separate parsing, name resolution, semantic validation, safety, normalization, and lowering. This chapter is anchored in `r12_mcrt_lowering`, `branch_lowering`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_07502
policy no_network
metadata { timebase: 30/1 deterministic: true }
timeline Timeline07502 {
  sequence Sequence07502 {
    track A { clip Static from 0/1s to 120/24s key 0/24s value 1 key 24/24s value 1 }
    track Dead { clip Unbound from 0/1s to 24/24s enabled false }
    branch B at 48/24s { when true -> A otherwise -> Dead }
    checkpoint CP at 60/24s
  }
}
optimize timeline Timeline07502 using [time_normalization, interval_analysis, dead_track_removal, key_reduction(0.001), checkpoint_indexing]
lower Timeline07502 to PORTAL_TIMELINE_R12
```

The example is `EX-MPTL-07502`, tier 5 (`compiler_optimization`), class `positive`, and topic `r12_mcrt_lowering`. Its source identity is `sha256:40cbde2ec8007f8999e3a19e0dfd35a320df14c572031dd699ade5263b016050` and semantic identity is `sha256:32476f4e3fa0df718ffb4308bc7b3a4dfe1d07b2745af011b286b9492054c28a`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 18: Optimization Without Temporal Drift

### Purpose

Apply reductions only when observable timing, events, and branch outcomes remain equivalent. This chapter is anchored in `time_normalization`, `clip_trimming`, `dead_track_removal`, `key_reduction`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_07503
policy no_network
metadata { timebase: 48/1 deterministic: true }
timeline Timeline07503 {
  sequence Sequence07503 {
    track A { clip Static from 0/1s to 120/24s key 0/24s value 1 key 24/24s value 1 }
    track Dead { clip Unbound from 0/1s to 24/24s enabled false }
    branch B at 48/24s { when true -> A otherwise -> Dead }
    checkpoint CP at 60/24s
  }
}
optimize timeline Timeline07503 using [time_normalization, interval_analysis, dead_track_removal, key_reduction(0.001), checkpoint_indexing]
lower Timeline07503 to PORTAL_TIMELINE_R12
```

The example is `EX-MPTL-07503`, tier 5 (`compiler_optimization`), class `positive`, and topic `time_normalization`. Its source identity is `sha256:f3e1783272dc90c7ce6518607defc8c99a8fcaf18b8e4dda0451414b1cbf3ee6` and semantic identity is `sha256:898260a4410a7db4e71a4977dcb82d57427bad3d36cb1cbe5eef3432880c7b81`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 19: R12 Lowering and MCRT Emission

### Purpose

Package authoritative state, provenance, diagnostics, and runtime intent into stable records. This chapter is anchored in `r12_mcrt_lowering`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_07502
policy no_network
metadata { timebase: 30/1 deterministic: true }
timeline Timeline07502 {
  sequence Sequence07502 {
    track A { clip Static from 0/1s to 120/24s key 0/24s value 1 key 24/24s value 1 }
    track Dead { clip Unbound from 0/1s to 24/24s enabled false }
    branch B at 48/24s { when true -> A otherwise -> Dead }
    checkpoint CP at 60/24s
  }
}
optimize timeline Timeline07502 using [time_normalization, interval_analysis, dead_track_removal, key_reduction(0.001), checkpoint_indexing]
lower Timeline07502 to PORTAL_TIMELINE_R12
```

The example is `EX-MPTL-07502`, tier 5 (`compiler_optimization`), class `positive`, and topic `r12_mcrt_lowering`. Its source identity is `sha256:40cbde2ec8007f8999e3a19e0dfd35a320df14c572031dd699ade5263b016050` and semantic identity is `sha256:32476f4e3fa0df718ffb4308bc7b3a4dfe1d07b2745af011b286b9492054c28a`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 20: Diagnostics, Negative Cases, and Recovery

### Purpose

Use negative examples as executable specification boundaries rather than defective filler. This chapter is anchored in `negative_duration`, `non_rational_time`, `sync_deadlock`, `missing_checkpoint`, `replay_hash_mismatch`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_09004
policy no_network
metadata { timebase: 60/1 deterministic: true }
timeline Timeline09004 { sequence Sequence09004 { track Main { clip Broken from 5s to 2s } } }
certify timeline Timeline09004 using strict_timeline
```

The example is `EX-MPTL-09004`, tier 6 (`validation_certification`), class `negative`, and topic `negative_duration`. Its source identity is `sha256:d9ad4516423295e49fb27f5b63d13c8f2a830a3884d031e5fd2ed87eabe05026` and semantic identity is `sha256:14bcfc40d35c2753eb76e3d607f441b576f6728d3445e8dfe26be7a82b8e2bd4`. The corpus expects the case to reach `semantic_validation`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 21: Certification and Smithson 8S Coupled Mechanics

### Purpose

Audit certification evidence and clearly separate computational coupling models from established physical law. This chapter is anchored in `portal_transition`, `synchronized_scene_motion_vfx`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_05002
policy no_network
metadata { timebase: 30/1 deterministic: true }
timeline Timeline05002 {
  sequence Intro { track Camera { clip FlyIn from 0s to 5s } track VFX { clip Weather from 0s to 12s } }
  sequence PortalCrossing {
    track Scene { clip OpenPortal from 0s to 4s }
    track Motion { clip Traverse from 2s to 8s }
    track VFX { clip Distortion from 1s to 9s }
    sync group PortalSync { Scene, Motion, VFX }
    checkpoint BeforeCrossing at 1s restore [Scene, Motion, VFX]
  }
  branch Narrative4 at 10s { when choice("left") -> Intro otherwise -> PortalCrossing }
  cinematic playback deterministic replayable true
}
```

The example is `EX-MPTL-05002`, tier 4 (`large_integrated_examples`), class `positive`, and topic `portal_transition`. Its source identity is `sha256:44c5080a127008a3b5f6db9067dc38ad35b639323412c79cbeb066fb011d2902` and semantic identity is `sha256:e894ede9488b7cc568d25bbf5f9d20cb2846caac0e47f49bd49cba07858432c3`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

## Chapter 22: Standalone Portal Timeline Toolchain Capstone

### Purpose

Integrate authoring, validation, optimization, replay, evidence, publication, and release packaging. This chapter is anchored in `interactive_cinematic`, `checkpointed_sequence`, `r12_mcrt_lowering`. In MCRT Portal Timeline, a timeline is not merely a list of timestamps. It is an evidence-bearing state machine whose source, semantic interpretation, compiler decisions, runtime expectations, and replay receipt must remain connected.

### Learning objectives

By the end of the chapter, the reader should be able to identify the governing declarations, explain the relevant temporal invariant, trace the program into its typed AST and R12/MCRT evidence, distinguish a modeled expected result from a native runtime observation, and design at least one positive and one controlled-negative conformance case.

### Source-faithful corpus example

```mcrt
mcrt portal.timeline 0.3
module corpus.mcrt_portal_timeline.example_05004
policy no_network
metadata { timebase: 60/1 deterministic: true }
timeline Timeline05004 {
  sequence Intro { track Camera { clip FlyIn from 0s to 5s } track VFX { clip Weather from 0s to 12s } }
  sequence PortalCrossing {
    track Scene { clip OpenPortal from 0s to 4s }
    track Motion { clip Traverse from 2s to 8s }
    track VFX { clip Distortion from 1s to 9s }
    sync group PortalSync { Scene, Motion, VFX }
    checkpoint BeforeCrossing at 1s restore [Scene, Motion, VFX]
  }
  branch Narrative6 at 10s { when choice("left") -> Intro otherwise -> PortalCrossing }
  cinematic playback deterministic replayable true
}
```

The example is `EX-MPTL-05004`, tier 4 (`large_integrated_examples`), class `positive`, and topic `interactive_cinematic`. Its source identity is `sha256:66f3558ffa1f95ed6ce07656713e7c4cdf5980a3e916ea0744664a2b8d795ac0` and semantic identity is `sha256:a816983912bc24edda8b41a2f8d5f9847256af7d3adc58f20422b9f145a87af6`. The corpus expects the case to reach `runtime`. These identifiers make the lesson reproducible: a reader can locate the record, inspect its typed AST, compare compiler and runtime evidence, and verify that the script was not silently rewritten during publication.

### Technical method

Start with authoritative source declarations. Resolve every named timeline, sequence, track, clip, branch, scene binding, checkpoint, and replay target before scheduling. Normalize rational time without converting it to an uncontrolled floating representation. Then evaluate semantic preconditions: interval bounds, branch reachability, synchronization closure, portal binding completeness, checkpoint availability, and deterministic policy. Only after those gates may an optimizer trim clips, reduce keys, remove dead tracks, or lower branches. Each transform needs an equivalence receipt stating what observations are preserved: event order, marker time, branch result, scene binding, checkpoint hash, and final MCRT identity.

The typed AST is the bridge between syntax and execution. Nodes carry source spans, inferred types, effects, capability requirements, and stable IDs. The semantic judgment adds inputs, outputs, preconditions, postconditions, relation, and policy requirements. R12 lowering records authoritative state and provenance; MCRT emission records the execution-facing receipt. Native playback, when eventually available, must append its own observed trace rather than overwrite modeled expectations.

### Review lenses

**SOPHIA** tests the temporal semantics, contradictions, policy implications, and confidence of the evidence. **CHARLOTTE** reconstructs missing relationships between source, timeline graph, checkpoints, and receipts. **LANDON** turns the specification into compiler passes, runtime scheduling, validators, and Windows-safe packages. **Professor** converts the rule into a teachable sequence of definitions, worked examples, exercises, and assessment. **Podium** ensures the result is navigable, visually coherent, release-ready, and honest about modeled versus native evidence.

### Engineering checklist

- Confirm the language header, module identity, deterministic metadata, and no-network policy.
- Verify that all time values are rational, in range, and expressed in the declared timebase.
- Resolve every reference and reject ambiguous or missing bindings.
- Check interval, synchronization, branch, checkpoint, and replay invariants relevant to the chapter.
- Preserve source hash, semantic hash, AST identity, R12 identity, and MCRT identity.
- Record whether evidence is modeled, structurally validated, or natively executed.

### Laboratory

Create a new `.mcrt` program that uses the chapter topics without copying the corpus example. Produce a positive case and one deliberate negative case. For each, write an expected-stage statement, a diagnostic identity, a source hash, a compact AST sketch, and an R12/MCRT evidence outline. Run the suite validator. A native compiler is not required for the laboratory, but any structural result must be labeled separately from native playback.

### Review questions

1. Which declaration is authoritative for this chapter’s temporal behavior?
2. What contradiction or ambiguity should be rejected earliest?
3. Which observations must remain invariant under optimization?
4. What information belongs in R12, and what belongs in the MCRT receipt?
5. How would a replay hash expose drift that a visual preview might miss?

