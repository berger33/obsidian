---
id: software.devops.tranche02.000119
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

# Reuniões quinzenais em dois fusos horários e governança em velero-io/.github

## Em uma frase
As seções `Community` e `Governance` do README informam que a comunidade do Velero realiza reuniões quinzenais (`bi-weekly`) alternando entre fusos horários amigáveis a Pequim (`Beijing-friendly`) e aos EUA/Europa (`US/Europe-friendly`), conta com lista de discussão (`projectvelero` no Google Groups) e mantém seu documento de governança em `velero-io/.github/blob/main/GOVERNANCE.md`.

## Por que importa
A alternância de horários entre Ásia e Américas/Europa facilita a participação direta de equipes distribuídas globalmente que dependem do Velero para proteção de dados em Kubernetes.

## Como funciona
Inscreva-se no calendário LFX do projeto (`zoom-lfx.platform.linuxfoundation.org/meetings/velero`) e consulte `GOVERNANCE.md` para conhecer o processo decisório e os papéis dos mantenedores.

## Exemplo
Uma equipe que desenvolve um plugin de armazenamento acompanha as reuniões quinzenais da comunidade para alinhar compatibilidade com a próxima release.

## Limites e trade-offs
As políticas de governança aplicam-se a toda a organização `velero-io`, incluindo repositórios de plugins mantidos pelo projeto.

## Como verificar
Conferi as seções Community e Governance no README oficial de `vmware-tanzu/velero`.

## Conexões
- [[velero-versioned-docs-and-troubleshooting]] — Veja também: Seletor de versão na documentação e fluxo de troubleshooting do Velero.
- [[velero-cncf-sandbox-and-contributing-workflow]] — Veja também: Status na CNCF, séries LF Projects e guia Start contributing.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
