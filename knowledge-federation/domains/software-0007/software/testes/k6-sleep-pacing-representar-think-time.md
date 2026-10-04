---
id: software.testes.tranche10.000418
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://grafana.com/docs/k6/latest/javascript-api/k6/sleep/", "https://grafana.com/docs/k6/latest/using-k6/scenarios/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: modelar think time em vez de adicionar pausas arbitrárias

## Em uma frase
sleep(t) suspende o VU pelo número de segundos informado e pode representar think time quando a pausa fizer parte do workload.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Pausas fixas adicionadas sem base no uso esperado alteram taxa de requisições e carga oferecida ao sistema.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Importe sleep da API k6 e escolha a duração segundo o modelo de sessão; mantenha-o fora de esperas por readiness e não o combine com código assíncrono.

## Exemplo
Uma jornada síncrona pausa por um segundo entre ler o catálogo e enviar o carrinho para representar think time; um cenário de throughput pode omitir a pausa por objetivo explícito.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. sleep bloqueia a execução do VU; a documentação desaconselha seu uso com código async, e uma pausa fixa não substitui uma condição observável de readiness.

## Como verificar
Compare taxa de chegada e duração da iteração com e sem sleep e confirme que a pausa representa a hipótese do cenário, sem mascarar operação assíncrona.

## Conexões
- [[k6-threshold-por-tag-e-escopo-de-metrica]] — Veja também: k6: limitar threshold a segmentos etiquetados.
- [[k6-browser-protocolo-e-experiencia-complementares]] — Veja também: k6: complementar teste de protocolo com teste de browser.

## Fontes
- [Grafana k6 — sleep API](https://grafana.com/docs/k6/latest/javascript-api/k6/sleep/) — suspensão bloqueante de um VU em segundos e restrições ao uso com código assíncrono; consultado em 2026-10-02.
- [Grafana k6 — Scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/) — execução de workloads nomeados com executors e parâmetros; consultado em 2026-10-02.
