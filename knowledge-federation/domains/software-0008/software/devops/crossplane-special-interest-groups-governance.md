---
id: software.devops.tranche02.000108
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

# Papel consultivo dos Special Interest Groups (SIGs) sem autoridade decisória

## Em uma frase
A subseção `Special Interest Groups (SIG)` esclarece que o projeto Crossplane apoia SIGs como grupos de discussão que reúnem membros com interesses compartilhados, mas enfatiza que os SIGs **não** têm autoridade de tomada de decisão nem responsabilidades de propriedade (ownership), servindo puramente como fóruns colaborativos no Slack e em reuniões regulares.

## Por que importa
Deixar explícito que SIGs são fóruns colaborativos sem poder de veto ou propriedade exclusiva mantém a governança técnica centralizada e acessível a novos contribuidores.

## Como funciona
Participe dos canais `#sig-*` no Slack do Crossplane para trocar experiências práticas ou proponha um novo SIG pelos canais de contato caso identifique uma área ainda não representada.

## Exemplo
Engenheiros interessados em prontidão de produção e testes ponta a ponta colaboram nos canais `#sig-prod-readiness` e `#sig-e2e-testing`.

## Limites e trade-offs
Decisões formais de arquitetura e aprovação de código continuam seguindo o guia de contribuição (`contributing/README.md`) e os mantenedores do projeto, e não votações isoladas dentro de um SIG.

## Como verificar
Conferi a subseção Special Interest Groups (SIG) no README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-community-meetings-and-channels]] — Veja também: Reuniões comunitárias a cada quatro semanas e canais de colaboração.
- [[crossplane-sig-composition-and-provider-ecosystems]] — Veja também: Frentes técnicas dos 14 SIGs: composição, provedores, Upjet e observabilidade.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane — Repositório Oficial no GitHub](https://github.com/crossplane/crossplane) — Repositório oficial do Crossplane com código-fonte, ADOPTERS.md, contributing/README.md e notas de release.; consultado em 2026-10-03.
