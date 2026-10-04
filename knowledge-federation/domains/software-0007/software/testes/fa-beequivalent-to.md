---
id: software.testes.tranche22.001597
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://www.fluentassertions.com/objectgraphs/", "https://www.fluentassertions.com/introduction"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# FluentAssertions: BeEquivalentTo entre DTOs

## Em uma frase
A asserção estrutural entre object graphs é orderDto.Should().BeEquivalentTo(order): todos os membros expostos do grafo expectativa precisam casar por nome e valor com o sujeito, e NotBeEquivalentTo cobre a desigualdade com as mesmas opções.

## Por que importa
DTOs, comandos e payloads de API são comparados por estrutura, não por instância; reimplementar essa travessia em teste na mão é onde nasce o assert-brittle.

## Como funciona
A comparação é recursiva por padrão, com teto de 10 níveis para evitar recursão infinita; AllowingInfiniteRecursion força profundidade total e ExcludingNestedObjects desliga a recursão.

## Exemplo
Pelas regras de matching, todo membro público de Order precisa existir no OrderDto com o mesmo nome — membros faltando lançam exceção, e ExcludingMissingMembers relaxa isso quando os contratos divergem de propósito.

## Limites e trade-offs
Tipos diferentes podem ser equivalentes: por padrão a comparação ignora se os tipos são exatamente iguais e olha membros; use WithStrictTyping quando a identidade do tipo importa.

## Como verificar
Adicione uma propriedade nova só no Order e confirme que BeEquivalentTo reclama do membro desbalanceado antes de qualquer mudança de valor.

## Conexões
- [[fa-subject-identification]] — Veja também: FluentAssertions: o nome da variável no erro.
- [[fa-value-semantics]] — Veja também: FluentAssertions: por valor ou por membros.

## Fontes
- [FluentAssertions — Object graphs](https://www.fluentassertions.com/objectgraphs/) — BeEquivalentTo, recursão, tipagem, exclusões e auto-conversão; consultado em 2026-10-03.
- [FluentAssertions — Introduction](https://www.fluentassertions.com/introduction) — chaining, frameworks detectados, subject identification e AssertionScope; consultado em 2026-10-03.
