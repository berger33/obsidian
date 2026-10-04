---
id: software.devops.tranche11.001072
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
fontes: ["https://raw.githubusercontent.com/derailed/popeye/master/README.md", "https://popeyecli.io/docs/codes.html", "https://github.com/derailed/popeye"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Catálogo de Linters do Popeye: recursos auditados, aliases de CLI (-s) e detecção de recursos órfãos

## Em uma frase
O Popeye possui linters dedicados para mais de 20 tipos de recursos do Kubernetes — selecionáveis individualmente na CLI pela flag **`-s`** usando seus nomes ou aliases curtos (`no`, `ns`, `po`, `svc`, `sa`, `sec`, `cm`, `dp`, `sts`, `ds`, `pv`, `pvc`, `hpa`, `pdb`, `cr`, `crb`, `ro`, `rb`, `ing`, `np`, `cj`, `job`, `gwc`, `gw`, `gwr`).

## Por que importa
Durante a investigação de um problema específico (por exemplo, revisar apenas `Services`, `Pods` e `NetworkPolicies` de um namespace, ou fazer uma faxina de `Secrets`, `ConfigMaps` e `ServiceAccounts` não utilizados), rodar apenas os linters desejados com `popeye -n <ns> -s po,svc,np` acelera o diagnóstico e reduz o ruído no console.

## Como funciona
Conforme a tabela oficial *Linters* do README (`derailed/popeye`), cada linter inspeciona aspectos específicos do recurso vivo e suas referências cruzadas: (1) **Node (`no`)**: condições de prontidão, pressão de disco/memória/PIDs, tolerations de pods referenciando taints e utilização > 80%; (2) **Namespace (`ns`)**: namespaces inativos ou mortos; (3) **Pod (`po`)** e **Workloads (`dp`, `sts`, `ds`, `cj`, `job`)**: status de containers, imagens sem tag ou com `:latest`, ausência de probes e requests/limits, portas nomeadas e utilização de CPU/MEM; (4) **Service (`svc`)**: presença de `Endpoints`, correspondência de labels de pods e portas nomeadas; (5) **Higiene de referências (`sa`, `sec`, `cm`, `pv`, `pvc`, `cr`, `crb`, `ro`, `rb`, `pdb`)**: detecta `ServiceAccounts`, `Secrets` (ou chaves específicas), `ConfigMaps`, volumes e papéis RBAC potencialmente **não utilizados (`Unused`)**; e (6) **Rede e Gateway API (`ing`, `np`, `gwc`, `gw`, `gwr`)**: valida `Ingress`, `NetworkPolicy` (incluindo políticas stale), `GatewayClass`, `Gateway` e `HTTPRoute`.

## Exemplo
```bash
# Executar o Popeye no namespace ns1 filtrando apenas os linters de Pod (po), Service (svc) e Secret (sec) sem gravar arquivo de log
popeye -n ns1 -s po,svc,sec --logs none
```

## Limites e trade-offs
Quando o Popeye reporta um `Secret` (`sec`), `ConfigMap` (`cm`) ou `ServiceAccount` (`sa`) como potencialmente não utilizado (códigos `400` / `401`), lembre-se de que o Popeye verifica referências declarativas nos recursos do cluster; se uma aplicação ler um `ConfigMap` ou `Secret` dinamicamente fazendo chamadas diretas à API do Kubernetes em tempo de execução (sem montá-lo em `volumes` ou `env`), o linter poderá marcá-lo como `Unused`.

## Como verificar
Execute `popeye -n kube-system -s no,po --logs none` para auditar rapidamente apenas a saúde dos nós e dos pods do plano de controle.

## Conexões
- [[popeye-linter-cluster-kubernetes-vivo-readonly]] — Veja também: Popeye: sanitizador e linter somente-leitura para clusters Kubernetes vivos.
- [[popeye-codigos-erro-severidades-containers-pods-seguranca]] — Veja também: Níveis de severidade (0 a 3) e códigos de erro do Popeye para Containers (100–113), Pods (200–209) e Segurança (300–308).
- [[popeye-configuracao-spinach-yaml-allocations-excludes-overrides]] — Referência cruzada direta com popeye-configuracao-spinach-yaml-allocations-excludes-overrides.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
