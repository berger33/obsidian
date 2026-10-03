---
id: software.devops.tranche02.000107
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
fontes: ["https://raw.githubusercontent.com/crossplane/crossplane/main/README.md", "https://github.com/crossplane/crossplane"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Reuniões comunitárias a cada quatro semanas e canais de colaboração

## Em uma frase
A seção `Get Involved` do README informa que a reunião comunitária do Crossplane ocorre a cada 4 semanas às quintas-feiras às 10:00 Pacific Time (com calendário na plataforma LFX da Linux Foundation, pauta pública e gravações no YouTube), além de listar os canais oficiais no Slack (`slack.crossplane.io`), Bluesky, Twitter/X, LinkedIn e e-mail (`crossplane-info@lists.cncf.io`).

## Por que importa
Quando surgem dúvidas de design, revisões de implementação ou bugs em provedores específicos, saber se a questão deve ser aberta no repositório central do Crossplane ou no repositório do provedor acelera a resposta.

## Como funciona
Abra issues no repositório `crossplane/crossplane` para o núcleo ou no repositório do provedor correspondente e participe das reuniões a cada 4 semanas para discutir revisões de design e direção do projeto.

## Exemplo
Um mantenedor interno de plataforma participa da call comunitária de quinta-feira para alinhar uma proposta de melhoria com os mantenedores upstream.

## Limites e trade-offs
Antes de abrir uma issue de bug em recursos de nuvem, verifique se a falha ocorre no core do Crossplane ou no provider específico instalado no cluster.

## Como verificar
Conferi a seção Get Involved no README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-public-roadmap-and-triage-process]] — Veja também: Roadmap público, triagem comunitária e natureza estimativa dos milestones.
- [[crossplane-special-interest-groups-governance]] — Veja também: Papel consultivo dos Special Interest Groups (SIGs) sem autoridade decisória.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane — Repositório Oficial no GitHub](https://github.com/crossplane/crossplane) — Repositório oficial do Crossplane com código-fonte, ADOPTERS.md, contributing/README.md e notas de release.; consultado em 2026-10-03.
