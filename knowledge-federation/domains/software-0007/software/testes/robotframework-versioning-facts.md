---
id: software.testes.tranche24.001769
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://github.com/robotframework/robotframework", "https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Fatos de versão e estabilidade do projeto

## Em uma frase
O repositório público mostra a escala do projeto: milhares de commits na história, releases como tags (171 tags listadas na página do repositório), múltiplas branches ativas e desenvolvimento contínuo — enquanto o README ancora os requisitos mínimos de Python e as versões de transição.

## Por que importa
Em decisões de adoção, a longevidade mensurável importa: um projeto com mais de dezesseis mil commits, política explícita de suporte a versões antigas e fundação mantenedora apresenta um perfil diferente de uma biblioteca de fim de semana; os fatos de versão sustentam essa avaliação.

## Como funciona
Para estimar risco de adoção, consulte as tags de release e o intervalo entre versões no repositório oficial, verifique no README a política de Python mínimo e registre na decisão o pin de transição aplicável (6.1.1 ou 4.1.3).

## Exemplo
Uma ADR pode dizer: "framework com releases contínuos, suporte documentado até Python 3.6 via pin 6.1.1, mantido por fundação sem fins lucrativos" — tudo checável no README e na página do repositório.

## Limites e trade-offs
Contagens de commits e tags mudam com o tempo; a nota usa os números como ordem de grandeza visível na página oficial, não como métrica estável.

## Como verificar
A escala do projeto (commits, tags, branches) foi lida diretamente da página oficial do repositório no GitHub consultada nesta revisão; a política de versões, do README.

## Conexões
- [[robotframework-contributing]] — Veja também: Contribuir: do CONTRIBUTING.rst aos rótulos de issue.

## Fontes
- [Repositório oficial robotframework/robotframework](https://github.com/robotframework/robotframework) — Repositório oficial no GitHub com código-fonte, histórico de commits, branches, tags e canais do projeto.; consultado em 2026-10-03.
- [Robot Framework README.rst oficial](https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst) — README.rst oficial do Robot Framework com introdução, instalação, exemplo de suíte, CLI robot/rebot, ecossistema, fundação e licenciamento.; consultado em 2026-10-03.
