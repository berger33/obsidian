# Study packs materializados do ledger de 1M (78 Subdomínios Completos)

Data: 2026-10-01

Este diretório contém os **78 recortes temáticos (100% dos subdomínios da taxonomia)** materializados a partir do checkpoint de 1 milhão de notas lógicas, com **200 notas por subdomínio = 15.600 notas curadas**.

## Checkpoint-fonte

```text
knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Cobertura completa por domínio (78 Study Packs)

| Domínio | Subdomínios / Packs | Notas por Pack | Notas Totais |
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
python knowledge-federation/scripts/build_all_78_study_packs.py
python knowledge-federation/scripts/build_pack_inventory.py
```

## Segurança

Os packs de `cannabis-medicinal` (11 packs) e `micologia` (9 packs) são educacionais, científicos, regulatórios e não operacionais (`conteudo_operacional: false`). Devem ser usados para estudo, documentação, rastreabilidade, leitura crítica e formulação de perguntas a profissionais habilitados.
