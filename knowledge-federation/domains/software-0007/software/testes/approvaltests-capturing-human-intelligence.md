---
id: software.testes.tranche23.001680
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/approvals/ApprovalTests.Java/blob/master/README.md", "https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ApprovalTests: capturar inteligência humana em vez de codar expectativas

## Em uma frase
O README oficial se abre com "Capturing Human Intelligence" e define o ApprovalTests como biblioteca open source de asserção/verificação para ajudar testes unitários, usada quando o objeto exige "more than a simple assert" — coleções, strings longas, logs, JPanels, XML, HTML, JSON e até colocar código legado sob teste.

## Por que importa
Em saídas grandes e estruturadas, escrever o esperado no código é caro e frágil; a verificação por aprovação inverte o fluxo: o humano examina a saída real uma vez e a registra como referência.

## Como funciona
A API central é um único ponto — Approvals.verify(objeto) — e a expectativa vive fora do código, em arquivos lado a lado com o teste; o próprio projeto descreve que "come prepackaged with utilities" para os cenários Java citados.

## Exemplo
Adicione a dependência com escopo test num projeto Maven, verifique o toString de um objeto simples e veja nascer o arquivo de aprovação ao lado da classe de teste — o ciclo completo cabe em cinco minutos.

## Limites e trade-offs
A biblioteca é por linguagem (a página documenta o ApprovalTests.Java; existem ports em outras stacks); e o lema de capturar julgamento humano transfere responsabilidade: o revisor precisa de fato olhar a saída antes de aprovar.

## Como verificar
Abra o topo do README oficial em approvals/ApprovalTests.Java e confirme o slogan, a definição de biblioteca de verificação e a lista de usos empacotados.

## Conexões
- [[approvaltests-received-approved]] — Veja também: O par .received e .approved é o protocolo do teste.

## Fontes
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
