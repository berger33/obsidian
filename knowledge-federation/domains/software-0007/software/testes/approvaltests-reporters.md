---
id: software.testes.tranche23.001686
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

# Reporters: a diferença é apresentada pela ferramenta certa

## Em uma frase
Quando uma aprovação falha, um reporter é invocado para apresentar received e approved; o mecanismo de escolha é a anotação @UseReporter(Reporter.class) no método ou na classe, e a tabela oficial lista os reporters comuns com suas funções exatas.

## Por que importa
A experiência de aprovação é o produto real da ferramenta: uma fila de diff no editor de diff preferido, um comando move no clipboard ou console limpo em CI — a mesma falha serve a públicos diferentes, e isso é configuração, não fork.

## Como funciona
A tabela documenta ClipboardReporter (põe o comando move no clipboard), DiffReporter (lança o diff tool especificado), FileLauncherReporter, ImageReporter e ImageWebReporter (abrem texto/imagem em editor ou navegador), JunitReporter (texto como falha assertEquals), NotePadLauncher, QuietReporter (imprime o comando move no console — "great for build systems") e TextWebReporter.

## Exemplo
Anote sua classe de teste com @UseReporter(DiffReporter.class) com seu editor de diff configurado e @UseReporter(QuietReporter.class) no perfil de CI, e veja a mesma falha se manifestar como janela de diff ou linha de comando no log.

## Limites e trade-offs
A página admite explicitamente que ferramentas fora da lista de diff tools suportadas — ou instaladas em pastas não padrão — exigem Custom Reporter; o conjunto "muitos reporters" é extensível, não exaustivo por padrão.

## Como verificar
Abra a seção Reporters do tutorial Getting Started e confira a anotação @UseReporter nos dois níveis e a tabela com os dez reporters descritos.

## Conexões
- [[approvaltests-combinations]] — Veja também: verifyAllCombinations: o produto cartesiano aprovado de uma vez.
- [[approvaltests-java-fitness]] — Veja também: Compatibilidade Java: JUnit 3/4/5, TestNG e JDK 8+.

## Fontes
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
