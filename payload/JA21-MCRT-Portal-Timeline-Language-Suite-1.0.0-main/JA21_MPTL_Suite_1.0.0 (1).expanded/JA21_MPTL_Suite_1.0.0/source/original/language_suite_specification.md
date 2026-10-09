

## 8S Coupled Mechanics Integration

This document is normalized to the **Smithson 8S Coupled Mechanics v1.0** framework. Candidate \(S^3\) fibers occupy latent penteract centers
\[
\mathbf c_n=\ell\mathbf n,\qquad \mathbf n\in\mathbb Z^5,\qquad \|\mathbf n\|_1\le M.
\]
The fifth coordinate \(t_8\) is an elucidation axis and is admitted only when
\[
\mathbf e_\perp=(I-C_4C_4^+)\mathbf e,\qquad
\eta_{\mathrm{ind}}=\frac{\|\mathbf e_\perp\|_2^2}{\|\mathbf e\|_2^2+\varepsilon}\ge\varepsilon_{\mathrm{ind}},
\]
and the held-out efficacy gain satisfies \(\Delta_{8S}=\operatorname{Score}(\mathcal M_8)-\operatorname{Score}(\mathcal M_7)>\varepsilon_{\mathrm{gain}}\).

Sparse geometric-semantic coupling and selective triadic escalation use
\[
W_{ij}=A_{ij}\exp\!\left[-\frac{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}{2\sigma_c^2}-\frac{d_J(i,j)^2}{2\sigma_J^2}\right],
\]
\[
\dot\theta_i=\omega_i+K_2\sum_jW_{ij}\sin(\theta_j-\theta_i)+K_3\sum_{j,k}H_{ijk}\sin(\theta_j+\theta_k-2\theta_i).
\]
Activation, effective support, and radius are
\[
p_i=\sigma(h_i),\qquad
s_i=p_i\kappa_i(1-\chi_i)(1-\zeta_i)v(\omega_i),\qquad
r_i=r_{\max}B_{5,\infty}(\mathbf c_i)^\alpha s_i^{1/3}.
\]
Each active site carries
\[
F_i=S^3_{r_i}=\{\mathbf y\in\mathbb R^4:\|\mathbf y\|_2=r_i\},
\]
so the noncollapsed total space is locally \(5+3=8\) dimensional.

Relation testing remains independent across latent geometry, product-state separation, visible projection, and judgement space:
\[
g^{(5)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}-(\lambda_i+\lambda_j),
\]
\[
\delta^{(8)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)+(r_i-r_j)^2},
\]
\[
g^{(3)}_{ij}=\|\Pi_5\mathbf c_i-\Pi_5\mathbf c_j\|_2-(\widehat r_i+\widehat r_j),
\qquad
g^{(J)}_{ij}=d_J(\mathfrak J_i,\mathfrak J_j)-\theta_J.
\]
R12 must retain the fifth-coordinate meaning, \(\eta_{\mathrm{ind}}\), \(W\), optional \(H\), phase, activation/support, \(g^{(5)}\), \(\delta^{(8)}\), \(g^{(3)}\), \(g^{(J)}\), projection version, uncertainty, relation class, interaction order, \(\Delta_{8S}\), provenance, and limitations.

**Example:** If \(g^{(5)}>\mathrm{tol}_5\) but \(g^{(3)}\le\mathrm{tol}_3\), record `PROJECTION_ONLY`; do not replace latent structure with visible appearance.

**Claim boundary:** this is a proposed penteract–\(S^3\) computational framework. The local dimension count is eight where the fiber is noncollapsed, but the construction is not proclaimed to be the standard sphere \(S^8\) without a separate topological proof.
## 3. MCRT Portal Timeline Language


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### 3.1 Suite profile

```text
Language: MCRT Portal Timeline Language
Profile ID: mcrt.portal.timeline
Version: 0.3
Header: mcrt portal.timeline 0.3
Namespace root: mcrt.portal.timeline
MCRT profile: PORTAL_TIMELINE_R12
Primary artifact: TimelinePackage
```

The suite represents deterministic time, sequencing, event scheduling, transitions, branching, synchronized playback, cinematic composition, checkpoint capture, replay, and seeded procedural generation.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.2 Module map

```text
mcrt.portal.timeline.timebase
mcrt.portal.timeline.sequence
mcrt.portal.timeline.track
mcrt.portal.timeline.clip
mcrt.portal.timeline.keyframe
mcrt.portal.timeline.event
mcrt.portal.timeline.transition
mcrt.portal.timeline.branch
mcrt.portal.timeline.replay
mcrt.portal.timeline.sync
mcrt.portal.timeline.cinematic
mcrt.portal.timeline.checkpoint
mcrt.portal.timeline.procedural
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.3 Timelines

A timeline owns one effective timebase, one or more sequences, and a deterministic playback state.

```mcrt
timeline PortalArrival timebase frames(60/1) {
  sequence Main from 0f to 360f {
    track camera CameraRig.Transform
    track event SceneEvents
  }
}
```

Time is normalized internally to rational ticks:

```text
TimelineTick := Rational<Int64>
```

Floating-point wall-clock values cannot become canonical timeline identity.


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### 3.4 Sequences

Sequences provide scoped intervals and nested composition.

Properties:

```yaml
sequence:
  id: SemanticId
  start: TimelineTick
  duration: TimelineTick
  priority: Int32
  mode: sequential | parallel | layered
  children: List<SequenceId>
  tracks: List<TrackId>
