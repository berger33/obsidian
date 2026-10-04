---
id: software.devops.tranche02.000138
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md", "https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Registro oficial cr.l5d.io/linkerd e fluxo de build local com k3d e buildx

## Em uma frase
As subseções `Comprehensive` e `Publishing images` de `BUILD.md` mostram como construir todas as imagens Docker localmente (`bin/docker-build`, exigindo `docker buildx`), carregá-las em um cluster `k3d` (`bin/k3d cluster create` e `bin/image-load --k3d`) ou publicá-las em um registro externo configurando a variável de ambiente `DOCKER_REGISTRY`, que por padrão aponta para o registro oficial `cr.l5d.io/linkerd`.

## Por que importa
Ambientes corporativos air-gapped ou com políticas estritas de egress precisam espelhar as imagens do registro padrão `cr.l5d.io/linkerd` para um registro interno (como o Harbor) ou sobrescrever `DOCKER_REGISTRY` ao construir imagens customizadas.

## Como funciona
Ao operar clusters sem acesso direto à internet pública, replique as imagens oficiais de `cr.l5d.io/linkerd` para o registro privado da organização e configure os Helm charts ou flags de instalação para consumir o registro interno.

## Exemplo
Uma equipe testa uma correção local no Linkerd rodando `bin/docker-build` e `bin/image-load --k3d` antes de publicar imagens de teste em um registro privado via `DOCKER_REGISTRY`.

## Limites e trade-offs
Esquecer de instalar o `docker buildx` antes de rodar os scripts de build de imagem fará o processo local de empacotamento falhar.

## Como verificar
Conferi as subseções Comprehensive e Publishing images em `BUILD.md` de `linkerd/linkerd2`.

## Conexões
- [[linkerd-control-plane-distributed-tracing-flag]] — Veja também: Habilitação de rastreamento distribuído nos componentes do control plane.
- [[linkerd-third-party-security-audits-and-policy]] — Veja também: Auditorias periódicas de segurança por terceiros e política em SECURITY.md.

## Fontes
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
