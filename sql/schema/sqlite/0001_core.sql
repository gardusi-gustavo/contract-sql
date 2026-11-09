CREATE TABLE IF NOT EXISTS dataset_registry (
  id TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  dataset_date TEXT NOT NULL,
  path TEXT NOT NULL,
  sha256 TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ingestion_run (
  id TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  status TEXT NOT NULL,
  item_count INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_dataset_domain_date
  ON dataset_registry (domain, dataset_date);
CREATE INDEX IF NOT EXISTS idx_run_domain_started
  ON ingestion_run (domain, started_at);
