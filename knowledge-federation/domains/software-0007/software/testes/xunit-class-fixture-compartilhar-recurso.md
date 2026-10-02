---
id: software.testes.tranche11.000504
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

# xUnit: usar class fixture somente para contexto realmente comum

## Em uma frase
IClassFixture compartilha uma instância de fixture entre os testes de uma classe e a descarta depois da classe.

## Por que importa
xUnit.net cria casos a partir de Facts/Theories e gerencia instâncias e fixtures com regras próprias de escopo e paralelismo; o nome familiar de um atributo não dispensa entender o lifecycle. Abrir banco ou servidor por caso pode ser caro, mas compartilhar uma conexão mutável sem coordenação causa races.

## Como funciona
Use test class instance para estado novo por caso, fixtures compartilhadas só quando o custo justificar, dados nomeáveis e determinísticos e coleções para proteger recursos compartilhados. Mantenha fixture com estado imutável ou concorrência segura e deixe cada caso criar seu próprio namespace ou transação de dados.

## Exemplo
A fixture inicializa container uma vez; cada teste recebe a fixture e aloca schema com id exclusivo.

## Limites e trade-offs
Detalhes de fixtures, runner e modos de paralelismo variam entre xUnit v2 e v3 e entre versões do runner. Compartilhar fixture não a torna thread-safe, e ordem do teste não é contrato entre casos. A classe de teste ainda pode ter instância nova por caso; recurso fixture é que permanece compartilhado.

## Como verificar
Conte inicializações e execute casos em paralelo quando aplicável, verificando que uso concorrente é seguro.

## Conexões
- [[xunit-constructor-dispose-instancia-por-teste]] — Veja também: xUnit: usar constructor e Dispose para contexto novo por caso.
- [[xunit-collection-fixture-serializar-recurso]] — Veja também: xUnit: agrupar classes por collection quando compartilham recurso.

## Fontes
- [xUnit.net — Sharing Context between Tests](https://xunit.net/docs/shared-context) — construtores, fixtures de classe/coleção, escopo e descarte; consultado em 2026-10-02.
- [xUnit.net — Running Tests in Parallel](https://xunit.net/docs/running-tests-in-parallel) — coleções, modos de paralelismo, limites e escopo de runner; consultado em 2026-10-02.
