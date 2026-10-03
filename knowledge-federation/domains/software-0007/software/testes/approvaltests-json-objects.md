---
id: software.testes.tranche23.001683
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

# verifyAsJson quando o toString não resolve

## Em uma frase
Para objetos sem toString útil — ou quando criar um não é desejável — o tutorial documenta JsonApprovals.verifyAsJson(objeto), que serializa o conteúdo e produz um arquivo de aprovação com extensão .json, por exemplo as chaves x, y, width e height do Rectangle aprovado como documento JSON indentado.

## Por que importa
JSON estruturado é mais barato de revisar que um toString denso: o revisor compara campos com nome, e diffs pontuais permanecem legíveis quando um único campo muda entre versões do objeto.

## Como funciona
A escolha de extensão vem junto: enquanto verify textual gera .approved.txt, verifyAsJson gera .approved.json — o nome do arquivo carrega o tipo, e ferramentas de diff entendem o formato.

## Exemplo
Troque um verify(obj.toString()) problemático por verifyAsJson(obj), aprove a saída e modifique um campo para ver o diff JSON isolando exatamente a chave alterada.

## Limites e trade-offs
O documento de aprovação é JSON gerado a partir do estado do objeto: campos com ordem instável, referências cíclicas ou tipos sem serialização JSON padronizada pedem atenção extra — a página não cobre configurações de serialização.

## Como verificar
Abra a subseção Using JSON do tutorial Getting Started e confirme a justificativa (sem toString definido ou indesejado), a classe JsonApprovals e o nome de arquivo .approved.json.

## Conexões
- [[approvaltests-verify-and-verifyall]] — Veja também: verify para o todo, verifyAll para itens rotulados.
- [[approvaltests-awt-image]] — Veja também: Testar Swing e AWT por imagem, com namer específico de SO.

## Fontes
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
