# Split assets para download via GitHub

Os artefatos principais excedem o limite de 100 MiB por arquivo do GitHub. Por isso, eles foram divididos em partes menores versionáveis.

## Arquivos divididos

### Merge completo

```text
merge-completo-materializado-1m.tar.xz.part-000
merge-completo-materializado-1m.tar.xz.part-001
merge-completo-materializado-1m.tar.xz.part-002
```

Reconstruir:

```bash
cat merge-completo-materializado-1m.tar.xz.part-* > merge-completo-materializado-1m.tar.xz
sha256sum -c SHA256SUMS.txt --ignore-missing
```

Extrair:

```bash
tar -xJf merge-completo-materializado-1m.tar.xz
```

### Ledger/checkpoint

```text
ledger-v1000000-mat8000.zip.part-000
ledger-v1000000-mat8000.zip.part-001
ledger-v1000000-mat8000.zip.part-002
```

Reconstruir:

```bash
cat ledger-v1000000-mat8000.zip.part-* > ledger-v1000000-mat8000.zip
sha256sum -c SHA256SUMS.txt --ignore-missing
```

## Onde abrir no Obsidian

Depois de extrair o merge completo, abra:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/
```

Ou copie os lotes desejados de:

```text
MERGE-COMPLETO/10-lotes/
```
