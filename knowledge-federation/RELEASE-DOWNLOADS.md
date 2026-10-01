# Links de download da entrega completa

Os arquivos grandes foram enviados ao GitHub como **partes divididas** dentro da branch, porque o GitHub bloqueia arquivos Git maiores que 100 MiB.

## Link para baixar tudo do GitHub

Baixe a branch inteira como ZIP:

```text
https://github.com/berger33/obsidian/archive/refs/heads/arena/01a0f4eb-obsidian.zip
```

Ou veja a branch no GitHub:

```text
https://github.com/berger33/obsidian/tree/arena/01a0f4eb-obsidian
```

## Onde estão os arquivos para reconstruir

Depois de baixar/descompactar o ZIP da branch, abra:

```text
knowledge-federation/archives/split-assets/
```

Arquivos do merge completo:

```text
merge-completo-materializado-1m.tar.xz.part-000
merge-completo-materializado-1m.tar.xz.part-001
merge-completo-materializado-1m.tar.xz.part-002
```

Arquivos do ledger/checkpoint:

```text
ledger-v1000000-mat8000.zip.part-000
ledger-v1000000-mat8000.zip.part-001
ledger-v1000000-mat8000.zip.part-002
```

## Reconstruir manualmente

Dentro de `knowledge-federation/archives/split-assets/`:

```bash
cat merge-completo-materializado-1m.tar.xz.part-* > merge-completo-materializado-1m.tar.xz
cat ledger-v1000000-mat8000.zip.part-* > ledger-v1000000-mat8000.zip
sha256sum -c SHA256SUMS.txt --ignore-missing
```

## Reconstruir com script

No root do repositório:

```bash
bash knowledge-federation/scripts/reconstruct_split_assets.sh
```

Os arquivos reconstruídos ficarão em:

```text
knowledge-federation/archives/reconstructed/
```

## Copiar para o cofre Obsidian

Guia simples:

```text
knowledge-federation/COMO-COPIAR-PARA-O-COFRE-OBSIDIAN.md
```

Depois de reconstruir e extrair:

```bash
tar -xJf knowledge-federation/archives/reconstructed/merge-completo-materializado-1m.tar.xz
```

Abra no Obsidian ou copie para seu cofre:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/
```

Ou copie lotes específicos de:

```text
MERGE-COMPLETO/10-lotes/
```

## Opção leve

Para começar sem extrair o merge completo, use:

```text
knowledge-federation/archives/starter-vault-prioritario.zip
```

Ele contém 900 notas prioritárias sobre IA, RAG, backend, vibe coding/orquestração e MVP.
