---
id: software.testes.tranche13.000653
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://mochajs.org/features/root-hook-plugins/", "https://mochajs.org/features/parallel-mode/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: instalar root hooks por plugin reutilizável

## Em uma frase
Um Root Hook Plugin exporta hooks que o Mocha instala fora de uma suite nomeada.

## Por que importa
O mecanismo evita copiar a mesma inicialização em vários arquivos e oferece uma forma documentada de compartilhar hooks quando a execução paralela cria workers independentes.

## Como funciona
Exporte `mochaHooks` a partir do módulo requerido pelo runner e escolha entre hook por teste ou hook de suite conforme o recurso; não confunda um plugin com fixture global de execução única.

## Exemplo
Um plugin pode remover a variável temporária após cada teste, enquanto um setup global cria uma infraestrutura cara uma vez antes dos workers iniciarem.

## Limites e trade-offs
Estado mutável dentro de um processo worker não vira automaticamente estado compartilhado entre arquivos. Serviços externos ainda precisam de isolamento por teste ou identificador.

## Como verificar
Execute dois arquivos em modo serial e paralelo e confirme qual código de hook roda em cada caso e onde os dados temporários ficam isolados.

## Conexões
- [[mocha-async-completion-contract]] — Veja também: Mocha: escolher uma única forma de concluir teste assíncrono.
- [[mocha-parallel-order-isolation]] — Veja também: Mocha: não depender de ordem global em modo paralelo.

## Fontes
- [Mocha — Root Hook Plugins](https://mochajs.org/features/root-hook-plugins/) — root hook plugins across test files and workers; consultado em 2026-10-02.
- [Mocha — Parallel Mode](https://mochajs.org/features/parallel-mode/) — workers, nondeterministic file order and parallel-mode limitations; consultado em 2026-10-02.
