---
id: software.testes.tranche12.000572
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
fontes: ["https://testng.org/dependencies.html", "https://testng.org/annotations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: dependências hard e soft entre testes

## Em uma frase
`dependsOnMethods` ou `dependsOnGroups` expressam pré-requisitos de execução e podem fazer o framework pular um consumidor quando uma dependência falha.

## Por que importa
Declarar relação causal ajuda a explicar quais verificações dependem de uma etapa, mas uma dependência rígida pode esconder testes úteis quando o primeiro método falha.

## Como funciona
Use dependências hard para um resultado realmente necessário; configure `alwaysRun=true` somente quando a execução posterior ainda fizer sentido após falha ou skip do método precedente.

## Exemplo
Um teste de leitura pode depender da criação de um registro; uma verificação de limpeza pode ser configurada para rodar mesmo após falha, se ela for segura sem aquele registro.

## Limites e trade-offs
Não use dependência para forçar uma ordem artificial de testes do mesmo grupo, pois a ordem de métodos de grupo não é uma garantia de fluxo de negócio.

## Como verificar
Faça a etapa antecedente falhar propositalmente e confira se o consumidor fica marcado como skipped ou se `alwaysRun` permite a execução conforme o contrato declarado.

## Conexões
- [[testng-parameters-escopo-xml]] — Veja também: TestNG: organizar parâmetros XML por escopo.
- [[testng-groups-selecao]] — Veja também: TestNG: usar groups para selecionar conjuntos de testes.

## Fontes
- [TestNG — Dependencies](https://testng.org/dependencies.html) — dependências entre métodos e grupos e comportamento de alwaysRun; consultado em 2026-10-02.
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
