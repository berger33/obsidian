# Reconciliação estrutural — lote `software-devops-2000-0002`, tranche 8 (IDs 701–800)

- Data: 2026-10-03
- Escopo: reconciliação completa da **tranche 8** do segundo lote de escala (`software-devops-2000-0002`, subdomínio `software/devops`), adicionando **100 notas substantivas** (IDs **701–800**) em dez grupos temáticos com dez notas cada (**Kata Containers, AWS Firecracker, Google gVisor, Youki, Liquibase, Redgate Flyway, Ariga Atlas, Bytebase, Nix e Earthly**).
- Revisor factual das 100 notas da tranche 8: `Arena.ai Agent Mode` (revisão factual assistida por IA registrada em [`ai-review-software-devops-2000-0002-tranche-08.md`](ai-review-software-devops-2000-0002-tranche-08.md); não é aprovação humana).

## Resumo de contagens após a tranche 8

| Métrica | Antes (após tranche 7) | Adicionado na tranche 8 | Depois (estado atual) |
|---|---:|---:|---:|
| Notas materiais no lote `software-devops-2000-0002` | 700 / 2.000 (35,00%) | +100 | **800 / 2.000 (40,00%)** |
| Notas aprovadas por revisão humana no lote 2 | 0 | +0 | **0** |
| Notas aprovadas por revisão factual de IA no lote 2 | 700 | +100 | **800** |
| Notas válidas no primeiro lote `software-testes-2000-0001` | 2.000 / 2.000 (100,00%) | +0 | **2.000 / 2.000 (`complete`)** |
| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2840 | +100 | **2940** |
| Notas candidatas aprovadas no gate automatizado global | 2740 | +100 | **2840** |
| Revisões humanas históricas globais preservadas | 49 | +0 | **49** |
| Revisões factuais por IA globais registradas separadamente | 2691 | +100 | **2791** |
| Notas válidas globais contabilizadas (`gate + revisão`) | 2740 / 1.000.000 (0,2740%) | +100 | **2840 / 1.000.000 (0,2840%)** |
| Sementes legadas com pendências (excluídas da meta) | 100 | +0 | **100** |

## Grupos temáticos e fontes primárias da tranche 8 (IDs 701–800)

1. **Kata Containers (IDs 701–710)**: README oficial (`raw.githubusercontent.com/kata-containers/kata-containers/main/README.md`) e documentação de arquitetura 4.0 (`github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md`).
2. **AWS Firecracker (IDs 711–720)**: README oficial (`raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md`) e documentação de design, especificação e produção (`github.com/firecracker-microvm/firecracker/blob/main/docs/design.md`).
3. **Google gVisor (IDs 721–730)**: README oficial (`raw.githubusercontent.com/google/gvisor/master/README.md`) e guia de arquitetura de segurança (`gvisor.dev/docs/architecture_guide/intro/`).
4. **Youki (IDs 731–740)**: README oficial (`raw.githubusercontent.com/youki-dev/youki/main/README.md`) e documentação oficial (`youki-dev.github.io/youki/user/basic_setup.html`).
5. **Liquibase (IDs 741–750)**: README oficial (`raw.githubusercontent.com/liquibase/liquibase/master/README.md`) e documentação de imagens Docker e migração 5.0+ (`raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md`).
6. **Redgate Flyway (IDs 751–760)**: README oficial (`raw.githubusercontent.com/flyway/flyway/main/README.md`) e guia oficial Redgate (`documentation.red-gate.com/flyway/getting-started-with-flyway`).
7. **Ariga Atlas (IDs 761–770)**: README oficial (`raw.githubusercontent.com/ariga/atlas/master/README.md`) e guia oficial (`atlasgo.io/getting-started`).
8. **Bytebase (IDs 771–780)**: README oficial (`raw.githubusercontent.com/bytebase/bytebase/main/README.md`) e documentação de implantação Self-hosted vs Cloud (`docs.bytebase.com/get-started/self-host-vs-cloud`).
9. **Nix (IDs 781–790)**: README oficial (`raw.githubusercontent.com/NixOS/nix/master/README.md`) e tutorial oficial de ambientes ad-hoc e reprodutibilidade (`nix.dev/tutorials/first-steps/ad-hoc-shell-environments`).
10. **Earthly (IDs 791–800)**: README oficial (`raw.githubusercontent.com/earthly/earthly/main/README.md`) e referência oficial do Earthfile (`docs.earthly.dev/docs/earthfile`).

## Verificações de qualidade, similaridade e integridade

- **Gate automatizado do lote 2 (`audit_note_quality.py --path knowledge-federation/domains/software-0008/software/devops`)**: `800/800` aprovadas (`0` pendências); contagem de palavras da tranche 8 entre `365` e `540` palavras por nota, com `3` fontes HTTPS específicas por nota.
- **Gate automatizado global (`audit_note_quality.py`)**: `2940` arquivos inspecionados, `2840` candidatas válidas (`49` humanas + `2791` IA) e `100` notas legadas com pendências.
- **Auditoria estrutural (`global_audit_fast.py`)**: executada e sincronizada em [`global-audit-fast.md`](global-audit-fast.md).
- **Testes unitários (`python3 -m unittest discover -s knowledge-federation/tests -v`)**: `12/12` testes aprovados (`OK`).
- **Similaridade Jaccard de shingles de 5 palavras (100 notas da tranche 8)**:
  - Prosa substantiva do corpo (excluindo frontmatter, conexões e fontes): média entre grupos = `0.0002`, média intra-grupo = `0.0024`, par máximo = `0.0214`.
- **Artefatos reconciliados**:
  - Manifesto do lote 2: [`../batches/software-devops-2000-0002.md`](../batches/software-devops-2000-0002.md)
  - MOC do lote 2: [`../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)
  - Fila de revisão: [`human-review-queue.md`](human-review-queue.md) (linhas `2741–2840` adicionadas para as notas `701–800` do lote 2)
  - Documentos globais de status: `README.md`, `knowledge-federation/README.md`, `knowledge-federation/README-1M.md`, `knowledge-federation/STATUS-CONSOLIDACAO-1M.md`, `knowledge-federation/PLANO-CONTINUO-1M.md`, `knowledge-federation/RECOVERY-AND-SCALE-NOTE.md`, `knowledge-federation/00-home-vault/Home.md` e `knowledge-federation/00-home-vault/Indice-Global.md`.
