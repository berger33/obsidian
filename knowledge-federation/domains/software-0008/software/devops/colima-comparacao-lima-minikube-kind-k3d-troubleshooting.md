---
id: software.devops.tranche15.001450
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
fontes: ["https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md", "https://raw.githubusercontent.com/abiosoft/colima/main/README.md", "https://github.com/abiosoft/colima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Colima: comparação arquitetural com Lima, Minikube, kind e k3d e resolução de problemas comuns

## Em uma frase
Para cargas de trabalho híbridas de Docker e Kubernetes local, o Colima diferencia-se do `kind` e do `k3d` por rodar um ambiente completo em VM sem depender de um Docker Desktop preexistente, e do `minikube` por expor simultaneamente o runtime de containers como cidadão de primeira classe.

## Por que importa
Enquanto `kind` e `k3d` rodam nós Kubernetes dentro de containers Docker (exigindo que no macOS já exista uma VM como o próprio Colima ou Docker Desktop por baixo), o Colima fornece tanto a VM base quanto o runtime Docker/containerd e o cluster Kubernetes integrados.

## Como funciona
Em caso de falhas após upgrades ou estado `Broken` em `colima list`, o fluxo de diagnóstico utiliza `colima status`, inspeção de logs de inicialização, verificação do plugin `docker-buildx` no `~/.docker/cli-plugins` e, quando necessário, redefinição limpa do runtime mantendo ou recriando o perfil.

## Exemplo
```bash
colima status
docker buildx version
colima ssh -- df -h
```

## Limites e trade-offs
No macOS com Homebrew, o pacote `docker` instala apenas a CLI sem o plugin `buildx`; para usar `docker buildx` ou `docker compose build` com BuildKit no Colima, instale `docker-buildx` e configure `cliPluginsExtraDirs` ou o symlink em `~/.docker/cli-plugins`.

## Como verificar
Execute `colima status` e `docker buildx ls` para validar que o cliente Docker e o builder estão operacionais sobre o contexto `colima`.

## Conexões
- [[colima-lima-overrides-provision-scripts-atualizacao-runtime]] — Veja também: Colima: scripts de provisionamento customizados (`provision`), overrides do Lima e atualização de runtimes.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
