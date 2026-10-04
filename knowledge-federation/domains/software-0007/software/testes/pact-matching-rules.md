---
id: software.testes.tranche17.001128
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.pact.io/implementation_guides/javascript/docs/matching", "https://github.com/pact-foundation/pact-js"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: usar correspondência flexível

## Em uma frase
As regras de correspondência verificam forma e tipo em vez de valores exatos, aceitando identificadores variáveis, listas de tamanho mínimo e padrões textuais.

## Por que importa
Valores fixos nos contratos fazem a verificação falhar por dados legítimos diferentes, enquanto tipos e formas preservam a intenção da expectativa.

## Como funciona
Aplique regras para campos gerados, listas e formatos textuais, e reserve igualdade exata para constantes do domínio.

## Exemplo
Um contrato de listagem pode exigir ao menos um item com identificador numérico e nome textual, sem fixar os valores que o provedor devolver.

## Limites e trade-offs
Correspondência frouxa demais aceita respostas que quebram o consumidor, e o excesso de regras dificulta a leitura do contrato.

## Como verificar
Altere um valor legítimo no provedor simulado e confirme que a verificação continua passando, depois mude o tipo do campo e confirme que ela falha.

## Conexões
- [[pact-consumer-test-dsl]] — Veja também: Pact: escrever a interação de teste.
- [[pact-provider-states]] — Veja também: Pact: preparar estados do provedor.

## Fontes
- [Pact — Matching rules](https://docs.pact.io/implementation_guides/javascript/docs/matching) — regras de tipo, lista e padrão em vez de valores exatos; consultado em 2026-10-03.
- [Pact — repositório oficial](https://github.com/pact-foundation/pact-js) — implementação de referência em JavaScript e exemplos; consultado em 2026-10-03.
