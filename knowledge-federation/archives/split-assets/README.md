# Checksums e artefatos para download via GitHub

Graças à otimização com compressão LZMA2 (`.tar.xz` e `.sqlite.xz`), os artefatos principais ficaram abaixo do limite de 100 MiB por arquivo do GitHub e agora residem diretamente em `knowledge-federation/archives/`:

- `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` (`32M` — 1.007.100 notas materializadas: vault curado + 5.000 lotes)
- `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` (`24M` — banco SQLite completo com 1.000.100 notas lógicas)
- `knowledge-federation/archives/study-vault-1m-packs.zip` (`8.4M` — vault curado de 7.100 notas)
- `knowledge-federation/archives/starter-vault-prioritario.zip` (`1.1M` — starter vault de 900 notas)

## Validação e compatibilidade

O arquivo `SHA256SUMS.txt` nesta pasta contém os hashes SHA-256 oficiais dos 4 pacotes principais.

Para validar os checksums e espelhar os arquivos em `knowledge-federation/archives/reconstructed/` (mantendo compatibilidade com fluxos que usam essa pasta):

```bash
bash knowledge-federation/scripts/reconstruct_split_assets.sh
```

## Extrair o merge completo

Diretamente de `archives/`:

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

## Onde abrir no Obsidian

Depois de extrair o merge completo, abra:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/
```

Ou copie os lotes desejados (`0001-0100` até `4901-5000`) de:

```text
MERGE-COMPLETO/10-lotes/
```
