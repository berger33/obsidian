---
id: software.testes.tranche07.000106
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
fontes: ["https://grafana.com/docs/k6/latest/testing-guides/test-types/spike-testing/", "https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Spike test para aumentos abruptos de tráfego", "Teste: Spike test para aumentos abruptos de tráfego"]
lote: software-testes-2000-0001
---

# Spike test para aumentos abruptos de tráfego

## Em uma frase
Simule uma subida rápida de carga para examinar se filas, autoscaling e dependências suportam mudanças abruptas e como o serviço se recupera.

## Por que importa
Um sistema pode suportar carga constante e mesmo assim falhar quando tráfego chega antes de processos de escala ou aquecimento estarem prontos.

## Como funciona
Estabeleça baseline, amplitude, velocidade e duração do pico; registre política de autoscaling, comportamento de fila, latência e erros. A etapa de retorno à carga usual também é importante para observar recuperação e recursos retidos.

## Exemplo
Partindo de 20 requisições por segundo, um teste autorizado sobe rapidamente para uma taxa de pico acordada e depois retorna ao baseline; compare o efeito nos endpoints críticos e a recuperação das filas.

## Limites e trade-offs
Picos arbitrários podem causar interrupção e não representam necessariamente rajadas reais. Autoscaling pode ter atraso e quotas externas podem dominar o resultado.

## Como verificar
Confirme que a curva de carga aplicada corresponde ao plano, estabeleça limites de segurança, verifique alarmes e valide que o serviço converge ao estado estável depois do pico.

## Conexões
- [[testes-carga-media-perfil-trafego]] — aprofundamento relacionado.
- [[testes-load-shedding-limites-sobrecarga]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Spike testing](https://grafana.com/docs/k6/latest/testing-guides/test-types/spike-testing/) — aumentos súbitos de tráfego; consultado em 2026-10-01.
- [Grafana k6 — API load testing](https://grafana.com/docs/k6/latest/testing-guides/api-load-testing/) — objectivos, desenho de carga e famílias de ensaio para APIs; consultado em 2026-10-01.
