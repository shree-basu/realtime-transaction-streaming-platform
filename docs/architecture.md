# Architecture

Source (card-auth switch) → Pub/Sub `transactions-raw`
  → Dataflow streaming job:
       validate + dead-letter · de-duplicate · enrich
       · reference side-input join · fixed + session windows
  → BigQuery: transactions, customer_spend_1m,
       customer_sessions, dead_letter

Design decisions are documented as the pipeline is built.