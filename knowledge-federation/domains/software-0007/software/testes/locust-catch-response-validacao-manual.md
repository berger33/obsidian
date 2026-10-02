---
id: software.testes.tranche11.000515
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html#http-client", "https://docs.locust.io/en/stable/writing-a-locustfile.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: marcar resposta manualmente com catch_response

## Em uma frase
Cliente HTTP de Locust permite inspecionar resposta no bloco catch_response e decidir manualmente se a chamada conta como sucesso ou falha.

## Por que importa
Locust descreve usuários simulados com tarefas Python e controla concorrência, waits e geração distribuída; a taxa observada depende do tempo das tarefas e da capacidade do gerador. HTTP 200 com corpo de erro de negócio pode aparecer como request bem-sucedida se o workload só mede status transport-level.

## Como funciona
Modele jornadas com tarefas observáveis, escolha pacing e pesos a partir do workload esperado, normalize nomes de requests e valide que o gerador suporta o volume planejado. Valide conteúdo relevante dentro do bloco, marque failure com motivo conciso quando contrato falhar e deixe success somente quando a semântica estiver satisfeita.

## Exemplo
Um endpoint retorna 200 com campo state=error; o teste marca request como falha e inclui endpoint sem segredo no motivo.

## Limites e trade-offs
HttpUser não é navegador real; resultado do teste combina comportamento da aplicação, cliente e gerador. Wait time não cria usuários para atingir throughput e tarefas podem conter várias requests. Matcher detalhado em todo response pode custar CPU e desviar workload; valide somente condições necessárias à métrica.

## Como verificar
Inclua resposta 200 válida, status 500 e corpo incoerente e compare contadores de sucesso/falha.

## Conexões
- [[locust-request-name-cardinalidade]] — Veja também: Locust: agrupar URLs variáveis com name estável nas estatísticas.
- [[locust-taskset-sequencia-de-tarefas]] — Veja também: Locust: escolher TaskSet para comportamento hierárquico ou sequência.

## Fontes
- [Locust — Using the HTTP client](https://docs.locust.io/en/stable/writing-a-locustfile.html#http-client) — response context, validação manual e cliente HTTP sem browser; consultado em 2026-10-02.
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
