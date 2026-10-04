---
id: software.devops.tranche15.001442
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

# Colima: seleção de runtimes (`docker`, `containerd` com `nerdctl` e `incus`) na inicialização da instância

## Em uma frase
A flag `--runtime` do comando `colima start` permite escolher o motor de execução da instância entre `docker` (padrão), `containerd` e `incus` (suportado desde a `v0.7.0`).

## Por que importa
Permite que engenheiros testem workloads tanto com a API clássica do Docker quanto diretamente sobre `containerd`/`nerdctl` (mesmo runtime do Kubernetes) ou em containers de sistema e máquinas virtuais gerenciados pelo Incus.

## Como funciona
Com `colima start --runtime containerd`, o Colima inicia o `containerd` e disponibiliza o subcomando `colima nerdctl` (podendo instalar um script alias global no `$PATH` com `colima nerdctl install`). Já com `colima start --runtime incus`, configura automaticamente o cliente local `incus` no host para lançar instâncias Alpine, Debian ou Ubuntu.

## Exemplo
```bash
colima start --runtime containerd
colima nerdctl install
nerdctl run --rm alpine uname -a
```

## Limites e trade-offs
No runtime `incus` em macOS, a execução de máquinas virtuais aninhadas (`incus launch ... --vm`) só é suportada em processadores Apple Silicon M3 ou mais recentes que expõem virtualização aninhada em hardware.

## Como verificar
Execute `colima list` para verificar a coluna `RUNTIME` de cada perfil provisionado na máquina.

## Conexões
- [[colima-arquitetura-containers-on-lima-docker-containerd-incus]] — Veja também: Colima: arquitetura de runtimes de containers no macOS e Linux sobre Lima com configuração mínima.
- [[colima-kubernetes-integrado-compartilhamento-imagens-k8s-io]] — Veja também: Colima: cluster Kubernetes local (`--kubernetes`) e compartilhamento direto de imagens com Docker e containerd.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
