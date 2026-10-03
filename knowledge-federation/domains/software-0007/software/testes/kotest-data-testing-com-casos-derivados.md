---
id: software.testes.tranche15.000902
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/datatesting/data-driven-testing.html", "https://kotest.io/docs/framework/isolation-mode.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: escolher withXXX de acordo com estilo e tipo de nó

## Em uma frase
Data-driven testing gera casos automaticamente a partir de linhas de entrada, mas as funções disponíveis dependem do estilo de Spec e podem criar containers ou testes folha.

## Por que importa
Na documentação atual, `withData` continua existindo para compatibilidade, enquanto variantes como `withTests`, `withContexts` ou `withScenarios` deixam explícito se a lista descreve casos executáveis ou agrupamentos.

## Como funciona
A escolha afeta hierarquia, nomes e filtros da plataforma de testes.

## Exemplo
Em `FunSpec`, use `withTests` para uma tabela que deve gerar folhas independentes; em estilos com contextos próprios, prefira a variante indicada para esse DSL.

## Limites e trade-offs
Reutilizar uma variante herdada de versão antiga pode gerar uma árvore diferente após upgrade; coleções grandes também exigem nomes de caso estáveis e únicos.

## Como verificar
Liste os testes descobertos no IDE ou runner e confira que cada linha gera o nível correto da árvore e que falhas apontam para a entrada correspondente.

## Conexões
- [[kotest-concorrencia-de-testes-e-estado-mutavel]] — Veja também: Kotest 6.2: habilitar concorrência só depois de definir segurança de estado.
- [[kotest-nomes-estaveis-para-linhas-de-dados]] — Veja também: Kotest 6.2: tornar nomes de casos de dados estáveis e legíveis.

## Fontes
- [Kotest 6.2 — Data Driven Testing](https://kotest.io/docs/framework/datatesting/data-driven-testing.html) — variantes withXXX, hierarquia, nomes e linhas de dados; consultado em 2026-10-02.
- [Kotest 6.2 — Isolation Modes](https://kotest.io/docs/framework/isolation-mode.html) — instâncias de Spec, SingleInstance, InstancePerRoot e modos depreciados; consultado em 2026-10-02.
