---
id: software.devops.tranche11.001074
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://popeyecli.io/docs/codes.html", "https://raw.githubusercontent.com/derailed/popeye/master/README.md", "https://github.com/derailed/popeye"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Códigos de diagnóstico do Popeye para Geral (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PV/PVC (1000–1004), Services (1100–1110) e NetworkPolicies (1200–1206)

## Em uma frase
Além de containers e pods, a tabela de códigos do Popeye cobre diagnósticos profundos de infraestrutura e topologia: referências órfãs e APIs depreciadas (**400–407**), sub/sobrealocação em Deployments/StatefulSets (**500–508**), capacidade de explosão de HPAs (**600–605**), saúde de Nodes (**700–712**), PDBs (**900–901**), PVs/PVCs (**1000–1004**), Services/Endpoints (**1100–1110**) e NetworkPolicies (**1200–1206**).

## Por que importa
Muitos incidentes graves em Kubernetes decorrem de inconsistências entre recursos distintos: um `Service` cujo seletor não casa com nenhum pod (`1100`) ou cuja `targetPort` não existe no container (`1106`), um `PodDisruptionBudget` cujo `minAvailable` é maior que o número de pods rodando (`901`) bloqueando o drain de nós, ou múltiplos `HorizontalPodAutoscalers` que, se dispararem juntos no pico (`604`/`605`), excederão a capacidade total de CPU e memória do cluster.

## Como funciona
Conforme documentado em `popeyecli.io/docs/codes.html`:
- **General (400–407)**: `400`/`401` (recurso ou chave de Secret/ConfigMap não referenciado, Sev 1), `402` (`metrics-server` não detectado, Sev 1), `403` (grupo de API depreciado, Sev 2) e `407` (referência a recurso inexistente, Sev 3);
- **Workloads (500–508)**: `500` (escala zero detectada, Sev 2), `501` (réplicas disponíveis abaixo do desejado, Sev 3), `503`/`505` (CPU/Memória subalocada na carga atual, Sev 2), `504`/`506` (CPU/Memória sobrealocada na carga atual, Sev 2) e `508` (nenhum pod corresponde ao seletor do controlador, Sev 3);
- **HPA (600–605)**: `600`/`601` (HPA aponta para Deployment/StatefulSet inexistente, Sev 3) e `602`–`605` (no pico máximo de réplicas de um ou de todos os HPAs, a demanda igualará ou excederá a capacidade de CPU/memória do cluster, Sev 2);
- **Nodes (700–712), PDB (900–901), PV/PVC (1000–1004), Service (1100–1110) e NetworkPolicies (1200–1206)**: incluem alertas como `700` (taint no nó que nenhum pod tolera), `1001`/`1003` (PV/PVC Pending, Sev 3), `1100`/`1105`/`1106` (Service sem pods/endpoints ou porta divergente, Sev 3) e `1204`/`1205` (Pod não protegido por NetworkPolicy de ingress/egress, Sev 2).

## Exemplo
```bash
# Auditar especificamente Services, Endpoints, HPAs e PDBs de produção em busca de referências quebradas ou riscos de capacidade
popeye -n producao -s svc,hpa,pdb,pvc --logs none
```

## Limites e trade-offs
Os códigos `602`–`605` (verificação de burst de HPA contra a capacidade atual do cluster) comparam o `maxReplicas` dos HPAs com os nós atualmente presentes no cluster; em clusters com Cluster Autoscaler ou Karpenter configurados para provisionar novos nós sob demanda, esse aviso serve como estimativa do crescimento necessário da frota de nós.

## Como verificar
Execute `popeye -A -s hpa,svc,pdb` e verifique se existem ocorrências dos códigos `600`/`601`, `901`, `1100`, `1105` ou `1106`.

## Conexões
- [[popeye-codigos-erro-severidades-containers-pods-seguranca]] — Veja também: Níveis de severidade (0 a 3) e códigos de erro do Popeye para Containers (100–113), Pods (200–209) e Segurança (300–308).
- [[popeye-configuracao-spinach-yaml-allocations-excludes-overrides]] — Veja também: Configuração avançada do Popeye com SpinachYAML (-f spinach.yaml): allocations, excludes, FQN, rx:, overrides e registries.
- [[popeye-catalogo-linters-recursos-aliases-selecao]] — Referência cruzada direta com popeye-catalogo-linters-recursos-aliases-selecao.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://popeyecli.io/docs/codes.html) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
