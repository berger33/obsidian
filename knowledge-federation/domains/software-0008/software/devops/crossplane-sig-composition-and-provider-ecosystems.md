---
id: software.devops.tranche02.000109
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
fontes: ["https://raw.githubusercontent.com/crossplane/crossplane/main/README.md", "https://docs.crossplane.io/latest/get-started/get-started-with-composition"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Frentes técnicas dos 14 SIGs: composição, provedores, Upjet e observabilidade

## Em uma frase
O README oficial lista 14 canais de SIGs que refletem as frentes técnicas ativas da arquitetura do Crossplane: `#sig-cli`, `#sig-composition-environments`, `#sig-composition-functions`, `#sig-deletion-ordering`, `#sig-devex`, `#sig-docs`, `#sig-e2e-testing`, `#sig-observability`, `#sig-observe-only`, `#sig-prod-readiness`, `#sig-provider-families`, `#sig-secret-stores`, `#sig-upjet` e `#sig-v2-migration`.

## Por que importa
Essa relação mostra exatamente os temas operacionais mais importantes ao operar Crossplane em produção: funções de composição, ordenação de deleção de recursos dependentes, recursos observe-only, famílias de provedores, geração de provedores com Upjet e cofres de segredos.

## Como funciona
Consulte as discussões de `#sig-composition-functions`, `#sig-deletion-ordering`, `#sig-observe-only` e `#sig-provider-families` ao projetar composições complexas que encadeiam múltiplos recursos de nuvem.

## Exemplo
Uma equipe que precisa importar recursos existentes sem recriá-los acompanha os padrões discutidos em `#sig-observe-only`, enquanto outra que constrói provedores baseados em Terraform/OpenTofu consulta `#sig-upjet`.

## Limites e trade-offs
Ordenação incorreta na exclusão de recursos compostos (por exemplo, remover uma sub-rede antes do banco de dados que a utiliza) trava a deleção no provedor de nuvem; planeje dependências com cuidado.

## Como verificar
Conferi a lista de 14 SIGs no README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-special-interest-groups-governance]] — Veja também: Papel consultivo dos Special Interest Groups (SIGs) sem autoridade decisória.
- [[crossplane-adopters-and-open-governance]] — Veja também: Registro público de adotantes em ADOPTERS.md e conformidade OpenSSF.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane Documentation — Get Started with Composition](https://docs.crossplane.io/latest/get-started/get-started-with-composition) — Documentação oficial de introdução ao Crossplane, instalação e quickstarts de recursos e composição referenciada no README.; consultado em 2026-10-03.
