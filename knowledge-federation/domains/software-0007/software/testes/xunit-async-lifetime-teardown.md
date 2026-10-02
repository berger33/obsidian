---
id: software.testes.tranche11.000506
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
fontes: ["https://xunit.net/docs/shared-context", "https://xunit.net/docs/getting-started/v3/getting-started"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# xUnit: escolher lifecycle async compatível com versão

## Em uma frase
xUnit oferece interfaces de lifecycle assíncrono para inicialização e limpeza; suportes de DisposeAsync diferem entre v2 e v3.

## Por que importa
xUnit.net cria casos a partir de Facts/Theories e gerencia instâncias e fixtures com regras próprias de escopo e paralelismo; o nome familiar de um atributo não dispensa entender o lifecycle. Bloquear async no constructor pode causar deadlock ou estado parcialmente pronto antes da assertion.

## Como funciona
Use test class instance para estado novo por caso, fixtures compartilhadas só quando o custo justificar, dados nomeáveis e determinísticos e coleções para proteger recursos compartilhados. Use interface async correspondente à versão, aguarde setup antes dos testes e conclua cleanup sem deixar tasks pendentes.

## Exemplo
A fixture de integração aguarda container ficar pronto em InitializeAsync e encerra em DisposeAsync.

## Limites e trade-offs
Detalhes de fixtures, runner e modos de paralelismo variam entre xUnit v2 e v3 e entre versões do runner. Compartilhar fixture não a torna thread-safe, e ordem do teste não é contrato entre casos. Não transfira diretamente exemplos de xUnit v3 para v2; verifique interface e método de cleanup disponíveis no pacote do projeto.

## Como verificar
Compile e execute com versão fixada e force falha após setup para verificar limpeza assíncrona.

## Conexões
- [[xunit-collection-fixture-serializar-recurso]] — Veja também: xUnit: agrupar classes por collection quando compartilham recurso.
- [[xunit-paralelismo-por-collection-isolar]] — Veja também: xUnit: entender paralelismo por collection antes de aumentar threads.

## Fontes
- [xUnit.net — Sharing Context between Tests](https://xunit.net/docs/shared-context) — construtores, fixtures de classe/coleção, escopo e descarte; consultado em 2026-10-02.
- [xUnit.net — Getting Started with xUnit.net v3](https://xunit.net/docs/getting-started/v3/getting-started) — execução em v3 e configuração de métodos/casos assíncronos; consultado em 2026-10-02.
