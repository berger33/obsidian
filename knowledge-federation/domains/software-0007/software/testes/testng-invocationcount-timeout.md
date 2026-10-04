---
id: software.testes.tranche12.000579
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://testng.org/annotations.html", "https://testng.org/documentation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: interpretar `invocationCount` e seu timeout

## Em uma frase
`invocationCount` repete um método de teste e `invocationTimeOut` limita o tempo acumulado dessas invocações quando a contagem está definida.

## Por que importa
Repetição mede comportamento ao longo de várias chamadas, mas não demonstra independência se cada invocação reutiliza estado ou depende de uma anterior.

## Como funciona
Defina a contagem somente para um objetivo explícito, prepare cada chamada de forma controlada e lembre que o timeout de invocação é ignorado se `invocationCount` não estiver configurado.

## Exemplo
Um teste de conversão pode invocar o mesmo caso várias vezes para observar uma propriedade determinística; uma verificação de concorrência precisa declarar também as condições de threads.

## Limites e trade-offs
Repetir uma assertion idêntica não aumenta a variedade de entradas e pode elevar tempo sem melhorar evidência sobre o contrato.

## Como verificar
Confira no relatório a quantidade real de execuções, observe duração acumulada e prove que cada chamada não herda dados residuais da anterior.

## Conexões
- [[testng-listener-eventos-relatorio]] — Veja também: TestNG: usar listeners para observar execução.

## Fontes
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
- [TestNG — Documentation](https://testng.org/documentation.html) — grupos, XML, execução paralela, listeners e relatórios; consultado em 2026-10-02.
