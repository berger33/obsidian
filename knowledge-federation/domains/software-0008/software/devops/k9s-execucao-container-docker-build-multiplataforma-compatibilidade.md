---
id: software.devops.tranche10.000988
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

# K9s: execução via container Docker (derailed/k9s), compilação com KUBECTL_VERSION e matriz de compatibilidade Kubernetes

## Em uma frase
O K9s pode ser executado diretamente como um container Docker montando o arquivo `~/.kube/config` (`docker run --rm -it -v ~/.kube/config:/root/.kube/config derailed/k9s`), compilado do código-fonte em Go 1.23+ (`make build` / `make imgx`) e customizado com a versão exata do `kubectl` (`--build-arg KUBECTL_VERSION`).

## Por que importa
Em máquinas bastion de emergência ou ambientes onde você não quer instalar pacotes locais, rodar a imagem oficial `derailed/k9s` via Docker (ou como extensão do Docker Desktop `spurin/k9s-dd-extension:latest`) entrega a TUI completa instantaneamente junto com o binário `kubectl` embutido para shells e plugins.

## Como funciona
Conforme documentam as seções `Building From Source`, `Running with Docker` e `K8S Compatibility Matrix` do README oficial: (1) **Execução em Docker**: basta montar `$KUBECONFIG` em `/root/.kube/config` no container `derailed/k9s`; (2) **Build customizado da imagem**: o `Dockerfile` oficial aceita `--build-arg KUBECTL_VERSION=${KUBECTL_VERSION}` (obtido via `make kubectl-stable-version`) para embutir a versão exata do cliente `kubectl` compatível com seu cluster, e o alvo **`make imgx`** constrói imagens multiplataforma (`linux/amd64` e `linux/arm64`) via Docker buildx; e (3) **Compatibilidade**: o K9s prefere versões recentes do Kubernetes (`1.28+`, mantendo retrocompatibilidade documentada na matriz de cliente `1.26.1+` para `k9s >= v0.27.0`).

## Exemplo
```bash
# Executar a imagem oficial do K9s via Docker montando o KUBECONFIG atual do usuário
docker run --rm -it -v "${KUBECONFIG:-$HOME/.kube/config}:/root/.kube/config" derailed/k9s
```

## Limites e trade-offs
Quando você executa o K9s dentro de um container Docker (`docker run ... derailed/k9s`) apontando para um cluster local (como `kind` ou `minikube` cujo `server:` no `~/.kube/config` aponta para `https://127.0.0.1:<porta>`), dentro do container do K9s o endereço `127.0.0.1` refere-se ao próprio container e não ao host; adicione `--network host` ao comando `docker run` no Linux para que o container do K9s alcance a porta local do API Server.

## Como verificar
Verifique a versão do cliente e do servidor reportada por `k9s version` confirmando o alinhamento com a versão do seu cluster Kubernetes.

## Conexões
- [[k9s-ordenacao-colunas-marcacao-lote-operacoes-nodes]] — Veja também: K9s: ordenação de colunas (SHIFT-N/A/S/O), seleção múltipla em lote (SPACE / CTRL-SPACE) e operações de Node (cordon/drain).
- [[k9s-gerenciamento-port-forwards-cronjobs-replicasets-rollback]] — Veja também: K9s: disparo manual de CronJobs (t), inspeção e Rollback de ReplicaSets (z / CTRL-L) e variável K9S_DEFAULT_PF_ADDRESS.
- [[k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes]] — Referência cruzada direta com k9s-interface-terminal-tui-gerenciamento-clusters-kubernetes.
- [[k9s-configuracao-xdg-diretorios-logs-debug-screendumps]] — Referência cruzada direta com k9s-configuracao-xdg-diretorios-logs-debug-screendumps.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [K9s GitHub — README.md (Installation, Docker Image, PreFlight Checks, Compatibility Matrix, XDG Config, Key Bindings & Pulses/XRay/Popeye)](https://raw.githubusercontent.com/derailed/k9s/master/README.md) — README oficial do derailed/k9s (Apache-2.0) documentando instalação, execução em Docker, matriz de compatibilidade, estrutura XDG (k9s info), modo --readonly, filtros regex/labels e visões :pulses, :xray e :popeye; consultado em 2026-10-03.
- [K9s Official Documentation — CLI Arguments & Key Bindings Reference (k9scli.io/topics/commands/)](https://k9scli.io/topics/commands/) — Referência oficial de argumentos de linha de comando e atalhos de teclado do K9s; consultado em 2026-10-03.
- [K9s — Official GitHub Repository](https://github.com/derailed/k9s) — Repositório oficial Apache-2.0 do K9s; consultado em 2026-10-03.
