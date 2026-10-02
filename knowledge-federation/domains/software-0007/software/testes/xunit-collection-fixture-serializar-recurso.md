---
id: software.testes.tranche11.000505
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://xunit.net/docs/shared-context", "https://xunit.net/docs/running-tests-in-parallel"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# xUnit: agrupar classes por collection quando compartilham recurso

## Em uma frase
Collection fixtures compartilham fixture entre classes associadas à mesma collection; classes na collection deixam de executar paralelamente entre si.

## Por que importa
xUnit.net cria casos a partir de Facts/Theories e gerencia instâncias e fixtures com regras próprias de escopo e paralelismo; o nome familiar de um atributo não dispensa entender o lifecycle. Duas classes que escrevem na mesma base estática precisam de proteção ou serialização explícita para não cruzar dados.

## Como funciona
Use test class instance para estado novo por caso, fixtures compartilhadas só quando o custo justificar, dados nomeáveis e determinísticos e coleções para proteger recursos compartilhados. Crie CollectionDefinition e aplique Collection às classes dependentes somente quando compartilham recurso; prefira independência quando possível.

## Exemplo
Fixtures que usam o mesmo schema ficam numa collection; demais suites continuam paralelas em outras collections.

## Limites e trade-offs
Detalhes de fixtures, runner e modos de paralelismo variam entre xUnit v2 e v3 e entre versões do runner. Compartilhar fixture não a torna thread-safe, e ordem do teste não é contrato entre casos. Collection reduz paralelismo entre classes associadas e pode aumentar duração total da suíte.

## Como verificar
Confirme no log que classes da collection não se sobrepõem e que classes independentes ainda rodam em paralelo.

## Conexões
- [[xunit-class-fixture-compartilhar-recurso]] — Veja também: xUnit: usar class fixture somente para contexto realmente comum.
- [[xunit-async-lifetime-teardown]] — Veja também: xUnit: escolher lifecycle async compatível com versão.

## Fontes
- [xUnit.net — Sharing Context between Tests](https://xunit.net/docs/shared-context) — construtores, fixtures de classe/coleção, escopo e descarte; consultado em 2026-10-02.
- [xUnit.net — Running Tests in Parallel](https://xunit.net/docs/running-tests-in-parallel) — coleções, modos de paralelismo, limites e escopo de runner; consultado em 2026-10-02.
