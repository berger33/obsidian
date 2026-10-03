---
id: software.testes.tranche15.000882
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
fontes: ["https://pestphp.com/docs/cli-api-reference", "https://pestphp.com/docs/continuous-integration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: fazer o job de CI ignorar focos locais marcados only

## Em uma frase
O seletor `->only()` é útil durante desenvolvimento, mas pode deixar a suíte quase toda de fora se uma marca de foco acidental chegar ao branch.

## Por que importa
A opção `--ci` ignora testes focados e executa a suíte inteira, funcionando como defesa no comando de integração em vez de depender da memória de remover cada foco antes do commit.

## Como funciona
Essa guarda não altera a intenção local de filtrar testes em desenvolvimento.

## Exemplo
Use `./vendor/bin/pest --ci` no job que representa a execução completa e mantenha um lint ou revisão que também aponte focos persistidos no código.

## Limites e trade-offs
O parâmetro do CI não substitui cobertura de todos os suites e o comando de validação precisa realmente ser chamado pelo workflow; um job que nunca roda Pest continua sem essa proteção.

## Como verificar
Crie temporariamente um teste `->only()` ao lado de outros casos, execute a forma local e a forma `--ci`, e confirme que a segunda inclui todos os testes.

## Conexões
- [[pest-dataset-bound-depois-de-beforeeach]] — Veja também: Pest 5: criar dataset bound depois do setup de cada teste.
- [[pest-sharding-balanceado-por-tempo]] — Veja também: Pest 5: atualizar tempos para distribuir shards por duração.

## Fontes
- [Pest 5 — CLI API Reference](https://pestphp.com/docs/cli-api-reference) — opções de seleção, execução, paralelismo, shards e reporters; consultado em 2026-10-02.
- [Pest 5 — Continuous Integration](https://pestphp.com/docs/continuous-integration) — execução integral em CI, browser plugin, parallel e artifacts; consultado em 2026-10-02.
