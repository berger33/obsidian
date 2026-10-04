---
id: software.testes.tranche07.000136
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
fontes: ["https://sre.google/sre-book/reliable-product-launches/", "https://grafana.com/docs/k6/latest/using-k6/thresholds/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Comparação de canário com baseline", "Teste: Comparação de canário com baseline"]
lote: software-testes-2000-0001
---

# Comparação de canário com baseline

## Em uma frase
Compare a versão canário e a versão estável por métricas e resultados sob condições suficientemente semelhantes antes de promover a mudança.

## Por que importa
Uma mudança pode degradar uma pequena parcela mesmo quando métricas agregadas parecem normais; comparação controlada ajuda a atribuir diferenças.

## Como funciona
Defina exposição, janela e critérios por segmento antes de iniciar. Acompanhe latência, erros, saturação e indicadores de negócio com a mesma instrumentação; verifique diferença de perfil de usuários, zona, cache e versão de dependências.

## Exemplo
Direcione pequena proporção de sessões de teste para canário e controle para versão estável; compare checkout concluído, erro e p95 na mesma janela e interrompa expansão se guardrail exceder limite.

## Limites e trade-offs
Desbalanceamento e baixa amostragem podem gerar falsas conclusões; mudanças paralelas tornam causalidade incerta. O canário observa tráfego real, mas não substitui conjunto de regressão.

## Como verificar
Valide roteamento, identificação de versão e qualidade do grupo comparador, escolha duração com base em volume e risco e simule falha de guardrail antes da promoção.

## Conexões
- [[testes-canary-validacao-telemetria]] — aprofundamento relacionado.
- [[ci-feedback-testes-regressao]] — aprofundamento relacionado.

## Fontes
- [Google SRE — Reliable Product Launches](https://sre.google/sre-book/reliable-product-launches/) — rollouts graduais, observação de canários e rollback após falha de validação; consultado em 2026-10-01.
- [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — critérios pass/fail associados a métricas e SLOs; consultado em 2026-10-01.
