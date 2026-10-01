# Merge completo — Knowledge Federation (1 Milhão de Notas + 78 Study Packs)

Data: 2026-10-01

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

O arquivo contém o merge lógico completo de **100% da meta de 1 milhão de notas materializadas + todos os 78 Study Packs por subdomínio**:

```text
MERGE-COMPLETO/00-home-vault/
MERGE-COMPLETO/00-vault-consolidado/
MERGE-COMPLETO/10-lotes/
MERGE-COMPLETO/90-ledger/
MERGE-COMPLETO/99-relatorios/
```

Inclui:

- **Home Vault mestre (`00-home-vault/`)** com `Home.md`, `Indice-Global.md`, 9 MOCs globais (`MOCs/`) e 8 Canvases (`_canvas/`);
- **Study Vault consolidado curado (`00-vault-consolidado/study-vault-1m-packs/`)** com **15.600 notas** distribuídas em **78 study packs temáticos (100% dos subdomínios da taxonomia)**, 85 MOCs, 5 trilhas guiadas, 6 playbooks/matrizes, 9 Canvases e auditoria limpa (`0` links quebrados em `93.894` links analisados);
- **50 pacotes sequenciais de lotes (`10-lotes/0001-0100/` até `10-lotes/4901-5000/`)**, expandidos dentro do TAR;
- **lotes 0001 a 5000** completos (`5.000 lotes × 200 notas`);
- **1.000.000 de notas sequenciais materializadas**;
- ponteiro do checkpoint ledger (`LATEST-LEDGER.txt`) dentro de `90-ledger/` (o banco compactado `ledger-v1000000-mat8000.sqlite.xz` de `24M` fica ao lado em `knowledge-federation/archives/`);
- todos os 50 relatórios de execução de lotes, auditorias, manifestos e índices em `99-relatorios/`.

## Totais representados

```text
Study packs curados (100% dos subdomínios): 78
Notas do vault curado: 15.600 notas
Pacotes sequenciais: 50
Lotes sequenciais: 5.000
Notas sequenciais: 1.000.000
Total materializado representado: 1.015.600 notas
Entradas totais no TAR: 1.021.127
Lotes em domínios regulados: 1.288
Conteúdo operacional regulado: 0
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

O script `knowledge-federation/scripts/build_full_merge_from_ledger.py` gera o arquivo `.tar.xz` completo diretamente do checkpoint SQLite e do Study Vault curado, sem criar arquivos intermediários no workspace:

```bash
python3 knowledge-federation/scripts/build_full_merge_from_ledger.py
```

## Como extrair

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Para extrair apenas o vault curado ou apenas um intervalo de lotes (recomendado para não criar 1 milhão de arquivos soltos de uma só vez no disco):

```bash
# Extrair apenas o vault consolidado curado (78 study packs / 15.600 notas)
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/00-vault-consolidado

# Extrair apenas um intervalo específico de 100 lotes (20.000 notas), ex.: 4901-5000
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/10-lotes/4901-5000
```
