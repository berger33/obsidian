---
id: software.testes.tranche15.000933
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests-lifecycle", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: respeitar a ordem do ciclo de vida

## Em uma frase
A inicialização e a limpeza acontecem em níveis de assembly, classe e teste, e o nível de teste se repete para cada linha de dados parametrizados.

## Por que importa
Depender de ordem implícita ou limpar recurso no nível errado causa vazamento entre casos e falhas que só aparecem na suíte completa.

## Como funciona
Use os atributos de assembly e classe para recursos compartilhados, os atributos de teste para estado por caso e garanta que limpeza ocorra mesmo em falha.

## Exemplo
A ordem completa do nível de teste cria instância, injeta contexto, roda inicialização, executa, atualiza resultado e só então executa limpeza e descarte.

## Limites e trade-offs
Recursos estáticos de classe exigem cuidado: método de inicialização recebe contexto e falha nele impede os testes da classe de rodar.

## Como verificar
Registre um log de entrada e saída em cada nível, execute dois testes e confirme pelo log a sequência real de chamadas para cada caso.

## Conexões
- [[mstest-dynamicdata-provider]] — Veja também: MSTest: gerar dados com DynamicData.
- [[mstest-testcontext]] — Veja também: MSTest: usar TestContext para informações de execução.

## Fontes
- [MSTest — Test lifecycle](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests-lifecycle) — ordem de inicialização e limpeza em nível de assembly, classe e teste; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
