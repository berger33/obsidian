---
id: software.testes.tranche16.000961
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

# Artillery: descrever a carga em fases

## Em uma frase
Cada fase informa duração e taxa de chegada de usuários virtuais, e a opção de progressão transforma a taxa inicial em taxa final ao longo do período.

## Por que importa
Modelar aquecimento, rampa e patamar separadamente permite reproduzir o formato de carga desejado em vez de um volume único e irreal.

## Como funciona
Declare as fases em sequência no arquivo, nomeie cada uma e mantenha o patamar com taxa estável pelo tempo necessário à medição.

## Exemplo
Uma configuração típica aquece com taxa baixa, progride até um pico e depois sustenta essa taxa por vários minutos para observar o comportamento estável.

## Limites e trade-offs
A ferramenta cria usuários virtuais segundo a taxa, não um número fixo de requisições por segundo, e o tempo de cada jornada influencia quantos permanecem ativos.

## Como verificar
Compare as fases planejadas com o resumo da execução e verifique se a taxa observada corresponde à declarada em cada período.

## Conexões
- [[artillery-scenario-flow]] — Veja também: Artillery: compor a jornada do usuário virtual.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
