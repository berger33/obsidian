---
id: software.testes.tranche20.001421
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://github.com/mockk/mockk"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: verificar chamadas realizadas

## Em uma frase
Blocos de verificação confirmam que a chamada ocorreu, com quantidade exata, faixa de ocorrências e ordem entre chamadas.

## Por que importa
Verificar o efeito no colaborador confirma o contrato de interação que o retorno do método sozinho não revela.

## Como funciona
Verifique a chamada essencial com quantidade explícita e use verificação de ordem quando a sequência for parte do comportamento.

## Exemplo
O teste pode exigir que o aviso tenha sido enviado exatamente uma vez, mesmo quando a resposta visível é igual em caso de duplicação.

## Limites e trade-offs
Verificar tudo o que o código chama acopla o teste à implementação, e verificar nada abre mão de confirmar o efeito combinado.

## Como verificar
Remova a chamada em teste e confirme que a verificação falha indicando a chamada esperada e o número observado.

## Conexões
- [[mockk-strict-vs-relaxed]] — Veja também: MockK: escolher entre modo estrito e relaxado.
- [[mockk-slots-and-capture]] — Veja também: MockK: capturar argumentos com slots.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — repositório oficial](https://github.com/mockk/mockk) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
