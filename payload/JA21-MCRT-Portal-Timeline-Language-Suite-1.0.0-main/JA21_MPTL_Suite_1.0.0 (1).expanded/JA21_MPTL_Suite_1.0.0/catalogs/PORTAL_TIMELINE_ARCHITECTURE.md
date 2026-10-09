# MCRT Portal Timeline Architecture

```text
MCRT Portal Timeline source (.mcrt)
        │
        ▼
Lexing → parsing → typed timeline AST
        │
        ├── temporal and rational-time validation
        ├── branch, checkpoint, and sync analysis
        ├── portal/scene binding validation
        └── deterministic no-network safety gate
        │
        ▼
Normalization and optimization
        │
        ├── clip trimming and time normalization
        ├── branch lowering and dead-track removal
        ├── key reduction with declared tolerances
        └── checkpoint and replay indexing
        │
        ▼
R12 lowering → MCRT emission → deterministic runtime trace
        │
        ▼
Timeline receipt, replay hash, diagnostics, and certification evidence
```

## Review system

- **SOPHIA** examines semantics, temporal invariants, contradictions, and risk.
- **CHARLOTTE** reconstructs source/AST/evidence relationships and missing context.
- **LANDON** owns implementation, tooling, deterministic execution, and packaging.
- **Professor** turns language rules into lessons, labs, and assessment.
- **Podium** governs publication, navigation, design consistency, and release evidence.
