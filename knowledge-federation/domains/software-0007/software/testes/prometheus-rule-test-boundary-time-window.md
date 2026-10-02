---
id: software.testes.tranche08.000238
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/", "https://prometheus.io/docs/prometheus/latest/querying/functions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prometheus: cobrir fronteiras de janela em testes de regras

## Em uma frase
Teste instantes imediatamente antes, durante e após a janela que determina a expressão, retenção local ou condição do alerta.

## Por que importa
Erros de unidade, range selector ou alinhamento de evaluation time podem mover disparo e alterar significado temporal.

## Como funciona
Escolha timestamps explícitos, inclua amostras nos limites da janela e registre a cadência de avaliação usada no cenário.

## Exemplo
Uma regra de erro em cinco minutos recebe série no início e no fim da janela; assertion confirma inclusividade e instante esperado.

## Limites e trade-offs
Evaluation interval do teste não reproduz toda irregularidade de scrape e atraso de ingestão da produção.

## Como verificar
Mova uma amostra através do limite e confirme que resultado muda no instante previsto; compare regra com requisito escrito.

## Conexões
- [[prometheus-alert-for-pending-firing]] — Veja também: Prometheus: cobrir estados pending e firing de alertas.
- [[prometheus-rate-counter-reset]] — Veja também: Prometheus: testar rate diante de reset de counter.

## Fontes
- [Prometheus — Unit testing for rules](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/) — promtool, séries de entrada e assertions de PromQL/alertas; consultado em 2026-10-02.
- [Prometheus — Query functions](https://prometheus.io/docs/prometheus/latest/querying/functions/) — semântica de funções e tipos de dados PromQL; consultado em 2026-10-02.
