---
id: software.testes.tranche18.001193
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://github.com/google/googletest", "https://google.github.io/googletest/advanced.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: integrar dublês com a suíte

## Em uma frase
A biblioteca de dublês complementa o framework, declarando expectativas sobre chamadas e valores de retorno das dependências.

## Por que importa
Colaborações com dependências externas ficam explícitas no teste, e a verificação de chamadas cobre comportamento que o resultado isolado não mostra.

## Como funciona
Declare a classe de dublê, registre as expectativas antes do exercício e verifique ao final do caso.

## Exemplo
Um serviço de envio pode ser substituído por dublê que exige uma chamada com o destinatário correto e devolve sucesso.

## Limites e trade-offs
Expectativas que aceitam qualquer argumento perdem o valor de verificação, e dublês usados fora de escopo geram erros de ciclo de vida.

## Como verificar
Remova a chamada no código de produção e confirme que a verificação acusa a expectativa não satisfeita.

## Conexões
- [[googletest-typed-tests]] — Veja também: GoogleTest: reutilizar casos entre tipos.
- [[googletest-death-tests]] — Veja também: GoogleTest: verificar encerramentos esperados.

## Fontes
- [GoogleTest — repositório oficial](https://github.com/google/googletest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
- [GoogleTest — Advanced](https://google.github.io/googletest/advanced.html) — fixtures, parametrização, testes por tipo, filtros e asserções de morte; consultado em 2026-10-03.
