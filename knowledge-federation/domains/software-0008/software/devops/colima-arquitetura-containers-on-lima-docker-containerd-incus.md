---
id: software.devops.tranche15.001441
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/abiosoft/colima/main/README.md", "https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md", "https://github.com/abiosoft/colima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Colima: arquitetura de runtimes de containers no macOS e Linux sobre Lima com configuração mínima

## Em uma frase
O Colima (*Containers on Lima*, licença MIT) é uma CLI em Go que abstrai o Lima para entregar runtimes prontos de Docker, containerd, Kubernetes e Incus em macOS (Intel e Apple Silicon) e Linux com um único comando.

## Por que importa
Enquanto o Lima é um gerenciador genérico de máquinas virtuais Linux, o Colima automatiza a criação de contextos do cliente (`docker context`, `kubeconfig`, `incus remote`), encaminhamento de portas, montagem de volumes e instalação de aliases sem exigir configuração manual de sockets.

## Como funciona
Na primeira execução de `colima start`, o Colima provisiona uma VM padrão (2 vCPUs, 2 GiB de RAM e 100 GiB de disco) com o runtime Docker pré-configurado e ativa automaticamente o contexto `colima` no cliente `docker` da máquina host, permitindo rodar `docker run` imediatamente e coexistir lado a lado com o Docker Desktop.

## Exemplo
```bash
colima start
colima status
docker context ls
docker run --rm hello-world
```

## Limites e trade-offs
O Colima fornece o daemon/runtime dentro da VM Linux, mas requer que o binário cliente correspondente (`docker`, `kubectl` ou `incus`) esteja instalado no sistema operacional host (por exemplo via `brew install docker kubectl`).

## Como verificar
Execute `colima status` e `docker context ls` para confirmar que o contexto `colima` está marcado com `*` (ativo) e apontando para o socket gerenciado em `~/.colima`.

## Conexões
- [[colima-runtimes-docker-containerd-nerdctl-incus-selecao]] — Veja também: Colima: seleção de runtimes (`docker`, `containerd` com `nerdctl` e `incus`) na inicialização da instância.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
