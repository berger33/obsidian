---
id: software.devops.tranche10.000989
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

# K9s: disparo manual de CronJobs (t), inspeção e Rollback de ReplicaSets (z / CTRL-L) e variável K9S_DEFAULT_PF_ADDRESS

## Em uma frase
Para operações diárias de workloads, o K9s permite disparar um `Job` imediato a partir de um `CronJob` selecionando-o e pressionando **`t` (`Trigger`)**, fazer rollback de um `Deployment` para um `ReplicaSet` anterior com **`z`** + **`Ctrl-l`** e definir o endereço padrão de Port-Forward via **`K9S_DEFAULT_PF_ADDRESS`**.

## Por que importa
Testar um `CronJob` que só rodaria às 03:00 da manhã exige normalmente digitar `kubectl create job --from=cronjob/<nome> <nome-manual> -n <ns>`; da mesma forma, reverter um deploy problemático para uma revisão específica exige consultar `kubectl rollout history`. No K9s, ambas as ações são visuais e levam uma única tecla.

## Como funciona
Conforme especifica a tabela `Key Bindings` e a seção `K9s Configuration` do README oficial: (1) **Trigger de CronJob (`:cj`)**: na visão de CronJobs, selecionar o CronJob desejado e pressionar **`t`** cria imediatamente uma execução manual de `Job` no cluster; (2) **Inspeção de ReplicaSets e Rollback**: na visão de Deployments (`:dp`), pressionar **`z`** abre os `ReplicaSet`s daquele Deployment (mostrando a imagem e o número de réplicas de cada revisão histórica), e pressionar **`Ctrl-l`** executa o rollback do recurso; e (3) **Endereço de Port-Forward (`K9S_DEFAULT_PF_ADDRESS`)**: exportar `K9S_DEFAULT_PF_ADDRESS=0.0.0.0` (ou um IP de interface específico `a.b.c.d`) sobrescreve o endereço local padrão (`localhost`) ao abrir túneis com `Shift-f`.

## Exemplo
```bash
# Definir o endereço padrão de bind para todos os Port-Forwards abertos no K9s e iniciar na visão de CronJobs
export K9S_DEFAULT_PF_ADDRESS="127.0.0.1"
k9s -c cj
```

## Limites e trade-offs
Tenha cuidado ao definir `K9S_DEFAULT_PF_ADDRESS=0.0.0.0` em um laptop conectado a uma rede Wi-Fi pública ou compartilhada: ao fazer `Shift-f` (Port-Forward) para um banco de dados ou serviço interno sem autenticação do cluster, fazer bind em `0.0.0.0` expõe aquela porta na interface de rede da sua máquina para outros dispositivos na mesma rede local; mantenha `127.0.0.1` a menos que precise acessar a porta a partir de uma VM/container local.

## Como verificar
Navegue até `:cj` (CronJobs) em um ambiente de desenvolvimento, pressione `t` sobre um CronJob e pressione `Enter` sobre o CronJob para ver o novo `Job` criado em execução.

## Conexões
- [[k9s-execucao-container-docker-build-multiplataforma-compatibilidade]] — Veja também: K9s: execução via container Docker (derailed/k9s), compilação com KUBECTL_VERSION e matriz de compatibilidade Kubernetes.
- [[k9s-navegacao-contextual-warp-namespace-breadcrumbs-cabecalho]] — Veja também: K9s: navegação rápida entre namespaces (Warp w e Use u) e controle de layout da TUI (Header CTRL-E, Crumbs CTRL-G).
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Referência cruzada direta com k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes.
- [[k9s-atalhos-operacao-logs-shell-port-forward-benchmark]] — Referência cruzada direta com k9s-atalhos-operacao-logs-shell-port-forward-benchmark.
- [[k9s-configuracao-xdg-diretorios-logs-debug-screendumps]] — Referência cruzada direta com k9s-configuracao-xdg-diretorios-logs-debug-screendumps.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
