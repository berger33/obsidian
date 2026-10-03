---
id: software.testes.tranche16.000969
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
fontes: ["https://www.artillery.io/docs/get-started/first-test", "https://github.com/artilleryio/artillery"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: distribuir carga entre cenários

## Em uma frase
Cenários podem receber pesos relativos, fazendo com que a carga gerada combine jornadas distintas na proporção declarada.

## Por que importa
Sistemas reais recebem mistura de comportamentos, e testar apenas um fluxo superestima a capacidade para o perfil dominante.

## Como funciona
Atribua pesos conforme a proporção observada no uso, mantenha os cenários independentes e registre a origem dos percentuais.

## Exemplo
Uma proporção de leitura alta e escrita baixa pode ser representada por pesos distintos, refletindo melhor o impacto de cada operação no banco.

## Limites e trade-offs
Pesos sem justificativa viram números arbitrários, e cenários dependentes entre si quebram quando a ordem de execução muda.

## Como verificar
Compare a proporção de cenários executados no relatório com os pesos declarados e ajuste se a distribuição observada divergir.

## Conexões
- [[artillery-quick-and-run]] — Veja também: Artillery: escolher entre execução rápida e arquivo.
- [[artillery-rate-vs-concurrency]] — Veja também: Artillery: compreender o modelo de geração de carga.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
