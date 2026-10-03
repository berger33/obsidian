---
id: software.testes.tranche18.001177
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

# JUnit 5: marcar testes com anotações

## Em uma frase
As anotações identificam métodos e classes de teste, com variantes para desabilitar, exibir nome personalizado e ordenar a execução.

## Por que importa
A marcação explícita desacopla o teste do nome do método e permite recursos que a convenção de nomenclatura não expressa.

## Como funciona
Use anotação de teste nos métodos, nomes de exibição descritivos e desabilitação apenas com justificativa registrada no código.

## Exemplo
Um caso pode exibir nome legível no relatório mantendo um método curto no código.

## Limites e trade-offs
Desabilitar testes sem motivo documentado acumula casos esquecidos, e nomes de exibição duplicados confundem a leitura do relatório.

## Como verificar
Renomeie um método mantendo o nome de exibição e confirme que o relatório continua identificando o caso pelo rótulo legível.

## Conexões
- [[junit5-lifecycle]] — Veja também: JUnit 5: preparar e limpar nos níveis corretos.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
