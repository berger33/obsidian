# Knowledge Federation — 1 milhão de notas lógicas

Este projeto atingiu o marco de **1.000.100 notas lógicas** usando arquitetura **ledger-first**.

## Estado final preservado

Checkpoint principal:

```text
knowledge-federation/archives/ledger-v1000000-mat8000.zip
```

Ponteiro:

```text
knowledge-federation/archives/LATEST-LEDGER.txt
```

Relatório:

```text
knowledge-federation/exports/reports/global-audit-fast.md
```

Pacote de estudo materializado:

```text
knowledge-federation/archives/materialized-study-pack-vscale4.zip
```

## Por que não existem 1 milhão de arquivos Markdown ativos?

Porque isso não é confiável neste ambiente. A estratégia correta é:

```text
1 nota = 1 registro no SQLite
Markdown = materialização sob demanda
```

Assim o vault pode ter escala de 1 milhão de notas lógicas sem explodir o número de arquivos ativos.

## Restaurar o ledger

O SQLite ativo foi removido depois do checkpoint para manter o workspace leve. Para restaurar:

```bash
python knowledge-federation/scripts/restore_ledger_checkpoint.py
```

Se já existir um `registry/knowledge.sqlite` e você quiser sobrescrever:

```bash
python knowledge-federation/scripts/restore_ledger_checkpoint.py --force
```

## Consultar o ledger

Depois de restaurar:

```bash
python knowledge-federation/scripts/query_ledger.py "agentes" --virtual --limit 20
python knowledge-federation/scripts/query_ledger.py --domain cannabis-medicinal --virtual --limit 20
python knowledge-federation/scripts/query_ledger.py --domain software --subdomain backend --virtual --limit 20
```

## Materializar um recorte para Obsidian

Depois de restaurar o ledger:

```bash
python knowledge-federation/scripts/materialize_batch.py --domain software --prefix vscale4 --limit 1000
python knowledge-federation/scripts/materialize_batch.py --domain ia --prefix vscale4 --limit 1000
```

As notas materializadas aparecerão em:

```text
knowledge-federation/materialized/
```

## Criar novo checkpoint depois de materializar

```bash
python knowledge-federation/scripts/checkpoint_virtual.py --label novo-recorte --prune-materialized
```

## Segurança em domínios regulados

As notas virtuais de `cannabis-medicinal` e `micologia` foram geradas com `operational_content = 0`, isto é: conteúdo educacional, médico/legal/científico e não operacional. O pipeline evita instruções operacionais de cultivo, extração ou produção de substâncias controladas.

## Distribuição final das notas virtuais

```text
software: 205.156
ia: 153.844
jogos: 153.840
cannabis-medicinal: 141.020
vibe-coding: 128.200
micologia: 115.380
negocio-carreira-produto: 102.560
```
