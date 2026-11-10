# contract-sql

Relational contract: canonical DDL, migrations, indexing blueprints, and query patterns.
Application data, seeds, and domain datasets stay in `database-*`.

## Layout

| Path | Holds |
| --- | --- |
| `schemas/sqlite/` | SQLite DDL |
| `schemas/postgres/` | PostgreSQL DDL |
| `migrations/` | migration conventions and templates |
| `queries/` | indexing and analytical query blueprints |
| `tests/` | schema and dialect smoke tests |
| `docs/` | usage and versioning |

## Validation

```bash
bash infra/scripts/ci.sh
```

## Rules

- Public package only.
- No application data, secrets, or personal data.
- Versioned by tag.
