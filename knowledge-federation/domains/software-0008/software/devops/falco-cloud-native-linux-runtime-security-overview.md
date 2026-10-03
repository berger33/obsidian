---
id: software.devops.tranche03.000241
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/falcosecurity/falco/master/README.md", "https://falco.org/docs/getting-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Detecção de comportamento anormal em tempo real no kernel Linux graduada na CNCF

## Em uma frase
O README oficial no repositório falcosecurity/falco define o Falco como uma ferramenta cloud-native de segurança em tempo de execução (runtime security) para sistemas operacionais Linux, projetada para detectar e alertar em tempo real sobre comportamentos anormais e potenciais ameaças de segurança: criado originalmente pela Sysdig, o Falco é um **projeto graduado** da Cloud Native Computing Foundation (CNCF) distribuído para arquiteturas `x86_64` e `aarch64` e utilizado em produção por diversas organizações listadas em `ADOPTERS.md`.

## Por que importa
Controles preventivos como escaneamento de imagens no Harbor e políticas de admissão no Kyverno ou Gatekeeper atuam antes de o contêiner rodar, mas não detectam um invasor que explore uma vulnerabilidade zero-day em tempo de execução; o Falco preenche exatamente essa camada de detecção em runtime.

## Como funciona
Implante o Falco nos nós Linux dos seus clusters Kubernetes (x86_64 ou ARM64/aarch64) para monitorar continuamente o comportamento em tempo de execução dos contêineres e dos próprios hosts.

## Exemplo
Enquanto o Kyverno valida se o pod pode ser admitido, o Falco vigia em tempo real se algum processo dentro do pod em execução tenta abrir um shell interativo ou ler arquivos sensíveis inesperados.

## Limites e trade-offs
O Falco é por natureza um sistema de detecção e alerta (IDS/monitoramento de runtime); combine seus alertas com fluxos de resposta a incidentes ou automação de contenção.

## Como verificar
Conferi os badges de topo e a abertura do README oficial de falcosecurity/falco.

## Conexões
- [[falco-syscall-monitoring-and-kubernetes-metadata-enrichment]] — Veja também: Observação de syscalls no kernel enriquecida com metadados de container runtime e Kubernetes.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco Documentation — Getting Started & Setup](https://falco.org/docs/getting-started/) — Documentação oficial do Falco para início rápido, implantação em produção e compilação a partir do código-fonte.; consultado em 2026-10-03.
