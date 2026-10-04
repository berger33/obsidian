---
id: software.devops.tranche02.000120
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

# Status na CNCF, séries LF Projects e guia Start contributing

## Em uma frase
As seções `Contributing` e `Cloud Native Computing Foundation` do README registram que o Velero é um projeto da Cloud Native Computing Foundation (CNCF, listado no README como sandbox project e estabelecido como Velero a Series of LF Projects, LLC), oferecendo o guia `Start contributing` (`velero.io/docs/start-contributing`) para configurar o ambiente de desenvolvimento e testes.

## Por que importa
Conhecer o enquadramento institucional na CNCF/Linux Foundation e o guia oficial de contribuição ajuda empresas usuárias a auditar conformidade legal e contribuir com correções para o projeto.

## Como funciona
Siga as instruções em `velero.io/docs/start-contributing` ao montar um ambiente local para testar correções de código ou melhorias de documentação no Velero.

## Exemplo
Um engenheiro de plataforma configura o ambiente de desenvolvimento seguindo `Start contributing` para reproduzir e corrigir um bug em restauração de recursos filtrados.

## Limites e trade-offs
Verifique sempre as políticas em `lfprojects.org/policies/` e os requisitos de assinatura/contribuição do repositório antes de submeter pull requests.

## Como verificar
Conferi as seções Contributing e Cloud Native Computing Foundation no README oficial de `vmware-tanzu/velero`.

## Conexões
- [[velero-community-meetings-and-governance]] — Veja também: Reuniões quinzenais em dois fusos horários e governança em velero-io/.github.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
