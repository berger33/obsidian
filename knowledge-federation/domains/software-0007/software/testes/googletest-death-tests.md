---
id: software.testes.tranche18.001194
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
fontes: ["https://google.github.io/googletest/advanced.html", "https://github.com/google/googletest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: verificar encerramentos esperados

## Em uma frase
As asserções de morte verificam que determinado trecho encerra o processo, opcionalmente conferindo o código de saída e a mensagem emitida.

## Por que importa
Validações que encerram o processo, como verificações de contrato, não podem ser exercitadas por asserções comuns.

## Como funciona
Use a asserção de morte apenas para comportamento que realmente encerra o processo, conferindo código e mensagem, e observe as restrições de uso.

## Exemplo
Uma função que aborta ao receber entrada inválida pode ser verificada quanto ao código de saída e ao texto emitido no erro.

## Limites e trade-offs
O trecho sob verificação executa em processo separado, e efeitos colaterais e liberação de memória não são visíveis ao processo principal.

## Como verificar
Substitua a mensagem esperada por outra e confirme que a asserção falha, evidenciando a verificação do texto.

## Conexões
- [[googletest-mocks-integration]] — Veja também: GoogleTest: integrar dublês com a suíte.
- [[googletest-running-and-filtering]] — Veja também: GoogleTest: executar e filtrar casos.

## Fontes
- [GoogleTest — Advanced](https://google.github.io/googletest/advanced.html) — fixtures, parametrização, testes por tipo, filtros e asserções de morte; consultado em 2026-10-03.
- [GoogleTest — repositório oficial](https://github.com/google/googletest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
