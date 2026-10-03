---
id: software.testes.tranche15.000909
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
fontes: ["https://kotest.io/docs/framework/project-config.html", "https://kotest.io/docs/framework/fail-on-empty-test-suite.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: tornar uma suíte vazia uma falha explícita

## Em uma frase
Filtros por spec, teste ou tag podem deixar o plano sem casos executados; o Kotest 6.2 oferece `failOnEmptyTestSuite` para fazer o módulo falhar nessa condição.

## Por que importa
A opção deve ser habilitada em ProjectConfig.

## Como funciona
A definição de módulo vazio depende de nenhum teste ser executado, mesmo que existam testes definidos e os filtros os tenham excluído; assim o CI detecta seletores obsoletos.

## Exemplo
Em `AbstractProjectConfig`, defina `override val failOnEmptyTestSuite = true`; depois execute o módulo com um filtro que não corresponda a nenhum caso e verifique que o build falha.

## Limites e trade-offs
A falha por suíte vazia identifica seleção sem execução, mas não prova que os testes executados cobrem a superfície exigida; preserve também contagem e inventário por job.

## Como verificar
Rode uma seleção válida e outra impossível, confirmando que a segunda falha porque nenhum teste foi executado, inclusive quando os testes continuam definidos no código.

## Conexões
- [[kotest-filter-por-tags-sem-perder-casos]] — Veja também: Kotest 6.2: usar tags como classificação sem transformar filtro em suíte completa.

## Fontes
- [Kotest 6.2 — Project Level Config](https://kotest.io/docs/framework/project-config.html) — configuração de engine no nível do projeto e precedência; consultado em 2026-10-02.
- [Kotest 6.2 — Fail On Empty Test Suite](https://kotest.io/docs/framework/fail-on-empty-test-suite.html) — failOnEmptyTestSuite e falha de módulo quando nenhum teste é executado após filtros; consultado em 2026-10-02.
