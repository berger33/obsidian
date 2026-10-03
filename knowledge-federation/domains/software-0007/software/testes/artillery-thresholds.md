---
id: software.testes.tranche16.000964
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
fontes: ["https://www.artillery.io/docs/get-started/first-test", "https://www.artillery.io/docs/reference/extensions/ensure"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: impor limites de desempenho

## Em uma frase
A extensão de verificação compara métricas da execução com limites declarados e encerra com código de erro quando algum deles é ultrapassado.

## Por que importa
Sem uma regra objetiva, o resultado do teste depende de interpretação e a regressão de latência passa despercebida até chegar ao ambiente de produção.

## Como funciona
Declare limites por métrica de resposta e código de erro, escolha percentuais coerentes com a experiência esperada e mantenha os valores versionados.

## Exemplo
Um limite pode exigir que o percentil 95 fique abaixo de um valor em milissegundos e que a taxa de erros permaneça em patamar mínimo durante a fase de pico.

## Limites e trade-offs
Limites apertados demais produzem falhas em máquinas carregadas, e limites frouxos transformam a verificação em formalidade; a calibração precisa vir de medições repetidas.

## Como verificar
Aprove deliberadamente um limite próximo do observado e confirme o código de saída e a mensagem que identifica a métrica violada.

## Conexões
- [[artillery-capture-and-reuse]] — Veja também: Artillery: encadear requisições com capturas.
- [[artillery-metrics-interpretation]] — Veja também: Artillery: interpretar o resumo de métricas.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — ensure](https://www.artillery.io/docs/reference/extensions/ensure) — limites e condições sobre métricas com código de saída não nulo; consultado em 2026-10-03.