```

Nested sequences transform local time into parent time through a declared offset, scale, direction, and loop mode.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.5 Events

Timeline events contain a typed payload and exact schedule location.

```mcrt
event Scene.PortalOpen at 120f with {
  portal: entity_ref("ExitPortal")
  intensity: 1.0
}
```

Equal-time event ordering uses:

1. explicit priority;
2. track order;
3. stable event sequence ID.

Event delivery is ledgered before runtime dispatch so replay can reproduce the same schedule.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.6 Transitions

Transitions connect clips, sequences, states, or cinematic segments.

```mcrt
transition Intro -> PortalFlight {
  at: marker("enter_portal")
  duration: 24f
  easing: cubic.in_out
  priority: 10
}
```

A transition declares:

- source and destination;
- trigger;
- duration;
- easing;
- interruption policy;
- priority;
- state-transfer rule.

Transition cycles are permitted only when loop semantics are explicit.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.7 Branching

Branches are explicit control-flow nodes:

```mcrt
branch when scene.Player.has_key {
  then sequence UnlockPortal
  else sequence DeniedPortal
}
```

Branch conditions must be pure or reference a checkpointed deterministic state. Replay records the chosen branch and the condition evidence.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.8 Replay

Replay uses a ledger of:

```text
input events
branch decisions
random seeds
checkpoint hashes
external-state hashes
scheduled events
runtime acknowledgements
```

Replay modes:

```text
strict
verified_external
best_effort
```

Only `strict` replay may claim deterministic identity. `best_effort` must report divergences rather than silently accepting them.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.9 Synchronization

Synchronization profiles:

```text
lockstep
barrier
master_clock
sampled_follow
external_timecode
```

Canonical declaration:

```mcrt
sync PortalScene, MotionGraph, VfxGraph using lockstep {
  timebase: frames(60/1)
  barrier: end_of_frame
  timeout: disabled
}
```

Lockstep participants must share an exactly convertible timebase and deterministic step order.


Example: Two fibers sharing only q(τ) are common-drive correlated; a nonzero K A_nm term is required before the interaction is called classical coupling.

### 3.10 Cinematic playback

Cinematic tracks may target:

- cameras;
- scene transforms;
- lights and materials;
- audio cues;
- UI overlays;
- DeepML Motion parameters;
- DeepML VFX controls;
- logic-functional conditions.

Cinematic playback separates editorial sequencing from runtime provider behavior. The timeline stores exact intent, target bindings, and interpolation rules; the runtime adapter supplies rendering and audio execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.11 Checkpoint restoration

Checkpoint declarations define capture scope:

```mcrt
checkpoint PortalEntry at 118f capture {
  scene: MainPortal.runtime_state
  motion: PlayerMotion.state
  vfx: PortalEffect.simulation_state
  timeline: self.playback_state
}
```

Restoration validates:

- checkpoint semantic hash;
- package versions;
- external-resource hashes;
- state schema versions;
- participant availability;
- timebase identity.

Partial restoration requires an explicit external-state dependency declaration.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.12 Procedural timelines

Procedural generators require:

```yaml
procedural:
  generator_id: SemanticId
  seed: UInt64
  parameters: CanonicalMap
  generator_semantic_hash: Hash
  output_contract: TimelineFragmentType
```

Generated events, clips, and keyframes receive stable IDs derived from generator identity, seed, parameter hash, and generation index.


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### 3.13 Compiler assets

```text
PortalTimelineLexer
PortalTimelineParser
PortalTimelineAstBuilder
PortalTimelineNameResolver
PortalTimelineTypeChecker
TimebaseNormalizer
TimelineControlFlowValidator
TimelinePolicyGate
TimelineScheduleCompiler
TimelineOptimizer
PortalTimelineR12Lowerer
PortalTimelineMcrtEmitter
TimelineReplaySchemaEmitter
TimelinePackager
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.14 Runtime services

```text
TimelineClockService
SequenceScheduler
EventScheduler
TransitionEngine
BranchEvaluator
SynchronizationCoordinator
CheckpointService
ReplayService
ProceduralTimelineService
CinematicBindingService
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### 3.15 R12 and MCRT profile

```text
<timeline:portal_arrival.event.portal_open,
 phi_timeline_event,
 s000120,
 d4,
 rho:mcrt.portal.timeline.event.portal_open,
 operator:schedule_event,
 OMEGA_MCRT_PORTAL_TIMELINE_event,
 state:scheduled,
 error0,
 theta:120/60,
 confidence1.0000,
 status:stable>
```

```text
PORTAL_TIMELINE_R12
id=timeline:portal_arrival.event.portal_open
timeline=PortalArrival
category=event
op=schedule_event
time=120/60
priority=0
sequence=s000120
state=scheduled
confidence=1.0000
status=stable
```


Example: rho stores the 8S relation class; psi stores phase; kappa stores eta_ind/g5/delta8/g3/gJ; epsilon stores tol5/tol8/tol3/tolJ; chi stores certification and replay judgement.

### 3.16 Suite deliverables

```text
languages/mcrt_portal_timeline/
  timebase/
  timelines/
  sequences/
  events/
  transitions/
  branching/
  replay/
  synchronization/
  cinematic/
  checkpoints/
  procedural/
```

---

Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.
