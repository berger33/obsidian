# Checksums e artefatos históricos para download via GitHub

> **Ressalva editorial:** os números abaixo descrevem artefatos e arquivos gerados do catálogo, não notas válidas. A auditoria atual identificou texto-template nos 1.000.000 registros virtuais do ledger. Estado atual em [`../../STATUS-CONSOLIDACAO-1M.md`](../../STATUS-CONSOLIDACAO-1M.md).

Graças à otimização com compressão LZMA2 (`.tar.xz` e `.sqlite.xz`), os artefatos principais ficaram abaixo do limite de 100 MiB por arquivo do GitHub e agora residem diretamente em `knowledge-federation/archives/`:

- `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` (`33,1 MB` — catálogo, packs, lotes, Home Vault atual e 8 notas candidatas; as candidatas aguardam revisão humana)
- `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` (`24M` — checkpoint com 1.000.000 de registros virtuais e 100 físicos)
- `knowledge-federation/archives/study-vault-1m-packs.zip` (`19M` — vault estrutural com 15.600 arquivos de nota derivados do catálogo)
- `knowledge-federation/archives/starter-vault-prioritario.zip` (`1.1M` — starter vault de inspeção; arquivos não aprovados pelo gate atual)

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
