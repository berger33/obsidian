---
id: software.devops.tranche11.001080
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

# Integração nativa do Popeye com o K9s (:popeye) e diagnóstico de problemas operacionais de linha de comando

## Em uma frase
O Popeye compartilha sua engine de sanitização diretamente com a visão interativa **`:popeye`** dentro do **K9s** e dispõe de opções de linha de comando para seleção de contexto (`--context`), controle de arquivo de logs (`--logs /tmp/scan.log` ou `--logs none`) e níveis de verbosidade (`-v4`) para depuração.

## Por que importa
Engenheiros que já operam o cluster diariamente pelo K9s podem invocar a auditoria do Popeye instantaneamente sem sair da TUI (`:popeye`), enquanto engenheiros de plataforma podem usar o binário standalone `popeye` com `--logs` e `-v4` para investigar falhas de conectividade ou lentidão na API do Kubernetes.

## Como funciona
Conforme documentam os READMEs oficiais do Popeye (`derailed/popeye`) e do K9s (`derailed/k9s`): (1) por padrão, rodar `popeye` sem argumentos usa o contexto e o namespace ativos do `kubeconfig` (ou `default`); (2) `--context <nome>` seleciona explicitamente o contexto do `kubeconfig`; (3) `-n <namespace>` audita um namespace específico e `-A` audita todos os namespaces; (4) `--logs none` desativa a gravação de arquivo de log, enquanto `--logs /tmp/fred.log -v4` grava logs detalhados de nível debug no caminho indicado; e (5) dentro do K9s, digitar `:popeye` (ou `:pop`) abre a visão interativa de sanitização que lista a pontuação e os códigos `[POP-xxx]` de cada recurso vivo.

## Exemplo
```bash
# Executar o Popeye em um contexto específico do kubeconfig com log de depuração (-v4) em arquivo dedicado
popeye --context prod-cluster -n pagamentos --logs /tmp/popeye-debug.log -v4

# Verificar a versão e a localização padrão dos arquivos de log do Popeye
popeye version
```

## Limites e trade-offs
Ao executar `popeye` sem as flags `-n` ou `-A`, ele auditará **apenas o namespace definido no seu contexto atual do `kubeconfig`** (ou `default`), exactamente como o `kubectl`; para auditar o cluster inteiro, lembre-se sempre de passar explicitamente `-A`.

## Como verificar
Execute `popeye version` para conferir o caminho padrão de logs e rode `popeye -n default --logs none` confirmando a execução limpa no terminal.

## Conexões
- [[popeye-execucao-in-cluster-cronjob-rbac-force-exit-zero]] — Veja também: Execução do Popeye in-cluster via CronJob Kubernetes, flag --force-exit-zero e perfil RBAC somente-leitura.
- [[popeye-linter-cluster-kubernetes-vivo-readonly]] — Referência cruzada direta com popeye-linter-cluster-kubernetes-vivo-readonly.
- [[k9s-visoes-diagnostico-pulses-xray-popeye-usedby]] — Referência cruzada direta com k9s-visoes-diagnostico-pulses-xray-popeye-usedby.
- [[popeye-catalogo-linters-recursos-aliases-selecao]] — Referência cruzada direta com popeye-catalogo-linters-recursos-aliases-selecao.

## Fontes
- [Popeye GitHub — README.md (Live Cluster Linter, Resource Linters Table, SpinachYAML, Output Formats, S3/MinIO, Prometheus & CronJob RBAC)](https://raw.githubusercontent.com/derailed/popeye/master/README.md) — README oficial do derailed/popeye (Apache-2.0) detalhando linters e aliases, arquivo spinach.yaml (allocations, excludes, FQN, rx:, overrides, registries), formatos de saída (-o), upload S3/MinIO, métricas Pushgateway e CronJob in-cluster (--force-exit-zero); consultado em 2026-10-03.
- [Popeye Official Documentation — Error Codes Reference (popeyecli.io/docs/codes.html)](https://popeyecli.io/docs/codes.html) — Tabela oficial completa de códigos de erro e níveis de severidade (0 a 3) do Popeye para Containers (100–113), Pods (200–209), Security (300–308), General (400–407), Workloads (500–508), HPA (600–605), Nodes (700–712), PDB, PV/PVC, Services e NetworkPolicies; consultado em 2026-10-03.
- [Popeye — Official GitHub Repository](https://github.com/derailed/popeye) — Repositório oficial do Popeye; consultado em 2026-10-03.
