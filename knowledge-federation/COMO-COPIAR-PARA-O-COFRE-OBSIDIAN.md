# Como copiar para o cofre Obsidian

Data: 2026-10-01

Este guia é para baixar a entrega do GitHub, reconstruir os arquivos grandes e copiar o conteúdo para seu cofre Obsidian.

## 1. Baixar a branch atual

O PR ainda está aberto. Enquanto ele não for mergeado, baixe a branch de trabalho:

```text
https://github.com/berger33/obsidian/archive/refs/heads/arena/01a0f4eb-obsidian.zip
```

Depois que o PR for mergeado em `main`, o link equivalente será:

```text
https://github.com/berger33/obsidian/archive/refs/heads/main.zip
```

PR:

```text
https://github.com/berger33/obsidian/pull/1
```

## 2. Descompactar o ZIP baixado

Ao descompactar, você terá uma pasta parecida com:

```text
obsidian-arena-01a0f4eb-obsidian/
```

Entre nessa pasta pelo terminal.

## 3. Reconstruir os arquivos grandes

Os arquivos maiores que 100 MiB foram divididos porque o GitHub não aceita arquivos grandes diretamente no Git.

Rode:

```bash
bash knowledge-federation/scripts/reconstruct_split_assets.sh
```

Isso reconstrói:

```text
knowledge-federation/archives/reconstructed/merge-completo-materializado-1m.tar.xz
knowledge-federation/archives/reconstructed/ledger-v1000000-mat8000.zip
```

O script também valida o checksum SHA-256.

## 4. Extrair o merge completo

Rode:

```bash
tar -xJf knowledge-federation/archives/reconstructed/merge-completo-materializado-1m.tar.xz
```

Será criada uma pasta:

```text
MERGE-COMPLETO/
```

## 5. Abrir o vault principal no Obsidian

No Obsidian, use:

```text
Open folder as vault
```

E selecione:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/
```

Esse é o vault curado, mais amigável para começar.

## 6. Copiar lotes específicos para seu cofre existente

Se você já tem um cofre e quer copiar partes específicas, copie pastas de:

```text
MERGE-COMPLETO/10-lotes/
```

Exemplos:

```text
MERGE-COMPLETO/10-lotes/0001-0100/
MERGE-COMPLETO/10-lotes/0101-0200/
MERGE-COMPLETO/10-lotes/3201-3300/
```

Cada intervalo tem:

```text
00-Inicio/Home.md
00-Mapas/
10-Lotes/
_canvas/
_meta/
README.md
```

## 7. Opção leve: Starter Vault

Também existe um pacote menor para começar sem extrair tudo:

```text
knowledge-federation/archives/starter-vault-prioritario.zip
```

Ele contém uma seleção prioritária de cerca de 900 notas focadas em IA, RAG, backend, orquestração e MVP.

## 8. O que significam os principais pacotes

| Pacote | Uso recomendado |
|---|---|
| `study-vault-1m-packs.zip` | Vault curado com trilhas, MOCs, playbooks e 7.100 notas. |
| `merge-completo-materializado-1m.tar.xz` | Merge completo com vault curado + 660.000 notas em lotes. |
| `ledger-v1000000-mat8000.zip` | Checkpoint do ledger SQLite com 1 milhão de notas virtuais. |
| `starter-vault-prioritario.zip` | Pacote menor para começar rápido. |

## 9. Segurança

Os conteúdos de cannabis medicinal e micologia são educacionais, documentais e não operacionais. Eles foram estruturados para estudo, rastreabilidade, documentação e perguntas qualificadas para profissionais habilitados.

Não use o material como prescrição, parecer jurídico, instrução de cultivo, instrução de extração ou guia operacional para substâncias controladas.
