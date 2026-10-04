---
id: software.testes.tranche15.000937
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
fontes: ["https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: limitar tempo e tratar repetição

## Em uma frase
Atributos de tempo limite e de repetição permitem interromper operação longa e repetir um caso falho antes de considerá-lo reprovado.

## Por que importa
Sem limite, um caso travado consome o tempo do pipeline; sem política, a repetição pode mascarar defeito real e virar rotina invisível.

## Como funciona
Aplique tempo limite compatível com o caso, use repetição apenas onde a flutuação é conhecida e registre a ocorrência para acompanhamento.

## Exemplo
`[Timeout(2000)]` limita a execução a dois segundos, e `[Retry(2)]` repete um caso que falhou antes de reportar o resultado final.

## Limites e trade-offs
Repetição sem investigação transforma falha real em ruído aceito, e limite curto demais gera reprovação por carga da máquina, não por comportamento do produto.

## Como verificar
Meça o tempo típico do caso, ajuste o limite com margem e verifique no relatório quantas tentativas foram necessárias na execução.

## Conexões
- [[mstest-parallelization]] — Veja também: MSTest: configurar paralelização.
- [[mstest-categories-and-filtering]] — Veja também: MSTest: classificar testes para seleção.

## Fontes
- [MSTest — Configure](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure) — runsettings, testconfig.json, paralelização, timeouts e retries; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
