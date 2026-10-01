# Study packs históricos materializados do ledger (78 subdomínios)

Data: 2026-10-01

> **Ressalva:** os 15.600 itens são arquivos-placeholder derivados de registros de catálogo. A auditoria encontrou texto-template nos registros virtuais que alimentam os packs. Não conte esses arquivos como notas válidas; consulte [`STATUS-CONSOLIDACAO-1M.md`](STATUS-CONSOLIDACAO-1M.md).

Este diretório contém 78 recortes organizados pela taxonomia, com 200 arquivos por subdomínio. A cobertura de tópicos e o total de arquivos não certificam conteúdo.

## Checkpoint-fonte

```text
knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Cobertura completa por domínio (78 Study Packs)

| Domínio | Subdomínios / Packs | Arquivos por Pack | Arquivos Totais |
|---|---:|---:|---:|
| `software` | 16 | 200 | 3.200 |
| `ia` | 12 | 200 | 2.400 |
| `jogos` | 12 | 200 | 2.400 |
| `cannabis-medicinal` | 11 | 200 | 2.200 |
| `vibe-coding` | 10 | 200 | 2.000 |
| `micologia` | 9 | 200 | 1.800 |
| `negocio-carreira-produto` | 8 | 200 | 1.600 |
| **Total** | **78** | **200** | **15.600** |

A lista completa dos 78 arquivos `.zip` individuais está em:

```text
knowledge-federation/PACK-INVENTORY.md
knowledge-federation/00-home-vault/MOCs/MOC-78-Study-Packs.md
```

## Vault consolidado com todos os 78 packs

Todos os 78 study packs estão reunidos e interligados em:

```text
knowledge-federation/archives/study-vault-1m-packs.zip
```

E também dentro do merge completo (`MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/`):

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

## Como regerar todos os 78 packs e o Study Vault

```bash
python knowledge-federation/scripts/build_all_78_study_packs.py --allow-catalog-stubs  # apenas para inspeção/recuperação; não cria notas válidas
python knowledge-federation/scripts/build_pack_inventory.py
```

## Segurança

Os packs de `cannabis-medicinal` (11 packs) e `micologia` (9 packs) são educacionais, científicos, regulatórios e não operacionais (`conteudo_operacional: false`). Devem ser usados para estudo, documentação, rastreabilidade, leitura crítica e formulação de perguntas a profissionais habilitados.
