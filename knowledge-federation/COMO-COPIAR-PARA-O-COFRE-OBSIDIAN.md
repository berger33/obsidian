# Como abrir os artefatos no Obsidian

Data: 2026-10-01

> **Importante:** os pacotes abaixo são artefatos históricos de catálogo/materialização. A auditoria detectou texto-template nos 1.000.000 registros virtuais. Os números descrevem IDs e arquivos, não 1 milhão de notas válidas. Confira [`STATUS-CONSOLIDACAO-1M.md`](STATUS-CONSOLIDACAO-1M.md) antes de usar os totais.

## 1. Baixar o repositório

Após o merge, baixe a branch `main`:

```text
https://github.com/berger33/obsidian/archive/refs/heads/main.zip
```

## 2. Artefatos disponíveis

| Pacote | Tamanho aprox. | Descrição / ressalva |
|---|---:|---|
| `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` | 34 MB | Merge histórico de arquivos de catálogo, packs, lotes e relatórios. Não são 1.015.600 notas validadas. |
| `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` | 24 MB | Checkpoint com 1.000.000 de registros virtuais e 100 registros físicos iniciais; entradas virtuais têm marcadores de template. |
| `knowledge-federation/archives/study-vault-1m-packs.zip` | 19 MB | 78 packs estruturais / 15.600 arquivos materializados; a auditoria de links não certifica conteúdo. |
| `knowledge-federation/archives/starter-vault-prioritario.zip` | 1,1 MB | Recorte leve de inspeção; a quantidade de arquivos não é selo de qualidade. |

## 3. Abrir ou inspecionar um recorte

Para abrir os Study Packs antigos no Obsidian:

```bash
unzip knowledge-federation/archives/study-vault-1m-packs.zip -d study-vault-1m-packs
```

No Obsidian, use **Open folder as vault** e selecione `study-vault-1m-packs`. Trate o conteúdo como material de inventário, não como fonte técnica validada.

Para extrair apenas um intervalo do TAR, evitando criar muitos arquivos no disco:

```bash
mkdir -p /tmp/merge-parcial
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz \
  -C /tmp/merge-parcial MERGE-COMPLETO/10-lotes/0001-0100
```

Não é necessário extrair o TAR inteiro para consultar o checkpoint.

## 4. Auditar o estado de qualidade

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

O gate separa arquivos-template, candidatas a revisão e conteúdo com revisão humana registrada. Um passe automatizado não é aprovação factual.

## 5. Checksums

Os hashes e instruções de conferência estão em [`RELEASE-DOWNLOADS.md`](RELEASE-DOWNLOADS.md). O checkpoint e o merge são preservados para compatibilidade e recuperação; não reconstruir nem sobrescrever esses arquivos para tentar aumentar artificialmente a contagem de notas válidas.
