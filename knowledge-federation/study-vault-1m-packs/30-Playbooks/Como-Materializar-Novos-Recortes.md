---
tipo: guia
status: curadoria
criado: 2026-10-01T12:35:38
tags: [playbook, ledger]
aliases: ["Playbook — Como materializar novos recortes"]
---
# Playbook — Como materializar novos recortes
## Consultar antes
```bash
python knowledge-federation/scripts/query_checkpoint.py "termo" --domain ia --limit 20
```

## Materializar
```bash
python knowledge-federation/scripts/materialize_from_checkpoint.py   --domain software   --subdomain arquitetura   --limit 500   --out checkpoint-materialized/software-arquitetura-extra   --zip archives/study-pack-software-arquitetura-extra.zip   --clean
```

## Recompilar vault
```bash
python knowledge-federation/scripts/build_study_vault.py
python knowledge-federation/scripts/enhance_study_vault.py
```
