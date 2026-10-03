# Reconciliação estrutural — lote `software-devops-2000-0002`, tranche 7 (IDs 601–700)

- Data: 2026-10-03
- Escopo: reconciliação completa da **tranche 7** do segundo lote de escala (`software-devops-2000-0002`, subdomínio `software/devops`), adicionando **100 notas substantivas** (IDs **601–700**) em dez grupos temáticos com dez notas cada (**Grafana Mimir, Grafana Pyroscope, Cilium Tetragon, Inspektor Gadget, Kubescape, OpenCost, Flux Flagger, Kubernetes Descheduler, OpenContainer runc e Containers crun**).
- Revisor factual das 100 notas da tranche 7: `Arena.ai Agent Mode` (revisão factual assistida por IA registrada em [`ai-review-software-devops-2000-0002-tranche-07.md`](ai-review-software-devops-2000-0002-tranche-07.md); não é aprovação humana).

## Resumo de contagens após a tranche 7

| Métrica | Antes (após tranche 6) | Adicionado na tranche 7 | Depois (estado atual) |
|---|---:|---:|---:|
| Notas materiais no lote `software-devops-2000-0002` | 600 / 2.000 (30,00%) | +100 | **700 / 2.000 (35,00%)** |
| Notas aprovadas por revisão humana no lote 2 | 0 | +0 | **0** |
| Notas aprovadas por revisão factual de IA no lote 2 | 600 | +100 | **700** |
| Notas válidas no primeiro lote `software-testes-2000-0001` | 2.000 / 2.000 (100,00%) | +0 | **2.000 / 2.000 (`complete`)** |
| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2740 | +100 | **2840** |
| Notas candidatas aprovadas no gate automatizado global | 2640 | +100 | **2740** |
| Revisões humanas históricas globais preservadas | 49 | +0 | **49** |
| Revisões factuais por IA globais registradas separadamente | 2591 | +100 | **2691** |
| Notas válidas globais contabilizadas (`gate + revisão`) | 2640 / 1.000.000 (0,2640%) | +100 | **2740 / 1.000.000 (0,2740%)** |
| Sementes legadas com pendências (excluídas da meta) | 100 | +0 | **100** |

## Grupos temáticos e fontes primárias da tranche 7 (IDs 601–700)

1. **Grafana Mimir (IDs 601–610)**: README oficial (`raw.githubusercontent.com/grafana/mimir/main/README.md`) e documentação de arquitetura e componentes (`grafana.com/docs/mimir/latest/references/architecture/components.md`).
2. **Grafana Pyroscope (IDs 611–620)**: README oficial (`raw.githubusercontent.com/grafana/pyroscope/main/README.md`) e documentação da arquitetura v2 (`grafana.com/docs/pyroscope/latest/reference-pyroscope-v2-architecture/about-pyroscope-v2-architecture.md`).
3. **Cilium Tetragon (IDs 621–630)**: README oficial (`raw.githubusercontent.com/cilium/tetragon/main/README.md`) e documentação de visão geral e eBPF (`tetragon.io/docs/overview/`).
4. **Inspektor Gadget (IDs 631–640)**: README oficial (`raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md`) e documentação oficial de Gadgets (`www.inspektor-gadget.io/docs/latest/gadgets/`).
5. **Kubescape (IDs 641–650)**: README oficial (`raw.githubusercontent.com/kubescape/kubescape/master/README.md`) e documentação do operador in-cluster (`kubescape.io/docs/operator/`).
6. **OpenCost (IDs 651–660)**: README oficial (`raw.githubusercontent.com/opencost/opencost/develop/README.md`) e documentação de integração Prometheus (`www.opencost.io/docs/installation/prometheus`).
7. **Flux Flagger (IDs 661–670)**: README oficial (`raw.githubusercontent.com/fluxcd/flagger/main/README.md`) e documentação de funcionamento (`docs.flagger.app/main/usage/how-it-works`).
8. **Kubernetes Descheduler (IDs 671–680)**: README oficial (`raw.githubusercontent.com/kubernetes-sigs/descheduler/master/README.md`) e documentação do Helm chart oficial (`github.com/kubernetes-sigs/descheduler/blob/master/charts/descheduler/README.md`).
9. **OpenContainer runc (IDs 681–690)**: README oficial (`raw.githubusercontent.com/opencontainers/runc/main/README.md`) e especificação OCI Runtime (`github.com/opencontainers/runtime-spec`).
10. **Containers crun (IDs 691–700)**: README oficial (`raw.githubusercontent.com/containers/crun/main/README.md`) e página de manual `crun.1.md` (`raw.githubusercontent.com/containers/crun/main/crun.1.md`).

## Verificações de qualidade, similaridade e integridade

- **Gate automatizado do lote 2 (`audit_note_quality.py --path knowledge-federation/domains/software-0008/software/devops`)**: `700/700` aprovadas (`0` pendências); contagem de palavras da tranche 7 entre `371` e `528` palavras por nota, com `3` fontes HTTPS específicas por nota.
- **Gate automatizado global (`audit_note_quality.py`)**: `2840` arquivos inspecionados, `2740` candidatas válidas (`49` humanas + `2691` IA) e `100` notas legadas com pendências.
- **Auditoria estrutural (`global_audit_fast.py`)**: executada e sincronizada em [`global-audit-fast.md`](global-audit-fast.md).
- **Testes unitários (`python3 -m unittest discover -s knowledge-federation/tests -v`)**: `12/12` testes aprovados (`OK`).
- **Similaridade Jaccard de shingles de 5 palavras (100 notas da tranche 7)**:
  - Prosa substantiva do corpo (excluindo frontmatter, conexões e fontes): média entre grupos = `0.0003`, média intra-grupo = `0.0027`, par máximo = `0.0245`.
- **Artefatos reconciliados**:
  - Manifesto do lote 2: [`../batches/software-devops-2000-0002.md`](../batches/software-devops-2000-0002.md)
  - MOC do lote 2: [`../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)
  - Fila de revisão: [`human-review-queue.md`](human-review-queue.md) (linhas `2641–2740` adicionadas para as notas `601–700` do lote 2)
  - Documentos globais de status: `README.md`, `knowledge-federation/README.md`, `knowledge-federation/README-1M.md`, `knowledge-federation/STATUS-CONSOLIDACAO-1M.md`, `knowledge-federation/PLANO-CONTINUO-1M.md`, `knowledge-federation/RECOVERY-AND-SCALE-NOTE.md`, `knowledge-federation/00-home-vault/Home.md` e `knowledge-federation/00-home-vault/Indice-Global.md`.
