---
id: software.testes.tranche20.001422
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
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://notwoods.github.io/mockk-guidebook/docs/mocking/coroutines/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: capturar argumentos com slots

## Em uma frase
Um slot registra o valor recebido por uma chamada, permitindo verificar detalhes do argumento depois da execução.

## Por que importa
Capturar o argumento verifica o conteúdo efetivamente enviado quando a assinatura não permite a comparação direta.

## Como funciona
Declare o slot para o tipo adequado, capture dentro da verificação e verifique os campos do valor capturado.

## Exemplo
O teste pode capturar a mensagem enviada e confirmar que o campo de destinatário corresponde ao usuário esperado.

## Limites e trade-offs
Slots reutilizados entre verificações do mesmo caso retêm o último valor e confundem a leitura; capture apenas o que for necessário verificar.

## Como verificar
Envie um valor diferente do esperado e confirme que a verificação sobre o valor capturado falha indicando o conteúdo recebido.

## Conexões
- [[mockk-verification]] — Veja também: MockK: verificar chamadas realizadas.
- [[mockk-coroutines]] — Veja também: MockK: dublar funções suspensas.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — Guia de corrotinas](https://notwoods.github.io/mockk-guidebook/docs/mocking/coroutines/) — uso das variantes para funções suspensas; consultado em 2026-10-03.
