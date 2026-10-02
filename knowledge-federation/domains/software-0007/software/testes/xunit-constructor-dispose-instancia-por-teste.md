---
id: software.testes.tranche11.000503
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

# xUnit: usar constructor e Dispose para contexto novo por caso

## Em uma frase
xUnit cria instância nova da classe de teste para cada test que executa; constructor e Dispose oferecem preparação e limpeza por instância.

## Por que importa
xUnit.net cria casos a partir de Facts/Theories e gerencia instâncias e fixtures com regras próprias de escopo e paralelismo; o nome familiar de um atributo não dispensa entender o lifecycle. Campo de instância novo reduz interferência entre testes da mesma classe e torna precondição próxima da assertion.

## Como funciona
Use test class instance para estado novo por caso, fixtures compartilhadas só quando o custo justificar, dados nomeáveis e determinísticos e coleções para proteger recursos compartilhados. Inicialize recurso local no constructor e implemente IDisposable para liberar o mesmo recurso após o caso.

## Exemplo
Cada teste recebe uma lista vazia nova e adiciona elementos sem que método seguinte observe o estado anterior.

## Limites e trade-offs
Detalhes de fixtures, runner e modos de paralelismo variam entre xUnit v2 e v3 e entre versões do runner. Compartilhar fixture não a torna thread-safe, e ordem do teste não é contrato entre casos. Constructor é síncrono; use lifecycle assíncrono documentado quando criação ou cleanup depende de await.

## Como verificar
Execute testes em ordem aleatória e confirme que identidade de instância muda por caso e cleanup ocorre após falhas.

## Conexões
- [[xunit-memberdata-classdata-provedor-tipado]] — Veja também: xUnit: mover dados reutilizáveis para MemberData ou ClassData.
- [[xunit-class-fixture-compartilhar-recurso]] — Veja também: xUnit: usar class fixture somente para contexto realmente comum.

## Fontes
- [xUnit.net — Sharing Context between Tests](https://xunit.net/docs/shared-context) — construtores, fixtures de classe/coleção, escopo e descarte; consultado em 2026-10-02.
- [xUnit.net — Getting Started with xUnit.net v3](https://xunit.net/docs/getting-started/v3/getting-started) — execução em v3 e configuração de métodos/casos assíncronos; consultado em 2026-10-02.
