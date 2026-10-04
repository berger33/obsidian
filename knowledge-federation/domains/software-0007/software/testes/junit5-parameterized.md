---
id: software.testes.tranche18.001180
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://junit.org/junit5/docs/current/user-guide/", "https://github.com/junit-team/junit5"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit 5: variar entradas com testes parametrizados

## Em uma frase
Os testes parametrizados recebem argumentos de fontes declaradas, com formatos de exibição que identificam cada invocação no relatório.

## Por que importa
Entradas variadas verificadas pela mesma lógica ficam concisas e cada conjunto aparece como invocação separada no relatório.

## Como funciona
Declare a fonte de dados, dê nome aos conjuntos e escolha o formato de exibição que melhor descreva cada caso.

## Exemplo
Uma regra de desconto pode ser verificada com conjuntos nomeados que descrevem o cenário aplicado em cada linha.

## Limites e trade-offs
Fontes com dados compartilhados entre casos criam acoplamento, e a falha em uma invocação pode interromper a interpretação das seguintes.

## Como verificar
Acrescente um conjunto com valor-limite e confirme que ele aparece como invocação própria, com o nome do caso no relatório.

## Conexões
- [[junit5-assertions]] — Veja também: JUnit 5: escrever asserções com mensagens úteis.
- [[junit5-dynamic-tests]] — Veja também: JUnit 5: gerar testes em tempo de execução.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
