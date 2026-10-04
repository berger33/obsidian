---
id: software.testes.tranche23.001684
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

# Testar Swing e AWT por imagem, com namer específico de SO

## Em uma frase
O tutorial documenta AwtApprovals.verify(componente) para qualquer herdeiro de java.awt.Component: o teste constrói a UI por código (o exemplo expõe um método selectTime em vez de clicar na interface) e o resultado verificado é um screenshot PNG do painel, aprovado como arquivo de imagem.

## Por que importa
Componentes Swing têm layout e estado visual que nenhum assert textual pega; a verificação por imagem captura o que o usuário veria, mantendo o teste programático — "we are programmers, and are not limited by the constraints of the UI", justifica a página.

## Como funciona
A página antecipa o problema de renderização entre plataformas: como o desenho difere por SO, existe NamerFactory.asOsSpecificTest(), que acrescenta o tipo de sistema operacional ao nome do arquivo de aprovação (por exemplo a sufixo Windows_10 visto no repositório), permitindo um arquivo aprovado por plataforma.

## Exemplo
Renderize um JPanel simples em verify, aprove o PNG no seu SO e confirme o par .approved/.received em imagem; depois, ative o namer de SO e veja o nome do arquivo incorporar a plataforma.

## Limites e trade-offs
Testes por screenshot tornam a aprovação mais cara (exige olhar imagem) e são inerentemente acoplados a fontes, DPI e tema — a própria solução de namer por SO admite que a identidade do esperado é multi-plataforma.

## Como verificar
Abra a seção Swing / AWT do tutorial Getting Started e confirme o AwtApprovals, a filosofia de não manipular a UI diretamente e a menção ao namer por sistema operacional.

## Conexões
- [[approvaltests-json-objects]] — Veja também: verifyAsJson quando o toString não resolve.
- [[approvaltests-combinations]] — Veja também: verifyAllCombinations: o produto cartesiano aprovado de uma vez.

## Fontes
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
