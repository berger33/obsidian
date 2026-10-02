---
id: software.testes.tranche15.000943
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/configuration/", "https://nexte.st/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: detectar e interromper testes lentos

## Em uma frase
O limite de lentidão avisa quando um teste excede o período configurado e pode encerrá-lo após um número de períodos.

## Por que importa
Testes lentos degradam o ciclo de feedback antes de falhar, e sem limite um caso travado consome o tempo do pipeline sem produzir diagnóstico.

## Como funciona
Configure um período compatível com o perfil, use `terminate-after` quando a interrupção for desejada e investigue avisos como sinal de regressão de desempenho.

## Exemplo
`slow-timeout = { period = \"60s\", terminate-after = 2 }` avisa após um minuto e encerra o caso após dois períodos.

## Limites e trade-offs
Limites apertados produzem interrupção em máquinas carregadas, e interromper pode deixar recurso parcialmente limpo se o teste não tratar encerramento abrupto.

## Como verificar
Meça a distribuição de duração dos casos, ajuste o período com margem e provoque um caso artificialmente lento para confirmar o aviso e o encerramento.

## Conexões
- [[nextest-retries-and-flaky-result]] — Veja também: nextest: usar retries com política explícita.
- [[nextest-filtersets]] — Veja também: nextest: selecionar testes com filtros.

## Fontes
- [nextest — Configuration](https://nexte.st/docs/configuration/) — perfis, overrides, retries, timeouts e grupos de teste; consultado em 2026-10-02.
- [nextest — Documentation](https://nexte.st/docs/) — visão geral do runner, instalação e operação; consultado em 2026-10-02.
