---
id: software.testes.tranche11.000536
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
fontes: ["https://docs.gatling.io/concepts/scenario/", "https://docs.gatling.io/concepts/assertions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: nomear groups para separar estatísticas de jornada

## Em uma frase
Groups agrupam ações do usuário e permitem observar estatísticas relativas a uma parte nomeada do scenario.

## Por que importa
Métrica global pode esconder uma chamada lenta de autenticação dentro de várias requests rápidas.

## Como funciona
Agrupe fronteiras relevantes, use nomes estáveis e evite criar grupos por id dinâmico de usuário.

## Exemplo
Grupo checkout contém validação de carrinho e confirmação de pagamento e tem assertions próprias de erro/tempo.

## Limites e trade-offs
Group statistic não altera workload nem substitui métricas de sistema ou análise de dependência.

## Como verificar
Compare métricas de grupo com global e confirme cardinalidade limitada aos nomes de jornada.

## Conexões
- [[gatling-open-closed-injection-model]] — Veja também: Gatling: escolher open ou closed conforme hipótese de carga.
- [[gatling-pauses-e-pacing]] — Veja também: Gatling: distinguir pausa do usuário de arrival-rate injection.

## Fontes
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — sequência de ações, exec, controles de fluxo e pausas; consultado em 2026-10-02.
- [Gatling — Assertions](https://docs.gatling.io/concepts/assertions/) — critérios sobre estatísticas da simulação e escopos; consultado em 2026-10-02.
