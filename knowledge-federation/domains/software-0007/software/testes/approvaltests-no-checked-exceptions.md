---
id: software.testes.tranche23.001689
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
fontes: ["https://github.com/approvals/ApprovalTests.Java/blob/master/README.md", "https://approvaltests.com/", "https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Filosofia sem exceções checked e API de runtime apenas

## Em uma frase
A seção More Info do README oficial declara a filosofia "No Checked Exceptions": a API do ApprovalTests lança apenas exceções de runtime — com documento explicativo no repositório — porque um assistente de verificação que força try/catch no teste contaminaria justamente o código que deveria permanecer leitura pura de intenção.

## Por que importa
Em DSLs de teste, boilerplate de assinatura polui cada método; a política documentada garante que Approvals.verify possa ser chamado em qualquer teste sem propagar throws, mantendo o ponto de chamada trivial.

## Como funciona
A mesma seção ancora o resto do ecossistema de aprendizado: o site approvaltests.com como porta de entrada, os vídeos e a observação útil de que os muitos materiais sobre ApprovalTests .NET "são igualmente úteis para entender os conceitos apesar de serem em outra linguagem".

## Exemplo
Chame Approvals.verify dentro de um @Test sem declarar throws e confirme que a falha por não aprovação se manifesta como exceção de runtime no relatório do framework, sem alterar a assinatura.

## Limites e trade-offs
O documento aponta a filosofia, não um contrato de tipos de exceção específicos para cada condição — quem precisar capturar a falha programaticamente (runners customizados, por exemplo) deve consultar o javadoc da versão em uso.

## Como verificar
Abra a seção No Checked Exceptions Philosophy do README oficial e confirme a frase da política, o link do documento explicativo e a nota sobre material .NET.

## Conexões
- [[approvaltests-legacy-code]] — Veja também: Approval testing como ponte para legado e dogfood.

## Fontes
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
- [ApprovalTests — site oficial](https://approvaltests.com/) — porta de entrada referenciada pelo README; consultado em 2026-10-03.
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
