---
id: software.testes.tranche15.000903
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/datatesting/data-driven-testing.html", "https://kotest.io/docs/framework/datatesting/custom-test-names.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: tornar nomes de casos de dados estáveis e legíveis

## Em uma frase
O nome de um teste gerado a partir dos dados depende normalmente de `toString()` da entrada; isso só é confiável quando a representação é estável e informativa para aquele alvo.

## Por que importa
Nomes instáveis dificultam seleção de teste, comparação de relatórios e investigação de falhas.

## Como funciona
A página de data testing permite passar um map de nomes ou implementar `WithDataTestName` para controlar a descrição.

## Exemplo
Dê a cada registro um identificador como `valid-email` ou implemente `dataTestName()` que inclui os campos relevantes, sem serializar dados sensíveis no output de CI.

## Limites e trade-offs
Nomes com dados pessoais ou conteúdo volumoso podem vazar informação e poluir relatórios; evite usar o payload completo como identificador de teste.

## Como verificar
Execute o conjunto em duas plataformas ou versões e confirme que o runner produz nomes iguais para a mesma linha e que uma falha identifica seu caso sem expor segredo.

## Conexões
- [[kotest-data-testing-com-casos-derivados]] — Veja também: Kotest 6.2: escolher withXXX de acordo com estilo e tipo de nó.
- [[kotest-retries-com-delay-na-configuracao-compartilhada]] — Veja também: Kotest 6.2: configurar retries sem apagar o sinal de falha intermitente.

## Fontes
- [Kotest 6.2 — Data Driven Testing](https://kotest.io/docs/framework/datatesting/data-driven-testing.html) — variantes withXXX, hierarquia, nomes e linhas de dados; consultado em 2026-10-02.
- [Kotest 6.2 — Data Test Names](https://kotest.io/docs/framework/datatesting/custom-test-names.html) — estabilidade de nomes, map, nameFn e WithDataTestName; consultado em 2026-10-02.
