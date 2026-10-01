# Como copiar para o cofre Obsidian (Consolidação Final — 1 Milhão de Notas + 78 Study Packs)

Data: 2026-10-01

Este guia explica como baixar a entrega completa do GitHub, validar os arquivos e abrir ou copiar o conteúdo para seu cofre Obsidian.

## 1. Baixar a branch atual (ou `main` após merge)

Baixe o ZIP completo da branch consolidada com 1 milhão de notas materializadas:

```text
https://github.com/berger33/obsidian/archive/refs/heads/arena/01a0f8f9-obsidian.zip
```

Depois que o PR (#2) for mergeado em `main`, o link principal será:

```text
https://github.com/berger33/obsidian/archive/refs/heads/main.zip
```

## 2. Descompactar o ZIP baixado

Ao descompactar, entre na pasta do repositório pelo terminal:

```bash
cd obsidian-arena-01a0f8f9-obsidian
```

## 3. Arquivos prontos para uso direto (sem necessidade de juntar partes)

Graças à compressão LZMA2 (`.tar.xz` e `.sqlite.xz`), todos os arquivos principais têm até `34M` cada e já estão versionados diretamente em `knowledge-federation/archives/`:

- `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` (`34M` — contém **1.015.600 notas materializadas**: `15.600` notas do vault curado em `78` packs + `5.000` lotes / `1.000.000` de notas sequenciais + `00-home-vault`)
- `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` (`24M` — banco SQLite completo com 1.000.000 de notas virtuais + 100 físicas)
- `knowledge-federation/archives/study-vault-1m-packs.zip` (`19M` — vault curado com **15.600 notas**, **78 packs / 100% dos subdomínios**, 85 MOCs, 5 trilhas, 6 playbooks e 9 Canvases)
- `knowledge-federation/archives/starter-vault-prioritario.zip` (`1.1M` — vault rápido com 900 notas prioritárias)

Se quiser validar os checksums SHA-256:

```bash
bash knowledge-federation/scripts/reconstruct_split_assets.sh
```

## 4. Opção A (Recomendada para começar já): Abrir o Vault Curado de 78 Subdomínios (15.600 notas)

Descompacte:

```bash
unzip knowledge-federation/archives/study-vault-1m-packs.zip -d study-vault-1m-packs
```

No Obsidian, clique em **Open folder as vault** e selecione a pasta `study-vault-1m-packs`. Comece por `00-Inicio/Home.md`.

## 5. Opção B: Extrair do Merge Completo de 1 Milhão de Notas

Para extrair apenas um intervalo específico de 100 lotes (20.000 notas) sem criar 1 milhão de arquivos de uma vez no seu disco:

```bash
# Exemplo: extrair os lotes 0001-0100
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/10-lotes/0001-0100

# Exemplo: extrair os últimos lotes 4901-5000
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz MERGE-COMPLETO/10-lotes/4901-5000
```

Se quiser extrair absolutamente tudo (`1.015.600 notas` / `1.021.127 arquivos`):

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

## 6. Resumo dos pacotes disponíveis

| Pacote | Tamanho | Conteúdo |
|---|---:|---|
| `study-vault-1m-packs.zip` | `19M` | Vault curado com 78 study packs (100% dos subdomínios), 85 MOCs, trilhas, playbooks, 9 canvases e **15.600 notas**. |
| `starter-vault-prioritario.zip` | `1.1M` | Pacote leve com **900 notas** prioritárias para início imediato. |
| `merge-completo-materializado-1m.tar.xz` | `34M` | Merge completo com vault curado (`15.600` notas) + todos os `5.000` lotes sequenciais (`1.000.000` de notas) = **1.015.600 notas**. |
| `ledger-v1000000-mat8000.sqlite.xz` | `24M` | Checkpoint do ledger SQLite com 1.000.000 de notas virtuais + 100 notas físicas. |

## 7. Segurança

Os conteúdos de cannabis medicinal e micologia são educacionais, documentais e não operacionais (`conteudo_operacional: false`). Eles foram estruturados para estudo, rastreabilidade, documentação e perguntas qualificadas para profissionais habilitados.
