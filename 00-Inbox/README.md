# Inbox

Landing zone for the ingestion pipeline. Nothing in here is trusted or linked yet.

- `papers/` — PDFs fetched by the sweep (filename: `AuthorYear-ShortTitle.pdf`).
- One stub markdown file per fetched paper (same basename), with frontmatter `status: inbox` and the paper's metadata (title, authors, year, abstract, URL).

**Flow:** sweep writes stubs here → you review and delete rejects → the extractor turns keepers into literature notes in `10-Literature/` → a Claude Code refinement pass extracts atoms into `20-Atoms/` and links them → the stub is removed.

An empty inbox is the goal state.
