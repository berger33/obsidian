# Merge consolidado histórico — Knowledge Federation

Data de rebuild e verificação end-to-end: 2026-10-01

> **Ressalva de qualidade:** o arquivo inclui 1.000.000 de arquivos-placeholder derivados do catálogo. A auditoria encontrou marcadores de template em todos os registros virtuais do checkpoint. O TAR também inclui oito notas candidatas ao gate automatizado; elas ainda aguardam revisão humana. **Arquivos, IDs, MOCs, links e candidatas não são notas válidas aprovadas.**

## Artefato

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

SHA-256:

```text
2712e91e13e6f9d3a828ca37eb4092c0d5dd0d403120cbcf7367da805f5e4eeb
```

Tamanho: **33.118.156 bytes** (aprox. 31,6 MiB / 33,1 MB).

Checksum sidecar: `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz.sha256`.

## Conteúdo e estado editorial

```text
MERGE-COMPLETO/00-home-vault/                 Home Vault atual e seus MOCs/Canvases
MERGE-COMPLETO/00-vault-consolidado/          Study Vault histórico (78 packs)
MERGE-COMPLETO/domains/software-0002/          8 notas candidatas do lote curated-batch-000001
MERGE-COMPLETO/10-lotes/                      5.000 lotes de arquivos-placeholder
MERGE-COMPLETO/90-ledger/                     ponteiro para o checkpoint
MERGE-COMPLETO/99-relatorios/                  auditorias, manifestos e relatórios
```

- **Home Vault:** 21 arquivos, com 10 MOCs e 8 Canvases. O MOC `MOC-Confiabilidade-e-Contratos` é apenas navegação; sua presença não aprova o lote.
- **Study Vault:** 78 packs e 15.600 arquivos de nota, além de mapas, trilhas e outros auxiliares. A validação estrutural dos links não certifica o conteúdo editorial.
- **Sequência:** 50 pacotes, 5.000 lotes e 1.000.000 de arquivos-placeholder materializados. Esses arquivos não passaram por validação editorial.
- **Lote curado:** 8 candidatas incluídas; checagem assistida de fontes registrada; revisão humana pendente; notas válidas aprovadas: **0**. A checagem assistida não equivale a aprovação humana.
- **Ledger:** o TAR contém `LATEST-LEDGER.txt`; o SQLite compactado permanece como artefato irmão em `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` e não é duplicado dentro do TAR.
- **Relatórios:** 55 relatórios Markdown atuais, além de manifestos, estados e documentos de operação.

## Contagens auditadas do arquivo

```text
Study Packs: 78
Arquivos de nota nos Study Packs: 15.600
Lotes sequenciais: 5.000
Arquivos-placeholder sequenciais: 1.000.000
Notas candidatas do lote curated-batch-000001: 8
Arquivos de nota representados (sem MOCs/relatórios): 1.015.608
Entradas no TAR: 1.021.139
Notas válidas aprovadas por revisão humana: 0
Conteúdo operacional regulado: 0
```

O manifesto interno `MERGE-COMPLETO/99-relatorios/manifest-merge-completo.json` separa contagem de placeholders, candidatas e notas válidas. O agregador não aprova notas: `notes_validated_by_this_aggregator=0`.

## Integridade e teste end-to-end

Resultados da reconstrução a partir do TAR-base e da verificação do arquivo final:

```text
xz -t: OK
Entradas TAR lidas em streaming: 1.021.139
Arquivos-placeholder contados nos caminhos dos lotes: 1.000.000
Notas candidatas incluídas e comparadas byte a byte com as fontes: 8
Relatórios Markdown incluídos: 55
Caminhos duplicados: 0
Caminhos absolutos ou com '..': 0
Home -> MOC -> notas candidatas: resolvido
Links relativos do relatório de checagem de fontes para as 8 notas: resolvidos
Revisão humana no manifesto: pending
```

Para validar o checksum no root do repositório:

```bash
sha256sum -c knowledge-federation/archives/merge-completo-materializado-1m.tar.xz.sha256
```

## Como reconstruir com segurança após os ZIPs de lotes terem sido podados

A reconstrução incremental usa o TAR anterior como base e grava em um arquivo temporário, sem truncar o original durante a geração. Só substitua o artefato depois de validar checksum, compressão, contagens e manifestos:

```bash
set -o pipefail
python3 knowledge-federation/scripts/merge_complete_archives.py \
  --base-tar knowledge-federation/archives/merge-completo-materializado-1m.tar.xz \
  | xz -T0 -1 > /tmp/merge-completo-materializado-1m.next.tar.xz

xz -t /tmp/merge-completo-materializado-1m.next.tar.xz
# Inspecione o manifesto e valide as contagens antes de substituir o TAR-base.
```

Não use `build_full_merge_from_ledger.py` para substituir o TAR de produção sem o opt-in explícito `--allow-catalog-stubs`: ele recria placeholders e pode sobrescrever a saída, sem executar revisão editorial.

## Extração

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Para inspecionar apenas uma parte e evitar criar um milhão de arquivos soltos no disco:

```bash
# Vault estrutural e notas candidatas
mkdir -p /tmp/kf-inspecao
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz \
  -C /tmp/kf-inspecao MERGE-COMPLETO/00-home-vault \
  MERGE-COMPLETO/domains/software-0002

# Um intervalo específico de 100 lotes (20.000 arquivos-placeholder)
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz \
  MERGE-COMPLETO/10-lotes/4901-5000
```
