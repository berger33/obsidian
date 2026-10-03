# Reconciliação estrutural — lote `software-devops-2000-0002`, tranche 5 (IDs 401–500)

- Data: 2026-10-03
- Escopo: reconciliação completa da **tranche 5** do segundo lote de escala (`software-devops-2000-0002`, subdomínio `software/devops`), adicionando **100 notas substantivas** (IDs **401–500**) em dez grupos temáticos com dez notas cada (**Grafana Tempo, VictoriaMetrics, Backstage, KubeVirt, MetalLB, Strimzi, Knative Serving, SPIFFE e SPIRE, Dapr e OpenFeature**).
- Revisor factual das 100 notas da tranche 5: `Arena.ai Agent Mode` (revisão factual assistida por IA registrada em [`ai-review-software-devops-2000-0002-tranche-05.md`](ai-review-software-devops-2000-0002-tranche-05.md); não é aprovação humana).

## Resumo de contagens após a tranche 5

| Métrica | Antes (após tranche 4) | Adicionado na tranche 5 | Depois (estado atual) |
|---|---:|---:|---:|
| Notas materiais no lote `software-devops-2000-0002` | 400 / 2.000 (20,00%) | +100 | **500 / 2.000 (25,00%)** |
| Notas aprovadas por revisão humana no lote 2 | 0 | +0 | **0** |
| Notas aprovadas por revisão factual de IA no lote 2 | 400 | +100 | **500** |
| Notas válidas no primeiro lote `software-testes-2000-0001` | 2.000 / 2.000 (100,00%) | +0 | **2.000 / 2.000 (`complete`)** |
| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2540 | +100 | **2640** |
| Notas candidatas aprovadas no gate automatizado global | 2440 | +100 | **2540** |
| Revisões humanas históricas globais preservadas | 49 | +0 | **49** |
| Revisões factuais por IA globais registradas separadamente | 2391 | +100 | **2491** |
| Notas válidas globais contabilizadas (`gate + revisão`) | 2440 / 1.000.000 (0,2440%) | +100 | **2540 / 1.000.000 (0,2540%)** |
| Sementes legadas com pendências (excluídas da meta) | 100 | +0 | **100** |

## Grupos temáticos e fontes primárias da tranche 5 (IDs 401–500)

1. **Grafana Tempo (IDs 401–410)**: README oficial (`raw.githubusercontent.com/grafana/tempo/main/README.md`) e documentação (`grafana.com/docs/tempo/latest/getting-started/`).
2. **VictoriaMetrics (IDs 411–420)**: README oficial (`raw.githubusercontent.com/VictoriaMetrics/VictoriaMetrics/master/README.md`) e conceitos fundamentais (`docs.victoriametrics.com/victoriametrics/keyconcepts/`).
3. **Backstage (IDs 421–430)**: README oficial (`raw.githubusercontent.com/backstage/backstage/master/README.md`) e documentação de arquitetura/início rápido (`backstage.io/docs/getting-started`).
4. **KubeVirt (IDs 431–440)**: README oficial (`raw.githubusercontent.com/kubevirt/kubevirt/main/README.md`) e especificação de arquitetura (`raw.githubusercontent.com/kubevirt/kubevirt/main/docs/architecture.md`).
5. **MetalLB (IDs 441–450)**: README oficial (`raw.githubusercontent.com/metallb/metallb/main/README.md`) e documentação de conceitos L2 ARP/NDP e BGP (`metallb.io/concepts/`).
6. **Strimzi (IDs 451–460)**: README oficial (`raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md`) e guia oficial Quick Starts (`strimzi.io/quickstarts/`).
7. **Knative Serving (IDs 461–470)**: README oficial (`raw.githubusercontent.com/knative/serving/main/README.md`) e guia de arquitetura e desenvolvimento (`raw.githubusercontent.com/knative/serving/main/DEVELOPMENT.md`).
8. **SPIFFE e SPIRE (IDs 471–480)**: README oficial (`raw.githubusercontent.com/spiffe/spire/main/README.md`) e guias de arquitetura e atestação (`spiffe.io/spire/try/`).
9. **Dapr (IDs 481–490)**: README oficial (`raw.githubusercontent.com/dapr/dapr/master/README.md`) e documentação oficial (`docs.dapr.io/getting-started/`).
10. **OpenFeature (IDs 491–500)**: Introdução e conceitos oficiais (`openfeature.dev/docs/reference/intro/`) e README da especificação na CNCF (`raw.githubusercontent.com/open-feature/spec/main/README.md`).

## Verificações de qualidade, similaridade e integridade

- **Gate automatizado do lote 2 (`audit_note_quality.py --path knowledge-federation/domains/software-0008/software/devops`)**: `500/500` aprovadas (`0` pendências); contagem de palavras da tranche 5 entre `352` e `540` palavras por nota, com `3` fontes HTTPS específicas por nota.
- **Gate automatizado global (`audit_note_quality.py`)**: `2640` arquivos inspecionados, `2540` candidatas válidas (`49` humanas + `2491` IA) e `100` notas legadas com pendências.
- **Auditoria estrutural (`global_audit_fast.py`)**: executada e sincronizada em [`global-audit-fast.md`](global-audit-fast.md).
- **Testes unitários (`python3 -m unittest discover -s knowledge-federation/tests -v`)**: `12/12` testes aprovados (`OK`).
- **Similaridade Jaccard de shingles de 5 palavras (100 notas da tranche 5)**:
  - Arquivo completo: média entre grupos = `0.0564`, média intra-grupo = `0.2401`.
  - Prosa substantiva do corpo (excluindo frontmatter, conexões e fontes): média entre grupos = `0.0003`, média intra-grupo = `0.0010`, par máximo = `0.0274`.
- **Artefatos reconciliados**:
  - Manifesto do lote 2: [`../batches/software-devops-2000-0002.md`](../batches/software-devops-2000-0002.md)
  - MOC do lote 2: [`../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)
  - Fila de revisão: [`human-review-queue.md`](human-review-queue.md) (linhas `2441–2540` adicionadas para as notas `401–500` do lote 2)
  - Documentos globais de status: `README.md`, `knowledge-federation/README.md`, `knowledge-federation/README-1M.md`, `knowledge-federation/STATUS-CONSOLIDACAO-1M.md`, `knowledge-federation/PLANO-CONTINUO-1M.md`, `knowledge-federation/RECOVERY-AND-SCALE-NOTE.md`, `knowledge-federation/00-home-vault/Home.md` e `knowledge-federation/00-home-vault/Indice-Global.md`.
