

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

### 3.1 Profile

```text
Language name: MCRT Portal Timeline Language
Profile ID: mcrt.portal.timeline
Header: mcrt portal.timeline 0.3
MCRT profile: PORTAL_TIMELINE_R12
Primary namespace: mcrt.portal.timeline
```

This language expresses deterministic timelines, tracks, clips, keyframes, events, transitions, branches, checkpoints, replay, synchronization, and procedural sequence generation.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.2 Lexical keywords

```text
timeline timebase fps tickrate track clip keyframe marker event transition branch
checkpoint replay sync group sequence parallel serial at from to duration offset
loop repeat hold ease linear step bezier cubic spring condition else target property
sample procedural generator seed restore capture mute solo weight layer priority
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.3 Parser grammar

```ebnf
timelineProgram = "mcrt", "portal.timeline", version,
                  metadataBlock,
                  { importDecl | policyDecl | annotation | timelineDecl } ;
metadataBlock   = "metadata", objectLiteral ;

timelineDecl    = annotationList, "timeline", identifier,
                  [ timelineParams ], timelineBlock ;
timelineParams  = "(", [ namedArguments ], ")" ;
timelineBlock   = "{", { timelineMember }, "}" ;
timelineMember  = timebaseDecl | trackDecl | markerDecl | transitionDecl
                | branchDecl | checkpointDecl | syncDecl | replayDecl
                | timelineStatement ;

timebaseDecl    = ( "timebase", timebaseExpr
                  | "fps", numberLiteral
                  | "tickrate", numberLiteral ), ";" ;
timebaseExpr    = durationLiteral | qualifiedName ;

trackDecl       = annotationList, "track", trackKind, identifier,
                  [ "target", expression ], trackBlock ;
trackKind       = "property" | "animation" | "audio" | "event" | "camera"
                | "logic" | "model" | qualifiedName ;
trackBlock      = "{", { clipDecl | keyframeDecl | timelineStatement }, "}" ;

clipDecl        = annotationList, "clip", identifier,
                  "from", timeExpr, "to", timeExpr,
                  [ "source", expression ], [ clipOptions ], clipBlockOpt ;
clipOptions     = "(", [ namedArguments ], ")" ;
clipBlockOpt    = [ "{", { keyframeDecl | timelineStatement }, "}" ] ;

keyframeDecl    = "keyframe", timeExpr, ":", expression,
                  [ "ease", easingExpr ], ";" ;
markerDecl      = "marker", identifier, "at", timeExpr, ";" ;
eventDecl       = "event", qualifiedName, "at", timeExpr,
                  [ argumentList ], ";" ;

transitionDecl  = "transition", stateRef, "->", stateRef,
                  [ "when", expression ],
                  [ "duration", durationLiteral ],
                  [ "ease", easingExpr ], ";" ;
branchDecl      = "branch", identifier, "when", expression, timelineBlock,
                  [ "else", timelineBlock ] ;
checkpointDecl  = "checkpoint", identifier, "at", timeExpr,
                  [ "capture", expression ], ";" ;
syncDecl        = "sync", "group", identifier,
                  "[", qualifiedName, { ",", qualifiedName }, "]",
                  [ "mode", syncMode ], ";" ;
replayDecl      = "replay", identifier,
                  "from", checkpointRef,
                  [ "to", timeExpr ], [ "seed", integerLiteral ], ";" ;

sequenceDecl    = "sequence", ( "parallel" | "serial" ), identifier,
                  timelineBlock ;
proceduralDecl  = "procedural", identifier,
                  [ parameterList ], "using", qualifiedName,
                  [ "seed", integerLiteral ], ";" ;

timelineStatement
                = eventDecl | sequenceDecl | proceduralDecl | scheduleStmt
                | restoreStmt | sampleStmt | corpusStatement ;
scheduleStmt    = "schedule", expression, "at", timeExpr, ";" ;
restoreStmt     = "restore", checkpointRef, ";" ;
sampleStmt      = "sample", expression, "at", timeExpr,
                  [ "as", typeRef ], ";" ;

timeExpr        = durationLiteral | timeLiteral | frameExpr | markerRef
                | timeExpr, ( "+" | "-" ), durationLiteral ;
frameExpr       = integerLiteral, "frame" ;
markerRef       = "marker", qualifiedName ;
checkpointRef   = qualifiedName ;
stateRef        = qualifiedName ;
easingExpr      = "linear" | "step" | "cubic" | "bezier", argumentList
                | "spring", argumentList | qualifiedName ;
