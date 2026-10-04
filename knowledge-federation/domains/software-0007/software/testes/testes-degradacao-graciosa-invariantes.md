---
id: software.testes.tranche07.000130
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
fontes: ["https://sre.google/sre-book/addressing-cascading-failures/", "https://sre.google/sre-book/testing-reliability/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de degradação graciosa sob falha", "Teste: Teste de degradação graciosa sob falha"]
lote: software-testes-2000-0001
---

# Teste de degradação graciosa sob falha

## Em uma frase
Introduza indisponibilidade ou lentidão de uma dependência e verifique se o serviço preserva operações essenciais ou comunica uma falha controlada.

## Por que importa
Uma falha parcial pode se propagar quando serviços mantêm trabalho inútil, esperas ilimitadas ou dependências recursivas; degradação explícita limita impacto aos usuários.

## Como funciona
Defina steady state e funções essenciais antes do experimento. Injete uma falha pequena e reversível, observe invariantes, erros e recursos, e confirme que fallback não mascara corrupção nem devolve dados obsoletos sem política.

## Exemplo
Desabilite temporariamente uma recomendação não crítica em staging e confirme que a página principal ainda carrega com aviso claro; o serviço deve manter capacidade e recuperar a função quando a dependência volta.

## Limites e trade-offs
Fallbacks podem ocultar incidentes ou fornecer dados inadequados. Experimentos requerem autorização, blast radius pequeno, monitoramento e plano de interrupção.

## Como verificar
Verifique estado antes/durante/depois, métricas de dependências e experiência do fluxo crítico; prove restauração da configuração original e repita apenas após analisar efeitos.

## Conexões
- [[chaos-experiments-steady-state-blast-radius]] — aprofundamento relacionado.
- [[testes-falha-dependencia-timeout-circuit-breaker]] — aprofundamento relacionado.

## Fontes
- [Google SRE — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga e falhas de dependência podem amplificar-se em cascata; consultado em 2026-10-01.
- [Google SRE — Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — testes reduzem incerteza sobre confiabilidade após mudanças; consultado em 2026-10-01.
