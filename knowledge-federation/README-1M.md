# Knowledge Federation — 1 milhão de notas lógicas e materializadas

Este projeto atingiu **100% da meta de 1 milhão de notas**:
- **1.000.100 notas lógicas no ledger SQLite** (1.000.000 virtuais + 100 físicas iniciais).
- **1.007.100 notas materializadas consolidadas** (5.000 lotes sequenciais × 200 notas = **1.000.000 de notas sequenciais** + **7.100 notas** do vault consolidado curado).

## Estado final preservado

Merge completo materializado (1.007.100 notas representadas):

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Checkpoint principal do ledger SQLite (1.000.100 notas lógicas):

```text
knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

Ponteiro:

```text
knowledge-federation/archives/LATEST-LEDGER.txt
```

Vaults prontos para uso imediato:

```text
knowledge-federation/archives/study-vault-1m-packs.zip
knowledge-federation/archives/starter-vault-prioritario.zip
```

Relatórios e documentação:

```text
knowledge-federation/STATUS-CONSOLIDACAO-1M.md
knowledge-federation/MERGE-COMPLETO.md
knowledge-federation/LOT-SEQUENCE.md
knowledge-federation/LOTS-3301-5000.md
knowledge-federation/COMO-COPIAR-PARA-O-COFRE-OBSIDIAN.md
knowledge-federation/exports/reports/global-audit-fast.md
knowledge-federation/exports/reports/lot-sequence-manifest.json
```

## Por que não existem 1 milhão de arquivos Markdown soltos na árvore ativa?

Porque manter 1 milhão de arquivos soltos no workspace ultrapassa limites de snapshot e degrada o desempenho do Git e do Obsidian. A arquitetura final combina:

1. **Ledger SQLite compactado com LZMA2** (`ledger-v1000000-mat8000.sqlite.xz`, `24M`) para consultas e materializações sob demanda.
2. **Merge completo em stream `.tar.xz`** (`merge-completo-materializado-1m.tar.xz`, `32M`) contendo todos os 50 pacotes sequenciais (`0001-0100` a `4901-5000`, 1.000.000 de notas) e o vault curado (`7.100` notas), permitindo extrair apenas o intervalo desejado.
3. **Vaults ZIP independentes** (`study-vault-1m-packs.zip` com 7.100 notas e `starter-vault-prioritario.zip` com 900 notas) para abrir imediatamente no Obsidian.

## Restaurar o ledger SQLite

Para restaurar `knowledge-federation/registry/knowledge.sqlite` a partir do checkpoint `.sqlite.xz`:

```bash
python knowledge-federation/scripts/restore_ledger_checkpoint.py
```

Se já existir um `registry/knowledge.sqlite` e você quiser sobrescrever:

```bash
python knowledge-federation/scripts/restore_ledger_checkpoint.py --force
```

## Consultar o checkpoint diretamente (sem restaurar no workspace)

```bash
python knowledge-federation/scripts/ledger_stats.py
python knowledge-federation/scripts/query_checkpoint.py "agentes" --domain ia --limit 20
```

## Segurança em domínios regulados

As notas de `cannabis-medicinal` e `micologia` foram geradas e materializadas com `operational_content = 0` (`conteudo_operacional: false`), mantendo caráter educacional, documental, científico, regulatório e de rastreabilidade.

## Distribuição final das 1.000.000 notas virtuais

```text
software: 205.156
ia: 153.844
jogos: 153.840
cannabis-medicinal: 141.020
vibe-coding: 128.200
micologia: 115.380
negocio-carreira-produto: 102.560
```
