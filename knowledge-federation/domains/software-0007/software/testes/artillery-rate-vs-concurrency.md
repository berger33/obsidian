---
id: software.testes.tranche16.000970
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

# Artillery: compreender o modelo de geração de carga

## Em uma frase
A ferramenta modela taxa de chegada de usuários virtuais ao longo do tempo, e não uma quantidade fixa de requisições por segundo.

## Por que importa
Interpretar a configuração como requisições por segundo leva a expectativas erradas quando a jornada dura mais do que o período da fase.

## Como funciona
Estime quantos usuários ficam ativos a partir da duração média do cenário e acompanhe a métrica de sessões não iniciadas.

## Exemplo
Uma fase curta com jornada longa pode atingir o teto de usuários ativos; nesse caso novas chegadas são contabilizadas como puladas e a taxa real fica abaixo do planejado.

## Limites e trade-offs
Saturar o gerador de carga produz números que descrevem o próprio executor, e não o sistema avaliado, o que exige monitorar recursos da máquina de teste.

## Como verificar
Compare a taxa planejada com a observada em execuções de durações diferentes para identificar em que ponto o gerador deixa de acompanhar.

## Conexões
- [[artillery-scenario-weights]] — Veja também: Artillery: distribuir carga entre cenários.
- [[artillery-ci-integration]] — Veja também: Artillery: integrar a carga ao pipeline.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
