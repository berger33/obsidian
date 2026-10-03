---
id: software.devops.tranche02.000118
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

# Seletor de versão na documentação e fluxo de troubleshooting do Velero

## Em uma frase
As seções `Documentation` e `Troubleshooting` do README orientam o usuário a utilizar o seletor de versão no topo do site `velero.io/docs/` para garantir que está lendo a documentação correspondente à sua versão instalada do Velero, além de apontar para o guia de troubleshooting (`velero.io/docs/troubleshooting`), abertura de issues e os canais `#velero-users` e `#velero-dev` no Slack do Kubernetes.

## Por que importa
Flags de CLI, anotações de pods para backup de volumes e parâmetros de plugins mudam ao longo das versões; seguir instruções da branch `main` em um cluster que roda uma versão estável anterior é causa comum de erro operacional.

## Como funciona
Selecione sempre a versão exata do Velero no topo da documentação oficial e consulte o guia de troubleshooting ao diagnosticar backups com status `PartiallyFailed` ou `Failed`.

## Exemplo
Um engenheiro de plantão usa `velero.io/docs/troubleshooting` e os logs do backup para identificar uma permissão IAM ausente no bucket de destino.

## Limites e trade-offs
Ao compartilhar logs no Slack `#velero-users` ou em issues públicas, remova credenciais, URLs internas e nomes confidenciais de segredos.

## Como verificar
Conferi as seções Documentation e Troubleshooting no README oficial de `vmware-tanzu/velero`.

## Conexões
- [[velero-design-proposals-and-implemented-archive]] — Veja também: Processo de propostas de design em design/ e histórico em design/Implemented/.
- [[velero-community-meetings-and-governance]] — Veja também: Reuniões quinzenais em dois fusos horários e governança em velero-io/.github.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
