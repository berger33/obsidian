---
id: software.testes.tranche13.000654
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
fontes: ["https://mochajs.org/features/parallel-mode/", "https://mochajs.org/running/cli/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: não depender de ordem global em modo paralelo

## Em uma frase
Com `--parallel`, Mocha distribui arquivos por workers e não garante a ordem em que eles serão executados.

## Por que importa
O modo pode reduzir duração da suíte, mas revela dependências entre arquivos e limitações de recursos que ficam escondidas em uma execução serial.

## Como funciona
Ative o modo apenas depois de remover estado compartilhado implícito, escolha um número de jobs compatível com banco e portas disponíveis e use filtros CLI em vez de `only` para depurar.

## Exemplo
Uma pipeline pode executar `mocha --parallel --jobs 4` se cada arquivo prepara seu próprio tenant e o serviço de teste suporta as quatro sessões concorrentes.

## Limites e trade-offs
Alguns reporters e opções que dependem da lista completa de testes não funcionam nesse modo; a saída pode ser agrupada por arquivo e bail é best effort.

## Como verificar
Repita a execução com ordem e worker diferentes, verifique os artefatos de reporter e procure colisões de dados antes de adotá-la na CI.

## Conexões
- [[mocha-root-hooks-plugin]] — Veja também: Mocha: instalar root hooks por plugin reutilizável.
- [[mocha-retry-diagnostic]] — Veja também: Mocha: usar retries como evidência de instabilidade.

## Fontes
- [Mocha — Parallel Mode](https://mochajs.org/features/parallel-mode/) — workers, nondeterministic file order and parallel-mode limitations; consultado em 2026-10-02.
- [Mocha — Command-Line Usage](https://mochajs.org/running/cli/) — grep, retries, timeouts, parallel flags and reporter options; consultado em 2026-10-02.
