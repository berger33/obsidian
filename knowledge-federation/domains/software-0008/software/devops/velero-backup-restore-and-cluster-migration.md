---
id: software.devops.tranche02.000111
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

# Visão geral do Velero: backup, restauração, migração e replicação de clusters

## Em uma frase
O README oficial e o documento `ARCHITECTURE.md` no repositório `vmware-tanzu/velero` apresentam o Velero (anteriormente conhecido como Heptio Ark) como um conjunto de ferramentas para fazer backup e restaurar recursos de clusters Kubernetes e volumes persistentes na nuvem pública ou on-premises, destacando três casos de uso principais: fazer backup do cluster e restaurar em caso de perda, migrar recursos para outros clusters e replicar o cluster de produção em clusters de desenvolvimento e teste.

## Por que importa
Mesmo quando toda a configuração declarativa está em GitOps (Argo CD ou Flux), o estado dinâmico do cluster, segredos gerados em runtime e dados de PersistentVolumes exigem uma ferramenta dedicada de backup e recuperação de desastres.

## Como funciona
Implante o Velero em seus clusters Kubernetes tanto para proteção contra perda acidental ou corrupção quanto para clonar ambientes produtivos em clusters de homologação e migrar cargas entre versões ou provedores.

## Exemplo
Antes de uma manutenção de risco no plano de controle, a equipe dispara um backup do Velero para garantir restauração rápida dos recursos e volumes.

## Limites e trade-offs
Possuir rotinas agendadas de backup sem exercitar regularmente o fluxo de `restore` em um cluster limpo cria falsa sensação de segurança.

## Como verificar
Conferi a seção Overview do README e a seção Goals de `ARCHITECTURE.md` em `vmware-tanzu/velero`.

## Conexões
- [[velero-server-controllers-and-local-cli]] — Veja também: Arquitetura cliente-servidor: controladores em réplica única no cluster e CLI local.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
