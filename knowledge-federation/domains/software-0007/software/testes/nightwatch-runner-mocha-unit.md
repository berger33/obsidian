---
id: software.testes.tranche21.001468
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
fontes: ["https://nightwatchjs.org/guide/reference/settings.html", "https://nightwatchjs.org/guide/concepts/test-environments.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: escolher runner e modo de unidade

## Em uma frase
O campo test_runner seleciona o runner interno (default) ou o mocha, com opções aninhadas como ui; unit_tests_mode desliga a criação automática da sessão de navegador.

## Por que importa
Testes de unidade de serviços Node.js não precisam de navegador, e ligar o mocha aproveita sintaxes que o time já conhece em vez de impor a estrutura interna.

## Como funciona
Para unidade, ative unit_tests_mode; para sintaxe tdd do mocha, declare test_runner com type mocha e options; mantenha o default para e2e clássico.

## Exemplo
Um utilitário de formatação de moeda pode ser testado no modo de unidade, sem sessão, enquanto o checkout usa o runner padrão.

## Limites e trade-offs
Modos diferentes coexistindo na mesma configuração exigem ambientes separados; misturar tudo em um arquivo gera sessões órfãs.

## Como verificar
Execute um teste de unidade e confirme que nenhum navegador abre durante a execução.

## Conexões
- [[nightwatch-parallel-test-workers]] — Veja também: Nightwatch: executar suítes em paralelo.
- [[nightwatch-screenshots-failures]] — Veja também: Nightwatch: capturas de tela em falha.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — Ambientes de teste](https://nightwatchjs.org/guide/concepts/test-environments.html) — herança entre ambientes, baseUrl e globals; consultado em 2026-10-03.
