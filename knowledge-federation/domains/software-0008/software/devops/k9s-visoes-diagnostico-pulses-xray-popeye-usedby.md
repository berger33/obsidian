---
id: software.devops.tranche10.000984
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/derailed/k9s/master/README.md", "https://k9scli.io/topics/commands/", "https://github.com/derailed/k9s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K9s: visões integradas de diagnóstico de saúde e topologia (:pulses, :xray, :popeye, UsedBy u e Jump to Owner SHIFT-J)

## Em uma frase
O K9s inclui visões analíticas especiais além das tabelas padrão de recursos: **`:pulses`** (`:pu`, painel de sinais vitais do cluster), **`:xray RESOURCE [NAMESPACE]`** (árvore hierárquica de dependências ao vivo), **`:popeye`** (`:pop`, auditoria de sanitização e boas práticas) e navegação relacional com **`u` (`UsedBy`)** e **`Shift-j` (`Jump to owner`)**.

## Por que importa
Em tabelas planas, é difícil responder rapidamente *"Quais Pods estão montando este Secret ou esta ServiceAccount?"* ou visualizar em uma única árvore como um `Deployment` se conecta aos seus `ReplicaSet`s, `Pod`s, `Container`s, `Service`s, `ConfigMap`s e `Secret`s. As visões `:xray`, `:pulses`, `:popeye` e o atalho `u` (`UsedBy`) resolvem isso diretamente no terminal.

## Como funciona
Conforme documenta a tabela `Key Bindings` do README oficial: (1) **`:pulses` (ou `:pu`)**: exibe um dashboard dinâmico em ASCII com gráficos de saúde de Deployments, ReplicaSets, Pods, consumo de CPU/Memória e eventos do cluster; (2) **`:xray RESOURCE [NAMESPACE]`** (onde `RESOURCE` pode ser `po`, `svc`, `dp`, `rs`, `sts`, `ds`): renderiza uma árvore interativa mostrando cada objeto e todas as suas referências filhas (pods -> containers -> secrets/configmaps/pvcs); (3) **`:popeye` (ou `:pop`)**: executa o sanitizador de cluster **Popeye** embutido no K9s, atribuindo notas (score de 0 a 100) e apontando configurações inseguras, recursos sem limites de CPU/RAM, portas órfãs ou imagens `:latest`; e (4) **`u` (`UsedBy`) e `Shift-j`**: pressionar `u` sobre uma `ServiceAccount`, `PVC`, `Secret` ou `ConfigMap` lista todos os recursos que o utilizam, enquanto `Shift-j` salta para o recurso pai (`ownerReference`).

## Exemplo
```text
# Comandos de visões especiais de diagnóstico e topologia digitados no prompt (:) do K9s
:pulses
:xray dp default
:popeye
```

## Limites e trade-offs
Em clusters muito grandes (com milhares de pods e dezenas de namespaces), abrir a visão `:xray po` em todos os namespaces simultaneamente exige que o K9s correlacione em memória toda a árvore de `Pod` -> `ServiceAccount` -> `Secret` -> `ConfigMap` -> `PVC`; para manter a árvore legível e responsiva, passe o namespace desejado ao comando (ex.: `:xray dp meu-namespace`).

## Como verificar
No K9s, navegue até `:secrets` (`:sec`), selecione um Secret usado por uma aplicação e pressione a tecla `u` (`UsedBy`) para listar imediatamente quais Pods referenciam aquele Secret.

## Conexões
- [[k9s-atalhos-operacao-logs-shell-port-forward-benchmark]] — Veja também: K9s: atalhos de operação em recursos (YAML y, Describe d, Edit e, Logs l/p, Shell s, Port-Forward SHIFT-F e Benchmark b).
- [[k9s-configuracao-xdg-diretorios-logs-debug-screendumps]] — Veja também: K9s: estrutura de diretórios XDG (config.yaml, clusters, screendumps), logs de debug (-l debug) e variável K9S_CONFIG_DIR.
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Referência cruzada direta com k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes.
- [[k9s-navegacao-modo-comando-filtros-regex-labels-contextos]] — Referência cruzada direta com k9s-navegacao-modo-comando-filtros-regex-labels-contextos.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
