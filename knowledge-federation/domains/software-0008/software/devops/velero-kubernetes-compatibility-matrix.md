---
id: software.devops.tranche02.000114
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
fontes: ["https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md", "https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Matriz de compatibilidade do Velero 1.14 a 1.18 com versões do Kubernetes

## Em uma frase
A subseção `Velero compatibility matrix` do README apresenta a compatibilidade esperada (`1.18-latest`) e as versões exatas do Kubernetes em que cada série foi testada: Velero `1.18` testado em Kubernetes `1.33.7`, `1.34.1` e `1.35.0`; `1.17` em `1.31.7`, `1.32.3`, `1.33.1` e `1.34.0`; `1.16` em `1.31.4`, `1.32.3` e `1.33.0`; `1.15` em `1.28.8`, `1.29.8`, `1.30.4` e `1.31.1`; e `1.14` em `1.27.9`, `1.28.9` e `1.29.4`.

## Por que importa
Quando um cluster Kubernetes é atualizado para uma nova versão menor (por exemplo `1.34` ou `1.35`), APIs depreciadas ou alteradas podem afetar a serialização e restauração de recursos se o Velero estiver desatualizado.

## Como funciona
Consulte a matriz de compatibilidade antes de atualizar o Kubernetes ou o Velero e execute testes de backup e restore caso utilize uma combinação de versão fora da lista testada pelos mantenedores.

## Exemplo
Ao planejar o upgrade do cluster para Kubernetes `1.34`, a equipe de plataforma atualiza o Velero para `1.17` ou `1.18` conforme a matriz oficial.

## Limites e trade-offs
Como o próprio README ressalta, os mantenedores não conseguem testar todas as combinações possíveis de versões; homologue sempre no seu ambiente antes da produção.

## Como verificar
Conferi a subseção Velero compatibility matrix no README oficial de `vmware-tanzu/velero`.

## Conexões
- [[velero-file-system-backup-and-csi-data-mover]] — Veja também: Movimentação de dados de volumes: file-system backup, data mover CSI e plugins de provedor.
- [[velero-n-minus-2-upgrade-restore-guarantee]] — Veja também: Garantia de restauração de backups entre versões N-2 menores do Velero.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
