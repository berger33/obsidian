---
id: software.devops.tranche10.000981
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

# K9s: interface de terminal (TUI) interativa em tempo real para observação e gerenciamento de clusters Kubernetes

## Em uma frase
O **K9s** (`derailed/k9s`, licenciado sob Apache-2.0 e documentado em `k9scli.io`) fornece uma interface de usuário em terminal (TUI) de 256 cores que observa continuamente os recursos do cluster Kubernetes em tempo real e oferece atalhos de teclado diretos para inspecionar, filtrar, editar e depurar aplicações.

## Por que importa
Durante um incidente em produção, digitar repetidamente comandos longos como `kubectl get pods -n meu-namespace -o wide`, copiar o nome do pod com o mouse, digitar `kubectl logs -f <pod> -c <container>` e depois `kubectl describe pod <pod>` desperdiça segundos preciosos. Segundo o README oficial, o K9s torna muito mais rápido navegar, observar e gerenciar aplicações Kubernetes sem sair do terminal.

## Como funciona
O K9s conecta-se ao API Server do Kubernetes usando o `KUBECONFIG` padrão da máquina e mantém *informers/watches* ativos sobre os recursos observados, atualizando a tela em tempo real. Conforme documenta a seção `PreFlight Checks` e `The Command Line` do README oficial: (1) requer um terminal com suporte a 256 cores (`export TERM=xterm-256color`) e usa as variáveis `KUBE_EDITOR` / `EDITOR` para edição de manifestos; (2) pode ser iniciado diretamente em um namespace específico (`k9s -n mycoolns`), em um contexto específico (`k9s --context coolCtx`) ou em uma visão inicial (`k9s -c pod`); e (3) suporta modo somente-leitura (**`k9s --readonly`**), onde todos os comandos que modificam ou apagam recursos do cluster ficam desabilitados.

## Exemplo
```bash
# Verificar caminhos de configuração/logs do K9s e iniciar a TUI em modo somente-leitura (--readonly) para produção
k9s info
k9s --context prod-cluster -n payments --readonly
```

## Limites e trade-offs
Ao conectar-se a clusters de **produção** apenas para investigar logs, eventos ou consumo de CPU/memória, inicie sempre o K9s com a flag **`k9s --readonly`**: isso evita que um atalho pressionado por engano no teclado (como `Ctrl-k` que mata um recurso sem pedir confirmação!) apague um pod ou deployment de produção.

## Como verificar
Execute `k9s version` e `k9s info` no terminal para verificar a versão instalada e os caminhos exatos onde o K9s armazena `config.yaml`, `k9s.log`, `skins`, `plugins.yaml` e `views.yaml`.

## Conexões
- [[k9s-navegacao-modo-comando-filtros-regex-labels-contextos]] — Veja também: K9s: modo de comando (:pod, :ctx, :ns) e filtragem avançada por Regex (/), inversa (/!), Labels (/-l) e Fuzzy (/-f).
- [[k9s-atalhos-operacao-logs-shell-port-forward-benchmark]] — Referência cruzada direta com k9s-atalhos-operacao-logs-shell-port-forward-benchmark.
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
