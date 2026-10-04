---
id: software.testes.tranche23.001682
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
fontes: ["https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md", "https://github.com/approvals/ApprovalTests.Java/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# verify para o todo, verifyAll para itens rotulados

## Em uma frase
O tutorial mostra a separação: todo teste tem a parte Do e a parte Verify, e a verificação no ApprovalTests é Approvals.verify(objetoToBeVerified) — para sequências, Approvals.verifyAll(label, itens) imprime cada elemento indexado sob o rótulo dado, por exemplo Text[0] = Approval e Text[1] = Tests.

## Por que importa
verifyAll transforma lista não ordenada em texto estável e legível: o índice visível permite ao revisor bater o olho na saída e ao diff apontar exatamente qual posição mudou, em vez de um blob de toString.

## Como funciona
Os exemplos oficiais percorrem tipos: uma string concatenada vira o conteúdo do approved .txt (Approval Tests); um Rectangle vira java.awt.Rectangle[x=5,y=10,width=100,height=200] — o texto do toString é o que se aprova — e o array de nomes ordenado sai rotulado [0] = Dan até [4] = Llewellyn.

## Exemplo
Verifique um List ordenado com verifyAll e uma linha formatada com verify; depois mude um elemento e confira que o relatório de falha é um diff posicional, não uma igualdade de strings gigantes.

## Limites e trade-offs
A qualidade da saída de objeto depende do toString — o tutorial ressalva a necessidade de um toString "useful" — e o exemplo do README usa um array de nomes; para coleções com ordem não determinística, a responsabilidade de normalizar antes de verificar é do autor do teste.

## Como verificar
Abra as seções Strings, Objects e Arrays do tutorial Getting Started e o snippet demo do README com o exemplo verifyAll ordenado.

## Conexões
- [[approvaltests-received-approved]] — Veja também: O par .received e .approved é o protocolo do teste.
- [[approvaltests-json-objects]] — Veja também: verifyAsJson quando o toString não resolve.

## Fontes
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
