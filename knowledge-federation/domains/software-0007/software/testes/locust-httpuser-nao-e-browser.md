---
id: software.testes.tranche11.000510
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
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://docs.locust.io/en/stable/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: não confundir HttpUser com navegador real

## Em uma frase
HttpUser oferece client HTTP e mantém cookies, mas não renderiza HTML nem carrega automaticamente recursos da página como browser.

## Por que importa
Um teste HTTP de protocolo pode passar enquanto scripts, layout ou experiência do navegador estão quebrados.

## Como funciona
Use HttpUser para jornada de API/protocolo e complemente com automação browser quando a hipótese depende de frontend.

## Exemplo
Carga HTTP consulta endpoints de catálogo; um smoke browser separado valida login e recurso crítico carregado na tela.

## Limites e trade-offs
HttpUser não mede renderização, execução JavaScript nem download de subresources.

## Como verificar
Compare endpoints e métricas da carga com um caso browser representativo e registre qual fronteira cada teste cobre.

## Conexões
- [[locust-task-weights-probabilidade]] — Veja também: Locust: interpretar peso de @task como probabilidade relativa.

## Fontes
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
- [Locust — API Reference](https://docs.locust.io/en/stable/api.html) — classes User, HttpUser, TaskSet e helpers de pacing; consultado em 2026-10-02.
