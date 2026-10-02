---
id: software.testes.tranche13.000728
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://spockframework.org/spock/docs/2.4/all_in_one.html#_conditions", "https://spockframework.org/spock/docs/2.4/all_in_one.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: capturar exceção como parte da condição esperada

## Em uma frase
Condições de Spock ajudam verificar comportamento de exceção no caminho em que ela é lançada.

## Por que importa
Teste de falha deve demonstrar tipo e conteúdo relevantes da exceção, não aceitar qualquer erro que esconda defeito diferente.

## Como funciona
Execute chamada no bloco de estímulo, capture tipo esperado com mecanismo documentado e valide mensagem ou estado adicional somente quando fizer parte do contrato.

## Exemplo
Uma entrada inválida pode exigir `IllegalArgumentException` com campo identificado antes de persistência tentar iniciar transação.

## Limites e trade-offs
Capturar exceção ampla demais ou lançada por setup não demonstra que a operação sob teste falhou pelo motivo esperado.

## Como verificar
Provoque exceção no ponto de chamada e uma falha em setup separada; confirme que apenas a primeira satisfaz condição da feature.

## Conexões
- [[spock-lenient-mock-scope]] — Veja também: Spock: evitar over-specification em mocks lenientes.
- [[spock-extension-boundary]] — Veja também: Spock: usar extension para política transversal.

## Fontes
- [Spock 2.4 — Conditions](https://spockframework.org/spock/docs/2.4/all_in_one.html#_conditions) — implicit conditions and diagnostic rendering; consultado em 2026-10-02.
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
