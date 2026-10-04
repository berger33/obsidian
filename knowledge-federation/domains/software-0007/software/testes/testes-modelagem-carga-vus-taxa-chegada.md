---
id: software.testes.tranche07.000102
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/", "https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Modelagem de carga: VUs e taxa de chegada", "Teste: Modelagem de carga: VUs e taxa de chegada"]
lote: software-testes-2000-0001
---

# Modelagem de carga: VUs e taxa de chegada

## Em uma frase
Selecione um modelo aberto ou fechado de geração de carga de acordo com a pergunta que o teste pretende responder.

## Por que importa
Quando o sistema fica lento, usuários virtuais em um modelo fechado podem iniciar menos iterações; uma taxa de chegada aberta tenta manter o ritmo programado e revela filas e saturação de outro modo.

## Como funciona
Modele VUs para concorrência de usuários e executores de arrival rate para taxa de início de iterações. Dimensione o gerador e a alocação de VUs; monitore iterações descartadas, pois capacidade insuficiente do gerador pode invalidar o perfil pretendido.

## Exemplo
Para estimar experiência de sessões interativas, modele usuários que aguardam respostas entre ações. Para testar uma taxa de entrada fixa de eventos, use chegada controlada e confirme que o gerador consegue sustentar o ritmo.

## Limites e trade-offs
Os modelos não são intercambiáveis: throughput, tempo de espera e concorrência observados mudam. Uma taxa aberta alta pode sobrecarregar o ambiente, e VUs não equivalem automaticamente a pessoas reais.

## Como verificar
Registre o modelo, a configuração de cenários, a taxa realmente iniciada, iterações descartadas, recursos do gerador e métricas do serviço; compare apenas execuções com perfis equivalentes.

## Conexões
- [[performance-testing-modelagem-carga]] — aprofundamento relacionado.
- [[testes-hermeticos-dependencias]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Scenario concepts](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/) — modelos de chegada, VUs, recursos e efeitos na interpretação; consultado em 2026-10-01.
- [Grafana k6 — API load testing](https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/) — objectivos, desenho de carga e famílias de ensaio para APIs; consultado em 2026-10-01.
