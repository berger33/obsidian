---
id: software.devops.tranche02.000117
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
fontes: ["https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md", "https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Processo de propostas de design em design/ e histórico em design/Implemented/

## Em uma frase
A seção `Design proposals` de `ARCHITECTURE.md` explica que propostas de design aceitas e em discussão vivem no diretório `design/`, seguem o modelo `design/_template.md`, são revisadas por meio de pull requests e nas reuniões comunitárias, e, uma vez implementadas, são arquivadas em `design/Implemented/`.

## Por que importa
Consultar os documentos em `design/` e `design/Implemented/` permite entender as decisões arquiteturais e os limites técnicos de recursos complexos como o CSI data mover e o backup de sistema de arquivos.

## Como funciona
Antes de propor uma mudança arquitetural ou investigar o comportamento interno de um controlador do Velero, revise os documentos em `design/Implemented/` e utilize `design/_template.md` para novas propostas.

## Exemplo
Um arquiteto lê as propostas implementadas em `design/Implemented/` para compreender como o Velero coordena snapshots CSI e upload assíncrono.

## Limites e trade-offs
Propostas ainda abertas em `design/` (fora de `Implemented/`) podem sofrer alterações antes do lançamento; baseie automações de produção na documentação da versão instalada.

## Como verificar
Conferi a seção Design proposals em `ARCHITECTURE.md` no repositório `vmware-tanzu/velero`.

## Conexões
- [[velero-ipv4-ipv6-and-dual-stack-support]] — Veja também: Suporte a ambientes IPv4, IPv6 e dual-stack no Velero.
- [[velero-versioned-docs-and-troubleshooting]] — Veja também: Seletor de versão na documentação e fluxo de troubleshooting do Velero.

## Fontes
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
