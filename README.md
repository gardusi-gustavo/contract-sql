# package-sql

Pure SQL schema and migration registry.

## Layout

| `sql/schema/sqlite/` | SQLite DDL |
| `sql/schema/postgres/` | PostgreSQL DDL |
| `sql/migrations/` | migration conventions |

## Validation

```bash
bash infra/scripts/ci.sh
```

## Rules

- Public contract/asset package only.
- No application data, secrets, or personal data.
- Versioned by tag.
