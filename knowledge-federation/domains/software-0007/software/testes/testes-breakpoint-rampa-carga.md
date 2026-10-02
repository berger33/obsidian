---
id: software.testes.tranche07.000108
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
fontes: ["https://grafana.com/docs/k6/latest/testing-guides/test-types/breakpoint-testing/", "https://grafana.com/docs/k6/latest/using-k6/thresholds/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Breakpoint test com rampa progressiva de carga", "Teste: Breakpoint test com rampa progressiva de carga"]
lote: software-testes-2000-0001
---

# Breakpoint test com rampa progressiva de carga

## Em uma frase
Aumente gradualmente a taxa ou concorrência para localizar a faixa em que o sistema deixa de cumprir critérios operacionais.

## Por que importa
A transição entre capacidade aceitável e degradação ajuda a dimensionar margem, limites e alarmes, desde que os resultados sejam reproduzíveis.

## Como funciona
Escolha incrementos e períodos de observação, defina thresholds e monitore dependências e recursos. Pare ao atingir critério de interrupção previamente acordado; depois repita perto da fronteira para verificar se o limite não foi apenas ruído.

## Exemplo
Suba a taxa de chegada em passos de 10% no ambiente de teste, mantendo cada patamar pelo tempo de coleta. Marque a primeira faixa com erro ou latência além do SLO e identifique o gargalo observado.

## Limites e trade-offs
A capacidade não é um número imutável: tamanho de dados, versão, concorrência e dependências alteram o breakpoint. Uma rampa sem tempo de estabilização pode confundir transientes com saturação.

## Como verificar
Registre configuração, patamares, limiar de parada e causa de saturação; repita a etapa decisiva e confronte métricas do sistema com métricas do gerador.

## Conexões
- [[testes-stress-limite-capacidade]] — aprofundamento relacionado.
- [[performance-testing-modelagem-carga]] — aprofundamento relacionado.

## Fontes
- [Grafana k6 — Breakpoint testing](https://grafana.com/docs/k6/latest/testing-guides/test-types/breakpoint-testing/) — rampa progressiva para descobrir limites do sistema; consultado em 2026-10-01.
- [Grafana k6 — Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) — critérios pass/fail associados a métricas e SLOs; consultado em 2026-10-01.