syncMode        = "lockstep" | "leader" | "resample" ;
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.4 AST rules

Required nodes:

```text
PortalTimelineProgramNode
TimelineDeclNode
TimebaseDeclNode
TrackDeclNode
ClipDeclNode
KeyframeDeclNode
MarkerDeclNode
TimelineEventNode
TransitionDeclNode
BranchDeclNode
CheckpointDeclNode
SyncGroupDeclNode
ReplayDeclNode
SequenceDeclNode
ProceduralDeclNode
ScheduleStmtNode
RestoreStmtNode
SampleStmtNode
TimeExprNode
EasingExprNode
```

AST constraints:

- All time expressions normalize to rational timeline ticks.
- Source time literals remain attached for round-trip formatting.
- Keyframes carry canonical sequence numbers for equal-time ordering.
- Branches create explicit control-flow nodes.
- Parallel sequences create explicit synchronization joins.
- Procedural generators record seed and generator semantic hash.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.5 Semantic operator mapping

| Construct | Operator | Omega family |
|---|---|---|
| `timeline` | `declare_timeline` | `OMEGA_MCRT_PORTAL_TIMELINE_declare` |
| `track` | `declare_track` | `OMEGA_MCRT_PORTAL_TIMELINE_track` |
| `clip` | `schedule_clip` | `OMEGA_MCRT_PORTAL_TIMELINE_clip` |
| `keyframe` | `set_keyframe` | `OMEGA_MCRT_PORTAL_TIMELINE_keyframe` |
| `event` | `schedule_event` | `OMEGA_MCRT_PORTAL_TIMELINE_event` |
| `transition` | `declare_transition` | `OMEGA_MCRT_PORTAL_TIMELINE_transition` |
| `branch` | `branch_timeline` | `OMEGA_MCRT_PORTAL_TIMELINE_branch` |
| `checkpoint` | `capture_checkpoint` | `OMEGA_MCRT_PORTAL_TIMELINE_checkpoint` |
| `replay` | `replay_timeline` | `OMEGA_MCRT_PORTAL_TIMELINE_replay` |
| `sync` | `synchronize_timeline` | `OMEGA_MCRT_PORTAL_TIMELINE_sync` |
| `sample` | `sample_timeline` | `OMEGA_MCRT_PORTAL_TIMELINE_sample` |


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.6 Semantic constraints

1. A timeline declares exactly one effective timebase.
2. Every time expression must convert exactly or through a declared resampling policy.
3. Clip end time must be greater than or equal to start time.
4. Keyframes in a property track must have type-compatible values.
5. Equal-time keyframes require deterministic source-order or explicit priority.
6. Transition graphs may contain cycles only when cycle semantics are declared.
7. A checkpoint name is unique in its timeline.
8. Replay from a checkpoint requires complete captured state or an explicit external-state dependency.
9. Procedural generation requires an explicit seed under deterministic policy.
10. Lockstep synchronization rejects incompatible timebases.
11. Branch conditions must be side-effect free unless a runtime profile explicitly permits effects.
12. A timeline cannot schedule an event before zero unless its timebase supports preroll.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.7 Typing rules

- Track target type determines keyframe value type.
- `Timecode` values are converted through the timeline timebase.
- `Curve<T>` requires interpolatable `T`; discrete types permit only step easing.
- Event track arguments must match the event signature.
- A model track target must type as a DeepML model input or control parameter.
- Checkpoint capture expression must be serializable.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.8 Optimization rules

Permitted:

- rational time normalization;
- removal of redundant identical keyframes;
- adjacent constant-segment coalescing;
- curve precomputation;
- clip interval indexing;
- deterministic event bucketing;
- static branch pruning when the condition is constant;
- parallel schedule dependency analysis;
- checkpoint delta compression with hash verification.

Prohibited:

- changing equal-time event order;
- approximating a curve outside declared tolerance;
- removing a checkpoint referenced by replay;
- changing transition priority;
- resampling without a declared mode;
- evaluating an effectful branch condition early.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### 3.9 Validation rules

Minimum conformance cases:

- minimal timeline with timebase;
- frame and duration conversion;
- incompatible timebase rejection;
- clip negative-duration rejection;
- keyframe type mismatch;
- deterministic equal-time ordering;
- transition cycle validation;
- unseeded procedural rejection;
- checkpoint/replay round trip;
- lockstep sync pass and failure;
- branch replay determinism;
- curve optimization equivalence.

---

Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.
