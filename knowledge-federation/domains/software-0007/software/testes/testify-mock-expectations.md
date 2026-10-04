---
id: software.testes.tranche17.001140
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
fontes: ["https://pkg.go.dev/github.com/stretchr/testify/mock", "https://github.com/stretchr/testify"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testify: declarar expectativas de chamada

## Em uma frase
O pacote de dublês permite registrar chamadas esperadas com argumentos e valores de retorno e verificar, ao final, se todas ocorreram.

## Por que importa
Dublês com expectativa explícita documentam o contrato entre o código sob teste e suas dependências, revelando chamadas esquecidas ou extras.

## Como funciona
Registre a expectativa com os argumentos relevantes, devolva valores coerentes com esse cenário e verifique as expectativas no encerramento.

## Exemplo
Uma dependência de repositório pode ser configurada para devolver um registro e ter sua chamada conferida ao final do caso.

## Limites e trade-offs
Dublês que aceitam qualquer argumento perdem o valor de verificação, e esquecer a verificação final deixa expectativas não cumpridas sem sinal.

## Como verificar
Remova a chamada ao dublê no código de produção e confirme que a verificação final acusa a expectativa não satisfeita.

## Conexões
- [[testify-suite-lifecycle]] — Veja também: Testify: organizar casos em suítes.
- [[testify-mock-argument-matchers]] — Veja também: Testify: casar argumentos de forma flexível.

## Fontes
- [Testify — Mock package](https://pkg.go.dev/github.com/stretchr/testify/mock) — expectativas de chamada, correspondência de argumentos e verificação final; consultado em 2026-10-03.
- [Testify — repositório oficial](https://github.com/stretchr/testify) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
