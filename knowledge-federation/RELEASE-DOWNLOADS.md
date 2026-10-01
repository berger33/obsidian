# Downloads dos artefatos históricos do merge

Data: 2026-10-01

> Os tamanhos e contagens abaixo descrevem arquivos/registros materializados. A auditoria atual encontrou texto-template nos 1.000.000 registros virtuais do ledger; não interprete esses pacotes como 1 milhão de notas válidas. Estado e critérios: [`STATUS-CONSOLIDACAO-1M.md`](STATUS-CONSOLIDACAO-1M.md).

## Link para baixar tudo do GitHub

Baixe a branch consolidada inteira como ZIP:

```text
https://github.com/berger33/obsidian/archive/refs/heads/arena/01a0f8f9-obsidian.zip
```

Ou veja a branch e o Pull Request no GitHub:

```text
https://github.com/berger33/obsidian/tree/arena/01a0f8f9-obsidian
https://github.com/berger33/obsidian/pull/2
```

*(Após o merge do Pull Request em `main`, o download direto da `main` também estará disponível em `https://github.com/berger33/obsidian/archive/refs/heads/main.zip`.)*

## Arquivos principais prontos em `knowledge-federation/archives/`

Com a otimização LZMA2 (`.tar.xz` e `.sqlite.xz`), nenhum arquivo excede 100 MiB e todos estão versionados diretamente no Git, prontos para uso sem precisar concatenar partes:

| Arquivo | Tamanho | SHA-256 | Descrição |
|---|---:|---|---|
| `merge-completo-materializado-1m.tar.xz` | `34M` | `ae692de0c8d48683de2d26a3b0ad638ea9bb0b47aa7b36ca7ae9940e5537217c` | Merge histórico com arquivos dos 78 packs e 5.000 lotes. Contagens são de arquivo/registro, não de conteúdo validado. |
| `ledger-v1000000-mat8000.sqlite.xz` | `24M` | `b824467e32b188b7cf7aad57161938fa2417f8a46193524cc26a5d0c7e460c85` | SQLite com 1.000.000 de registros virtuais de catálogo + 100 registros físicos iniciais; auditoria detectou template nos registros virtuais. |
| `study-vault-1m-packs.zip` | `19M` | `36861d71866d59b1aa4e4fb227f36fe004b81aff2f90765dd4d7652d3dc5e17a` | Pacote Obsidian com 15.600 arquivos distribuídos em 78 packs; estrutura e links não certificam validade editorial. |
| `starter-vault-prioritario.zip` | `1.1M` | `a60001c716653916ff5d87a357c57d4cdc403a6eb992f063a02b3ffbf3198fd7` | Starter vault prioritário leve (900 notas). |

## Validar checksums / compatibilidade com `reconstruct_split_assets.sh`

No root do repositório:

```bash
bash knowledge-federation/scripts/reconstruct_split_assets.sh
```

O script valida os hashes SHA-256 em `knowledge-federation/archives/split-assets/SHA256SUMS.txt` e espelha os artefatos em `knowledge-federation/archives/reconstructed/`.

## Copiar para o cofre Obsidian

Guia passo a passo:

```text
knowledge-federation/COMO-COPIAR-PARA-O-COFRE-OBSIDIAN.md
```

Para extrair o merge completo:

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```
