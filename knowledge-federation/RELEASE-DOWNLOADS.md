# Links de download da entrega completa (1 Milhão de Notas Consolidadas)

Data: 2026-10-01

## Link para baixar tudo do GitHub

Baixe a branch consolidada inteira como ZIP:

```text
https://github.com/berger33/obsidian/archive/refs/heads/arena/01a0f8f9-obsidian.zip
```

Ou veja a branch no GitHub:

```text
https://github.com/berger33/obsidian/tree/arena/01a0f8f9-obsidian
```

*(Após o merge do Pull Request em `main`, o download direto da `main` também estará disponível em `https://github.com/berger33/obsidian/archive/refs/heads/main.zip`.)*

## Arquivos principais prontos em `knowledge-federation/archives/`

Com a otimização LZMA2 (`.tar.xz` e `.sqlite.xz`), nenhum arquivo excede 100 MiB e todos estão prontos para uso direto sem precisar concatenar partes:

| Arquivo | Tamanho | SHA-256 | Descrição |
|---|---:|---|---|
| `merge-completo-materializado-1m.tar.xz` | 32M | `6df88bc1cef2df18a7a3df7d1e96a70bd80c04630295693350d7a72db3ad3429` | Merge completo com **1.007.100 notas materializadas** (7.100 do vault curado + 5.000 lotes / 1.000.000 de notas sequenciais). |
| `ledger-v1000000-mat8000.sqlite.xz` | 24M | `b824467e32b188b7cf7aad57161938fa2417f8a46193524cc26a5d0c7e460c85` | Banco SQLite completo com 1.000.000 de notas virtuais + 100 físicas. |
| `study-vault-1m-packs.zip` | 8.4M | `4ea41e71dac184b9d2adf35889eebd724596fd40b2c8d69d4fde81ab8d656986` | Vault Obsidian curado pronto para abrir (7.100 notas, 36 packs, trilhas, playbooks, canvas). |
| `starter-vault-prioritario.zip` | 1.1M | `a60001c716653916ff5d87a357c57d4cdc403a6eb992f063a02b3ffbf3198fd7` | Starter vault prioritário leve (900 notas). |

## Validar checksums / compatibilidade com `reconstruct_split_assets.sh`

No root do repositório:

```bash
bash knowledge-federation/scripts/reconstruct_split_assets.sh
```

O script valida os hashes SHA-256 em `knowledge-federation/archives/split-assets/SHA256SUMS.txt` e espelha os artefatos em `knowledge-federation/archives/reconstructed/` para manter compatibilidade com os comandos anteriores.

## Copiar para o cofre Obsidian

Guia passo a passo:

```text
knowledge-federation/COMO-COPIAR-PARA-O-COFRE-OBSIDIAN.md
```

Para extrair o merge completo:

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Abra no Obsidian ou copie para seu cofre:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/
```

Ou copie intervalos específicos de 100 lotes (`0001-0100` a `4901-5000`) de:

```text
MERGE-COMPLETO/10-lotes/
```
