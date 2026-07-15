"""Canonical transaction contract + validation rules (single source of truth)."""
from __future__ import annotations

# Fields that MUST be present and non-null on every event.
REQUIRED_FIELDS = (
    "transaction_id", "customer_id", "amount", "currency", "event_timestamp",
)

# Currencies we are licensed to process; anything else is dead-lettered.
SUPPORTED_CURRENCIES = frozenset({"USD", "EUR", "GBP", "INR", "SGD"})

# Hard business limits -- outside this is almost certainly bad data.
MAX_AMOUNT = 1_000_000.0
MIN_AMOUNT = 0.0

# Clean, enriched operational fact table.
TRANSACTION_BQ_SCHEMA = ",".join([
    "transaction_id:STRING", "customer_id:STRING", "amount:FLOAT",
    "currency:STRING", "event_timestamp:TIMESTAMP", "merchant_id:STRING",
    "merchant_category:STRING", "country:STRING", "channel:STRING",
    # enriched fields added by the pipeline:
    "amount_bucket:STRING", "is_international:BOOLEAN",
    "merchant_risk_tier:STRING", "ingest_timestamp:TIMESTAMP",
    "processing_date:DATE",
])