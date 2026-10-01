# Merge histórico — Knowledge Federation (inventário de 1 milhão + 78 Study Packs)

Data: 2026-10-01

> **Ressalva de qualidade:** as contagens deste pacote representam entradas, arquivos e registros gerados. A auditoria atual identificou marcadores de texto-template em todos os 1.000.000 registros virtuais do checkpoint. Não contar esses arquivos como 1 milhão de notas válidas. Consulte [`STATUS-CONSOLIDACAO-1M.md`](STATUS-CONSOLIDACAO-1M.md) e [`exports/reports/note-quality-audit.md`](exports/reports/note-quality-audit.md).

## Entrega principal

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Checksum:

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz.sha256
```

SHA-256:

```text
ae692de0c8d48683de2d26a3b0ad638ea9bb0b47aa7b36ca7ae9940e5537217c
```

Tamanho compactado:

```text
34M
```

## O que foi mesclado

O arquivo contém um merge histórico com os artefatos e as entradas produzidas pela estratégia de inventário/materialização em escala. Os totals não expressam validação editorial:

```text
MERGE-COMPLETO/00-home-vault/
MERGE-COMPLETO/00-vault-consolidado/
MERGE-COMPLETO/10-lotes/
MERGE-COMPLETO/90-ledger/
MERGE-COMPLETO/99-relatorios/
```

Inclui:

- **Home Vault mestre (`00-home-vault/`)** com `Home.md`, `Indice-Global.md`, 9 MOCs globais (`MOCs/`) e 8 Canvases (`_canvas/`);
- **Study Vault histórico (`00-vault-consolidado/study-vault-1m-packs/`)** com **15.600 arquivos de nota** em 78 Study Packs, além de MOCs, trilhas, playbooks, Canvases e auditoria estrutural de links. A auditoria de links não verifica se o corpo tem conteúdo substantivo;
- **50 pacotes sequenciais de lotes (`10-lotes/0001-0100/` até `10-lotes/4901-5000/`)**, expandidos dentro do TAR;
- **lotes 0001 a 5000** representados (`5.000 lotes × 200 arquivos`);
- **1.000.000 de arquivos sequenciais materializados** a partir dos registros do ledger; não são 1.000.000 de notas validadas;
- ponteiro do checkpoint ledger (`LATEST-LEDGER.txt`) dentro de `90-ledger/` (o banco compactado `ledger-v1000000-mat8000.sqlite.xz` de `24M` fica ao lado em `knowledge-federation/archives/`);
- todos os 50 relatórios de execução de lotes, auditorias, manifestos e índices em `99-relatorios/`.

## Totais representados

```text
Study packs no pacote: 78
Arquivos de nota nos Study Packs: 15.600
Pacotes sequenciais: 50
Lotes sequenciais: 5.000
Arquivos sequenciais materializados: 1.000.000
Arquivos de nota representados (sem MOCs/relatórios): 1.015.600
Entradas totais no TAR: 1.021.127
Notas válidas aprovadas por revisão humana no checkpoint: 0
Conteúdo operacional regulado marcado no ledger: 0
```

## Integridade

Validações executadas:

```text
xz -t knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Resultado: `OK`.

Contagem total das entradas do TAR:

```text
tar_entries=1021127
```

## Como regerar o merge completo a partir do ledger

O script `knowledge-federation/scripts/build_full_merge_from_ledger.py` apenas permite recriar o TAR histórico se houver opt-in explícito. Isso agrega arquivos-placeholder e **não** gera notas válidas; o comando pode substituir o arquivo de saída existente. Use somente para recuperação/inspeção:

```bash
python3 knowledge-federation/scripts/build_full_merge_from_ledger.py --allow-catalog-stubs
```

## Como extrair

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Para extrair apenas o vault curado ou apenas um intervalo de lotes (recomendado para não criar 1 milhão de arquivos soltos de uma só vez no disco):

```bash
# Extrair apenas o vault estrutural (78 packs / arquivos-placeholder)
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/00-vault-consolidado

# Extrair apenas um intervalo específico de 100 lotes (20.000 arquivos-placeholder), ex.: 4901-5000
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/10-lotes/4901-5000
```
