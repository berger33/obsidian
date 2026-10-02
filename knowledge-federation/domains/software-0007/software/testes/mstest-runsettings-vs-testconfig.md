---
id: software.testes.tranche15.000939
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

# MSTest: escolher o arquivo de configuração

## Em uma frase
Executores baseados na plataforma de testes leem `testconfig.json`, enquanto o caminho clássico usa `.runsettings` para paralelização, timeouts e demais ajustes.

## Por que importa
Misturar os dois formatos sem saber qual está ativo faz uma configuração parecer aplicada quando o executor lê outro arquivo.

## Como funciona
Identifique o executor em uso, mantenha um único arquivo ativo e versione a configuração junto do projeto para que o comportamento seja reproduzível.

## Exemplo
Um projeto com plataforma moderna pode habilitar paralelização em `testconfig.json` com escopo e trabalhadores, enquanto o formato clássico expressa a mesma intenção no runsettings.

## Limites e trade-offs
As opções têm nomes e precedências distintas entre os formatos, e configuração duplicada nos dois cria divergência silenciosa quando alguém altera apenas um deles.

## Como verificar
Execute a suíte com a configuração ativa e confirme pelo relatório o efeito esperado, como número de trabalhadores ou tempo limite aplicado.

## Conexões
- [[mstest-categories-and-filtering]] — Veja também: MSTest: classificar testes para seleção.

## Fontes
- [MSTest — Configure](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure) — runsettings, testconfig.json, paralelização, timeouts e retries; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
