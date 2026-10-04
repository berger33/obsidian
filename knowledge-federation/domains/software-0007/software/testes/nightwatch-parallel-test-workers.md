---
id: software.testes.tranche21.001467
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://nightwatchjs.org/guide/reference/settings.html", "https://github.com/nightwatchjs/nightwatch"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: executar suítes em paralelo

## Em uma frase
A chave test_workers aceita verdadeiro ou um objeto com enabled e workers, rodando cada suíte em um processo próprio com número de trabalhadores fixo ou automático.

## Por que importa
Testes de navegador são lentos por natureza; distribuir suítes entre núcleos costuma ser o ganho mais barato disponível antes de reescrever qualquer teste.

## Como funciona
Habilite workers com número ou auto, ajuste parallel_process_delay se os processos competirem por recursos ao subir, e mantenha cada suíte independente.

## Exemplo
A suíte inteira pode rodar em quatro trabalhadores enquanto a máquina de CI oferece quatro núcleos disponíveis.

## Limites e trade-offs
Paralelismo expõe estado compartilhado entre suítes: dados de teste comuns transformam falha isolada em corrida de interferências.

## Como verificar
Rode a suíte com workers ativado e desativado e confirme que o conjunto de resultados é idêntico nos dois modos.

## Conexões
- [[nightwatch-custom-commands-assertions]] — Veja também: Nightwatch: estender com comandos e asserções próprios.
- [[nightwatch-runner-mocha-unit]] — Veja também: Nightwatch: escolher runner e modo de unidade.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — repositório oficial](https://github.com/nightwatchjs/nightwatch) — código-fonte, releases e documentação do projeto; consultado em 2026-10-03.
