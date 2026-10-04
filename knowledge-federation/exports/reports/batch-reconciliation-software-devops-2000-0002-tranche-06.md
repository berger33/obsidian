# Reconciliação estrutural — lote `software-devops-2000-0002`, tranche 6 (IDs 501–600)

- Data: 2026-10-03
- Escopo: reconciliação completa da **tranche 6** do segundo lote de escala (`software-devops-2000-0002`, subdomínio `software/devops`), adicionando **100 notas substantivas** (IDs **501–600**) em dez grupos temáticos com dez notas cada (**LitmusChaos, Chaos Mesh, Tilt, Buildah, Skopeo, Kaniko, Dagger, HashiCorp Vagrant, HashiCorp Consul e HashiCorp Nomad**).
- Revisor factual das 100 notas da tranche 6: `Arena.ai Agent Mode` (revisão factual assistida por IA registrada em [`ai-review-software-devops-2000-0002-tranche-06.md`](ai-review-software-devops-2000-0002-tranche-06.md); não é aprovação humana).

## Resumo de contagens após a tranche 6

| Métrica | Antes (após tranche 5) | Adicionado na tranche 6 | Depois (estado atual) |
|---|---:|---:|---:|
| Notas materiais no lote `software-devops-2000-0002` | 500 / 2.000 (25,00%) | +100 | **600 / 2.000 (30,00%)** |
| Notas aprovadas por revisão humana no lote 2 | 0 | +0 | **0** |
| Notas aprovadas por revisão factual de IA no lote 2 | 500 | +100 | **600** |
| Notas válidas no primeiro lote `software-testes-2000-0001` | 2.000 / 2.000 (100,00%) | +0 | **2.000 / 2.000 (`complete`)** |
| Arquivos Markdown ativos em `knowledge-federation/domains/` | 2640 | +100 | **2740** |
| Notas candidatas aprovadas no gate automatizado global | 2540 | +100 | **2640** |
| Revisões humanas históricas globais preservadas | 49 | +0 | **49** |
| Revisões factuais por IA globais registradas separadamente | 2491 | +100 | **2591** |
| Notas válidas globais contabilizadas (`gate + revisão`) | 2540 / 1.000.000 (0,2540%) | +100 | **2640 / 1.000.000 (0,2640%)** |
| Sementes legadas com pendências (excluídas da meta) | 100 | +0 | **100** |

## Grupos temáticos e fontes primárias da tranche 6 (IDs 501–600)

1. **LitmusChaos (IDs 501–510)**: README oficial (`raw.githubusercontent.com/litmuschaos/litmus/master/README.md`) e documentação (`docs.litmuschaos.io/docs/introduction/what-is-litmus`).
2. **Chaos Mesh (IDs 511–520)**: README oficial (`raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md`) e guia de arquitetura dos controladores (`raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md`).
3. **Tilt (IDs 521–530)**: README oficial (`raw.githubusercontent.com/tilt-dev/tilt/master/README.md`) e tutorial oficial (`docs.tilt.dev/tutorial/index.html`).
4. **Buildah (IDs 531–540)**: README oficial (`raw.githubusercontent.com/containers/buildah/main/README.md`) e guia de ferramentas (`github.com/containers/buildah/tree/main/docs/containertools`).
5. **Skopeo (IDs 541–550)**: README oficial (`raw.githubusercontent.com/containers/skopeo/main/README.md`) e documentação da imagem oficial (`github.com/containers/image_build/blob/main/skopeo/README.md`).
6. **Kaniko (IDs 551–560)**: README oficial (`raw.githubusercontent.com/GoogleContainerTools/kaniko/main/README.md`) e tutorial (`github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md`).
7. **Dagger (IDs 561–570)**: README oficial (`raw.githubusercontent.com/dagger/dagger/main/README.md`) e guia de contribuição e engenharia (`raw.githubusercontent.com/dagger/dagger/main/CONTRIBUTING.md`).
8. **HashiCorp Vagrant (IDs 571–580)**: README oficial (`raw.githubusercontent.com/hashicorp/vagrant/main/README.md`) e guia de início rápido (`vagrantup.com/docs/getting-started`).
9. **HashiCorp Consul (IDs 581–590)**: README oficial (`raw.githubusercontent.com/hashicorp/consul/main/README.md`) e documentação oficial (`developer.hashicorp.com/consul/docs`).
10. **HashiCorp Nomad (IDs 591–600)**: README oficial (`raw.githubusercontent.com/hashicorp/nomad/main/README.md`) e documentação oficial (`developer.hashicorp.com/nomad/docs`).

## Verificações de qualidade, similaridade e integridade

- **Gate automatizado do lote 2 (`audit_note_quality.py --path knowledge-federation/domains/software-0008/software/devops`)**: `600/600` aprovadas (`0` pendências); contagem de palavras da tranche 6 entre `361` e `545` palavras por nota, com `3` fontes HTTPS específicas por nota.
- **Gate automatizado global (`audit_note_quality.py`)**: `2740` arquivos inspecionados, `2640` candidatas válidas (`49` humanas + `2591` IA) e `100` notas legadas com pendências.
- **Auditoria estrutural (`global_audit_fast.py`)**: executada e sincronizada em [`global-audit-fast.md`](global-audit-fast.md).
- **Testes unitários (`python3 -m unittest discover -s knowledge-federation/tests -v`)**: `12/12` testes aprovados (`OK`).
- **Similaridade Jaccard de shingles de 5 palavras (100 notas da tranche 6)**:
  - Arquivo completo: média entre grupos = `0.0550`, média intra-grupo = `0.2412`.
  - Prosa substantiva do corpo (excluindo frontmatter, conexões e fontes): média entre grupos = `0.0004`, média intra-grupo = `0.0009`, par máximo = `0.0136`.
- **Artefatos reconciliados**:
  - Manifesto do lote 2: [`../batches/software-devops-2000-0002.md`](../batches/software-devops-2000-0002.md)
  - MOC do lote 2: [`../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md`](../../00-home-vault/MOCs/MOC-DevOps-Software-0008.md)
  - Fila de revisão: [`human-review-queue.md`](human-review-queue.md) (linhas `2541–2640` adicionadas para as notas `501–600` do lote 2)
  - Documentos globais de status: `README.md`, `knowledge-federation/README.md`, `knowledge-federation/README-1M.md`, `knowledge-federation/STATUS-CONSOLIDACAO-1M.md`, `knowledge-federation/PLANO-CONTINUO-1M.md`, `knowledge-federation/RECOVERY-AND-SCALE-NOTE.md`, `knowledge-federation/00-home-vault/Home.md` e `knowledge-federation/00-home-vault/Indice-Global.md`.
