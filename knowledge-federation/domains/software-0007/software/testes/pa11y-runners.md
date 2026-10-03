---
id: software.testes.tranche16.001025
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/pa11y/pa11y", "https://github.com/pa11y/pa11y-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pa11y: combinar motores de verificação

## Em uma frase
A ferramenta aceita dois motores distintos de análise, e cada um mantém conjunto próprio de regras e forma de reportar resultados.

## Por que importa
Os motores não são idênticos, e usar apenas um deles deixa lacunas que o outro detecta.

## Como funciona
Configure os dois motores na mesma execução, compare as listas produzidas e trate a duplicidade na consolidação.

## Exemplo
Uma página pode apresentar problemas de contraste detectados por um motor e falhas de estrutura detectadas apenas pelo outro.

## Limites e trade-offs
Executar tudo em dobro aumenta o tempo e multiplica avisos repetidos, o que exige deduplicação antes de virar critério bloqueante.

## Como verificar
Rode com um motor de cada vez e depois com os dois, verificando que a união dos resultados corresponde à execução combinada.

## Conexões
- [[pa11y-standards-and-levels]] — Veja também: Pa11y: escolher o padrão de conformidade.
- [[pa11y-actions]] — Veja também: Pa11y: preparar a página com ações.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
