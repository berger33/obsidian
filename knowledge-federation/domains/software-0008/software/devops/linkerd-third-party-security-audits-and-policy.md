---
id: software.devops.tranche02.000139
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
fontes: ["https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md", "https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Auditorias periódicas de segurança por terceiros e política em SECURITY.md

## Em uma frase
A seção `Security` do README oficial aponta para `SECURITY.md` quanto à política de segurança e relato de vulnerabilidades e destaca que o Linkerd passa por auditorias periódicas de segurança realizadas por terceiros independentes, cujos relatórios completos são publicados diretamente no diretório `audits/` do repositório (`github.com/linkerd/linkerd2/tree/main/audits`).

## Por que importa
Como o service mesh intercepta todo o tráfego de rede das aplicações e gerencia chaves criptográficas de mTLS, a transparência de auditorias independentes publicadas no próprio repositório é um insumo importante para revisões de segurança e conformidade.

## Como funciona
Consulte os relatórios em `audits/` durante processos de homologação de segurança da malha e utilize o fluxo definido em `SECURITY.md` para reportar vulnerabilidades de forma responsável.

## Exemplo
O time de segurança corporativa revisa os relatórios de auditoria de terceiros no diretório `audits/` do repositório `linkerd/linkerd2` antes de aprovar o mesh para cargas financeiras.

## Limites e trade-offs
Auditorias do software upstream não substituem a configuração correta de NetworkPolicies, RBAC e rotação de certificados de confiança no cluster onde o Linkerd é instalado.

## Como verificar
Conferi a seção Security no README oficial de `linkerd/linkerd2`.

## Conexões
- [[linkerd-container-registry-and-k3d-dev-workflow]] — Veja também: Registro oficial cr.l5d.io/linkerd e fluxo de build local com k3d e buildx.
- [[linkerd-steering-committee-and-community-channels]] — Veja também: Reuniões do Steering Committee, listas da CNCF e canais comunitários.

## Fontes
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
