---
id: software.testes.tranche11.000508
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
fontes: ["https://xunit.net/docs/capturing-output", "https://xunit.net/docs/shared-context"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# xUnit: associar diagnóstico ao teste com ITestOutputHelper

## Em uma frase
ITestOutputHelper fornece saída associada ao test case, enquanto Console e Trace são recursos compartilhados do processo.

## Por que importa
xUnit.net cria casos a partir de Facts/Theories e gerencia instâncias e fixtures com regras próprias de escopo e paralelismo; o nome familiar de um atributo não dispensa entender o lifecycle. Console.WriteLine concorrente pode misturar mensagens de testes e dificultar saber qual contexto produziu a linha.

## Como funciona
Use test class instance para estado novo por caso, fixtures compartilhadas só quando o custo justificar, dados nomeáveis e determinísticos e coleções para proteger recursos compartilhados. Injete o helper no construtor do teste e escreva somente informações úteis, sem segredo ou dumps excessivos.

## Exemplo
Um teste registra correlation id sintético e valor esperado usando seu helper para que runner associe output à falha correta.

## Limites e trade-offs
Detalhes de fixtures, runner e modos de paralelismo variam entre xUnit v2 e v3 e entre versões do runner. Compartilhar fixture não a torna thread-safe, e ordem do teste não é contrato entre casos. Captura direta de Console em xUnit v3 é configurável e desabilitada por default para compatibilidade; não presuma mesma política entre versões.

## Como verificar
Execute dois casos concorrentes com mensagens distintas e confirme que cada saída aparece associada ao caso correto.

## Conexões
- [[xunit-paralelismo-por-collection-isolar]] — Veja também: xUnit: entender paralelismo por collection antes de aumentar threads.
- [[xunit-assert-throws-tipo-exato]] — Veja também: xUnit: afirmar exceção esperada no ponto da chamada.

## Fontes
- [xUnit.net — Capturing Output](https://xunit.net/docs/capturing-output) — ITestOutputHelper, console e captura associada a testes; consultado em 2026-10-02.
- [xUnit.net — Sharing Context between Tests](https://xunit.net/docs/shared-context) — construtores, fixtures de classe/coleção, escopo e descarte; consultado em 2026-10-02.
