---
id: software.testes.tranche10.000415
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
fontes: ["https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/", "https://grafana.com/docs/k6/latest/using-k6/scenarios/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# k6: manter setup e teardown como lifecycle explícito

## Em uma frase
setup prepara dados antes dos cenários; seus dados JSON são copiados para cada VU e para teardown, não compartilhados como um objeto JavaScript mutável.

## Por que importa
Um teste de carga útil precisa representar o modelo de chegada e transformar métricas em critérios de decisão explícitos. Criar fixture em toda iteração aumenta tráfego e mistura custo de preparação à medição do caminho principal.

## Como funciona
Modele cenários e executors a partir do comportamento esperado, segmente métricas com tags e use thresholds para declarar resultados. Use setup uma vez para preparar o estado do run e retorne apenas dados compatíveis com JSON; cada VU e teardown recebe uma cópia própria do resultado.

## Exemplo
setup obtém o ID de um produto de leitura e o retorna; cada VU cria seu próprio carrinho, sem depender de mutations na memória compartilhada.

## Limites e trade-offs
Resultados dependem do perfil de workload, ambiente, capacidade geradora e métricas escolhidas; exemplos de thresholds não são SLOs universais. A cópia de memória não isola recursos externos: VUs que escrevem na mesma conta ou registro ainda podem disputar locks, quotas ou ordenação e deixar o cenário artificial.

## Como verificar
Confirme a chamada única de setup, inspecione o payload JSON e use recursos externos exclusivos por VU quando houver escrita; não dependa de estado JavaScript compartilhado.

## Conexões
- [[k6-dropped-iterations-capacidade-vus]] — Veja também: k6: interpretar dropped iterations junto à capacidade de VUs.
- [[k6-tags-segmentar-metricas-sem-alta-cardinalidade]] — Veja também: k6: usar tags para segmentar métricas de forma controlada.

## Fontes
- [Grafana k6 — Test lifecycle](https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/) — setup, execução de cenários e teardown; consultado em 2026-10-02.
- [Grafana k6 — Scenarios](https://grafana.com/docs/k6/latest/using-k6/scenarios/) — execução de workloads nomeados com executors e parâmetros; consultado em 2026-10-02.
