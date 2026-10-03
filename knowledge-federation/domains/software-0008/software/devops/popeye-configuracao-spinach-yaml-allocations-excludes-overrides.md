---
id: software.devops.tranche11.001075
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

# Configuração avançada do Popeye com SpinachYAML (-f spinach.yaml): allocations, excludes, FQN, rx:, overrides e registries

## Em uma frase
O arquivo de configuração **SpinachYAML** (`popeye -f spinach.yaml`) permite calibrar limiares de sobre/subalocação de CPU e memória (`allocations`), limites de nós e restarts de pods (`resources`), listas de registros de imagens permitidos (`registries`), sobrescrita de severidade de códigos (`overrides`) e regras de exclusão globais ou por linter (`excludes`) usando nomes totalmente qualificados (**FQN** `namespace/resource_name`) e expressões regulares com o prefixo **`rx:`**.

## Por que importa
Em qualquer cluster Kubernetes real, namespaces de sistema como `kube-system` e `kube-public` possuem DaemonSets privilegiados e usa-se `hostNetwork` por design. Sem um arquivo `spinach.yaml` para excluir recursos de sistema e calibrar limiares, o relatório do Popeye fica poluído por falsos positivos que mascaram erros reais nas aplicações de negócio.

## Como funciona
Conforme a seção *SpinachYAML* do README oficial (`derailed/popeye`): (1) **`allocations.cpu` e `allocations.memory`** definem `underPercUtilization` (ex.: `200`%) e `overPercUtilization` (ex.: `50`%); (2) **`excludes.global`** e **`excludes.linters.<plural_kind_lowercase>`** filtram recursos por **`fqns`** (`namespace/resource_name` para recursos namespaced, ou `name` para recursos cluster-wide), `labels`, `annotations` e `codes` — suportando correspondência exata ou regex precedida por **`rx:`** (ex.: `rx:^kube-`); (3) **`resources.node.limits`** (`cpu: 90`, `memory: 80`) e **`resources.pod`** (`restarts: 3`, `limits: { cpu: 80, memory: 75 }`) ajustam os gatilhos de alerta; (4) **`overrides`** altera a severidade de códigos específicos (`1`, `2` ou `3`); e (5) **`registries`** lista os registros de container permitidos (acionando o código `113` para imagens fora da lista).

## Exemplo
```yaml
# Exemplo de arquivo spinach.yaml calibrando alocações, excluindo namespaces kube-* via regex (rx:) e restringindo registries
popeye:
  allocations:
    cpu:
      underPercUtilization: 200
      overPercUtilization: 50
    memory:
      underPercUtilization: 200
      overPercUtilization: 50
  excludes:
    global:
      fqns: ["rx:^kube-"]
      codes: ["300", "206"]
    linters:
      pods:
        instances:
          - labels:
              app: [legado]
            codes: [102, 105]
  resources:
    node:
      limits:
        cpu: 90
        memory: 80
    pod:
      restarts: 3
      limits:
        cpu: 80
        memory: 75
  overrides:
    - code: 206
      severity: 1
  registries:
    - quay.io
    - docker.io
    - ghcr.io
```

## Limites e trade-offs
A documentação oficial alerta para ter cuidado com expressões regulares (`rx:`) frouxas em `excludes`, pois elas podem ocultar mais recursos do que o planejado; por isso, recomenda-se rodar o Popeye *"wide open"* (sem `-f spinach.yaml`) periodicamente para garantir que novos problemas não estejam sendo mascarados.

## Como verificar
Execute `popeye -A -f spinach.yaml` e confirme que os namespaces `kube-system` e `kube-public` foram filtrados pelas regras `rx:^kube-` e que imagens fora de `registries` acionam o código `113`.

## Conexões
- [[popeye-codigos-workloads-hpa-nodes-services-networkpolicies]] — Veja também: Códigos de diagnóstico do Popeye para Geral (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PV/PVC (1000–1004), Services (1100–1110) e NetworkPolicies (1200–1206).
- [[popeye-formatos-saida-html-json-junit-prometheus-score]] — Veja também: Formatos de saída do Popeye (-o): standard, jurassic, yaml, html, json, junit, prometheus e score.
- [[popeye-linter-cluster-kubernetes-vivo-readonly]] — Referência cruzada direta com popeye-linter-cluster-kubernetes-vivo-readonly.
- [[popeye-codigos-erro-severidades-containers-pods-seguranca]] — Referência cruzada direta com popeye-codigos-erro-severidades-containers-pods-seguranca.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
