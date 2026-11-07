---
name: phantom-sovereign-guard
description: Private cloud sensitive document security audit and zero-residue privacy indexing for UGOS NAS. Use when users need to inspect local private documents for privacy compliance, organize sensitive files, or build a local secure knowledge index.
---

# Goal

Provide automated privacy compliance inspection, sensitive document categorization, and secure local indexing for private cloud storage on UGOS NAS.

Detailed security standards and empty result rules are documented in [Privacy Audit Protocol](references/privacy-audit-protocol.md).

# Required input

Collect user-specified target directory path and privacy scanning sensitivity options.

# Generation-time capability evidence

- `ug-filesystem` → `file-agent`
- `ug-document` → `document-agent`
- `ug-knowledge` → `knowledge-agent`

# Orchestration

The orchestration coordinates registered NAS agents in strict sequential order:

1. Scan target directory:
   `delegate --target file-agent --instruction 'Scan target directory for document files and list metadata'`
   If the scan produces an empty result with zero matches, stop the workflow and report no results found.

2. Parse document contents:
   Pass the real result from the upstream file scan to document analysis:
   `delegate --target document-agent --instruction 'Extract text and sensitive classification metadata from verified document paths'`

3. Index into local knowledge base:
   Pass the real result from upstream document extraction to downstream indexing:
   `delegate --target knowledge-agent --instruction 'Index verified privacy-compliant document records into local private knowledge base'`

# Completion and failure

Handle all delegation lifecycle states:
- `completed`: All target documents processed and indexed successfully.
- `failed`: An agent encountered an execution error; report failure reason and stop dependent steps.
- `cancelled`: User requested cancellation; terminate downstream tasks cleanly.
- `waiting_user`: Missing required path; prompt user for confirmation.
- `waiting_approval`: Modification or index creation requires user confirmation before proceeding.
