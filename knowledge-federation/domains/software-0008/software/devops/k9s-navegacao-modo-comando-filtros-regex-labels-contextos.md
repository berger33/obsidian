---
id: software.devops.tranche10.000982
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

# K9s: modo de comando (:pod, :ctx, :ns) e filtragem avançada por Regex (/), inversa (/!), Labels (/-l) e Fuzzy (/-f)

## Em uma frase
No K9s, pressionar **`:`** abre o modo de comando para saltar para qualquer recurso Kubernetes (por nome singular, plural, short-name ou alias, combinável com namespace, filtro, labels ou `@contexto`), enquanto pressionar **`/`** filtra a visão atual por expressão regular, regex inversa (`/!`), seletor de labels (`/-l`) ou busca fuzzy (`/-f`).

## Por que importa
Em clusters com centenas de CRDs e milhares de pods distribuídos em dezenas de namespaces, rolar listas manualmente com as setas do teclado é inviável; dominar a gramática de comandos `:` e filtros `/` do K9s (documentada na tabela `Key Bindings` do README oficial e em `k9scli.io/topics/commands/`) permite localizar qualquer pod em menos de 2 segundos.

## Como funciona
Conforme especifica a tabela oficial de `Key Bindings` (incluindo os recursos introduzidos no K9s v0.30.0+): (1) **Navegação por recurso (`:`)**: `:pod` (ou `:po`, `:deploy`, `:svc`, `:crd`, ou `ctrl-a` para ver todos os aliases); (2) **Argumentos diretos no comando `:pod`**: `:pod ns-x` abre os pods do namespace `ns-x`; **`:pod /fred`** já abre os pods filtrados por `fred`; **`:pod app=fred,env=dev`** filtra por labels; e **`:pod @ctx1`** alterna imediatamente para o contexto `ctx1` exibindo seus pods; (3) **Filtros na visão (`/`)**: `/fred|blee` filtra usando Regex2; **`/! filter`** aplica filtro regex inverso (mantendo tudo que *não* casa); **`/-l app=web`** filtra por label selector; e **`/-f texto`** faz busca fuzzy; e (4) **Histórico de comandos**: `-` alterna para o último comando ativo (como `cd -`), e `[` / `]` navegam para trás e para frente no histórico.

## Exemplo
```text
# Exemplos de comandos interativos (:) e filtros (/) digitados dentro da interface do K9s
:pod app=checkout,env=prod
:deploy @staging-cluster
/!Running|Completed
/-l tier=backend
```

## Limites e trade-offs
O filtro inverso **`/! Running|Completed`** é uma das ferramentas mais rápidas para triagem de incidentes no K9s: em uma visão com 800 pods em todos os namespaces (`:pod all`), digitar `/!Running|Completed` oculta instantaneamente todos os pods saudáveis e deixa na tela apenas pods em `CrashLoopBackOff`, `Pending`, `Error` ou `ImagePullBackOff` (ou pressione `ctrl-z` para alternar a exibição de falhas/erros).

## Como verificar
Dentro do K9s, pressione `ctrl-a` para listar todos os aliases de recursos disponíveis no cluster (incluindo CRDs instalados) e pressione `?` para ver o menu de ajuda contextual da tela atual.

## Conexões
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Veja também: K9s: interface de terminal (TUI) interativa em tempo real para observação e gerenciamento de clusters Kubernetes.
- [[k9s-atalhos-operacao-logs-shell-port-forward-benchmark]] — Veja também: K9s: atalhos de operação em recursos (YAML y, Describe d, Edit e, Logs l/p, Shell s, Port-Forward SHIFT-F e Benchmark b).
- [[k9s-visoes-diagnostico-pulses-xray-popeye-usedby]] — Referência cruzada direta com k9s-visoes-diagnostico-pulses-xray-popeye-usedby.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
