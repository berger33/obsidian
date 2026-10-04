---
id: software.devops.tranche03.000243
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
fontes: ["https://raw.githubusercontent.com/falcosecurity/falco/master/README.md", "https://github.com/falcosecurity/falco"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura modular da organização falcosecurity: libs, rules, plugins, falcoctl e charts

## Em uma frase
A seção `The Falco Project` do README explica que, enquanto `falcosecurity/falco` mantém o código-fonte do binário principal, o projeto isola componentes especializados em cinco repositórios core sob a organização `falcosecurity` (governada pelo hub `falcosecurity/evolution`): **falcosecurity/libs** (bibliotecas centrais que constituem a maior parte do código-fonte e fornecem os drivers de kernel), **falcosecurity/rules** (conjunto oficial de regras pré-definidas de detecção), **falcosecurity/plugins** (plugins que estendem o Falco além de syscalls e eventos de contêiner para serviços externos), **falcosecurity/falcoctl** (utilitário CLI para gerenciar e interagir com o Falco) e **falcosecurity/charts** (Helm charts oficiais, com o fonte do chart em `chart/falco`).

## Por que importa
Desacoplar os drivers e bibliotecas de captura (`libs`), as regras de ameaças (`rules`), os plugins de fontes externas (`plugins`), a CLI de gerenciamento (`falcoctl`) e os pacotes Helm (`charts`) permite atualizar regras de detecção ou plugins sem precisar recompilar o motor principal nem os drivers do kernel.

## Como funciona
Utilize `falcosecurity/charts` para implantar o Falco no Kubernetes, `falcoctl` para gerenciar artefatos de regras e plugins e consulte `falcosecurity/rules` ao customizar políticas de detecção.

## Exemplo
Quando uma nova técnica de ataque é catalogada, a equipe atualiza o pacote de regras a partir de `falcosecurity/rules` via `falcoctl` sem precisar reiniciar ou atualizar os drivers de kernel de `falcosecurity/libs`.

## Limites e trade-offs
Ao reportar bugs ou auditar código, identifique se o componente envolvido pertence ao binário (`falco`), às bibliotecas/drivers (`libs`), às regras (`rules`) ou aos charts (`charts`).

## Como verificar
Conferi a seção The Falco Project no README oficial de falcosecurity/falco.

## Conexões
- [[falco-syscall-monitoring-and-kubernetes-metadata-enrichment]] — Veja também: Observação de syscalls no kernel enriquecida com metadados de container runtime e Kubernetes.
- [[falco-plugins-beyond-syscalls-and-falcoctl-management]] — Veja também: Extensão além de syscalls com falcosecurity/plugins e gerenciamento via falcoctl.

## Fontes
- [Falco — GitHub README](https://raw.githubusercontent.com/falcosecurity/falco/master/README.md) — Visão geral do Falco (segurança em tempo de execução no kernel Linux graduada na CNCF, observação de syscalls com metadados de container/Kubernetes, 5 repositórios core, ambiente demo, auditorias em ./audits/ e build CMake com Modern BPF).; consultado em 2026-10-03.
- [Falco — Repositório Oficial no GitHub](https://github.com/falcosecurity/falco) — Repositório oficial do Falco na CNCF com código-fonte C++, chart/falco, docker/docker-compose/ e audits/.; consultado em 2026-10-03.
