# Merge completo — Knowledge Federation (1 Milhão de Notas Consolidadas)

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
6df88bc1cef2df18a7a3df7d1e96a70bd80c04630295693350d7a72db3ad3429
```

Tamanho compactado:

```text
32M
```

## O que foi mesclado

O arquivo contém o merge lógico completo de **100% da meta de 1 milhão de notas materializadas**:

```text
MERGE-COMPLETO/00-vault-consolidado/
MERGE-COMPLETO/10-lotes/
MERGE-COMPLETO/90-ledger/
MERGE-COMPLETO/99-relatorios/
```

Inclui:

- vault consolidado curado com **7.100 notas** (36 study packs temáticos, trilhas, playbooks, matrizes, canvas e auditoria);
- **50 pacotes sequenciais de lotes** (`0001-0100` até `4901-5000`), expandidos dentro do TAR;
- **lotes 0001 a 5000** completos (`5.000 lotes × 200 notas`);
- **1.000.000 de notas sequenciais materializadas**;
- ponteiro do checkpoint ledger (`LATEST-LEDGER.txt`) dentro de `90-ledger/` (o banco compactado `ledger-v1000000-mat8000.sqlite.xz` de 24M fica ao lado em `knowledge-federation/archives/`);
- todos os 50 relatórios de execução de lotes, manifestos e índices em `99-relatorios/`.

## Totais representados

```text
Vault curado: 7.100 notas
Pacotes sequenciais: 50
Lotes sequenciais: 5.000
Notas sequenciais: 1.000.000
Total materializado representado: 1.007.100 notas
Entradas no TAR: 1.012.505
Lotes em domínios regulados: 1.288
Conteúdo operacional regulado: 0
```

## Integridade

Validações executadas:

```text
xz -t knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Resultado: `OK`.

Listagem completa das entradas do TAR:

```text
tar_entries=1012505
```

## Otimização de tamanho e persistência

Ao armazenar o ledger SQLite separadamente com compressão LZMA2 (`knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz`, `24M`) e consolidar todos os `1.007.100` arquivos Markdown diretamente no stream `.tar.xz` (`32M`), ambos os artefatos ficaram abaixo do limite de 100 MiB por arquivo do GitHub e mantiveram o repositório inteiro em ~77 MB (dentro do limite seguro de snapshot).

Depois do merge validado, os 50 zips sequenciais intermediários (`study-vault-next-100-lotes.zip` e `study-vault-lotes-101-200.zip` até `study-vault-lotes-4901-5000.zip`) foram podados.

Registro da poda:

```text
knowledge-federation/archives/pruned-after-merge/sequential-zips-pruned.txt
```

Os conteúdos desses 50 pacotes estão integralmente preservados dentro do merge completo em:

```text
MERGE-COMPLETO/10-lotes/0001-0100/
...
MERGE-COMPLETO/10-lotes/4901-5000/
```

## Como extrair

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Para extrair apenas o vault curado ou apenas um intervalo de lotes (recomendado para não criar 1 milhão de arquivos soltos de uma só vez no disco):

```bash
# Extrair apenas o vault consolidado curado (7.100 notas)
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/00-vault-consolidado

# Extrair apenas um intervalo específico de 100 lotes (20.000 notas), ex.: 3301-3400
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/10-lotes/3301-3400
```

## Como abrir no Obsidian

Após extrair, abra uma destas pastas como vault:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/
```

Ou abra qualquer um dos 50 intervalos de lotes em:

```text
MERGE-COMPLETO/10-lotes/0001-0100/
MERGE-COMPLETO/10-lotes/0101-0200/
...
MERGE-COMPLETO/10-lotes/4901-5000/
```

Cada intervalo contém `00-Inicio/Home.md`, 100 MOCs, Canvas e 20.000 notas interligadas.

## Segurança

Conteúdos de cannabis medicinal e micologia permanecem educacionais, documentais e não operacionais. O material usa `conteudo_operacional: false` e aviso de domínio regulado para orientar uso seguro: estudo, rastreabilidade, documentação e perguntas para profissionais habilitados.
