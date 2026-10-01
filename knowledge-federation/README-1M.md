# Knowledge Federation — 1 milhão de notas lógicas e materializadas

Este projeto atingiu **100% da meta de 1 milhão de notas**:
- **1.000.100 notas lógicas no ledger SQLite** (`1.000.000` virtuais + `100` físicas iniciais).
- **1.015.600 notas materializadas consolidadas** (`5.000 lotes sequenciais × 200 notas = 1.000.000 de notas sequenciais` + `78 study packs × 200 notas = 15.600 notas curadas`).

## Estado final preservado

Merge completo materializado (`1.015.600 notas` representadas, `34M`):

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Checkpoint principal do ledger SQLite (`1.000.100 notas lógicas`, `24M`):

```text
knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

Vaults prontos para uso imediato:

```text
knowledge-federation/archives/study-vault-1m-packs.zip       (19M — 78 packs / 15.600 notas)
knowledge-federation/archives/starter-vault-prioritario.zip  (1.1M — 900 notas prioritárias)
knowledge-federation/00-home-vault/                          (Home Vault Mestre com 9 MOCs e 8 Canvases)
```

## Restaurar o ledger SQLite

```bash
python knowledge-federation/scripts/restore_ledger_checkpoint.py
```

## Consultar o checkpoint diretamente (sem restaurar no workspace)

```bash
python knowledge-federation/scripts/ledger_stats.py
python knowledge-federation/scripts/query_checkpoint.py "agentes" --domain ia --limit 20
```

## Regerar os 78 Study Packs, o Home Vault e o Merge Completo

```bash
python knowledge-federation/scripts/build_all_78_study_packs.py
python knowledge-federation/scripts/build_pack_inventory.py
python knowledge-federation/scripts/build_global_indexes.py
python knowledge-federation/scripts/build_full_merge_from_ledger.py
```

## Distribuição final das 1.000.000 notas virtuais

```text
software: 205.156 (16 subdomínios)
ia: 153.844 (12 subdomínios)
jogos: 153.840 (12 subdomínios)
cannabis-medicinal: 141.020 (11 subdomínios)
vibe-coding: 128.200 (10 subdomínios)
micologia: 115.380 (9 subdomínios)
negocio-carreira-produto: 102.560 (8 subdomínios)
```
