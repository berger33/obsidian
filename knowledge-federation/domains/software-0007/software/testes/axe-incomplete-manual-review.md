---
id: software.testes.tranche12.000645
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md", "https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: revisar resultados marcados como incomplete

## Em uma frase
Uma regra que não consegue decidir automaticamente pode aparecer em `incomplete` com nós que demandam avaliação adicional.

## Por que importa
Tratar esses itens como aprovação automática elimina o sinal de que uma condição importante continua sem resposta mecânica.

## Como funciona
Apresente descrição da regra, alvos e motivo de revisão ao responsável e registre decisão manual fora do status automatizado.

## Exemplo
Um contraste sobre imagem pode depender de conteúdo visual que a regra não consegue inferir e precisa de inspeção humana contextual.

## Limites e trade-offs
O item incompleto não é equivalente a uma violação comprovada nem a um passe; pode continuar aberto até que evidência manual exista.

## Como verificar
Crie um relatório de exemplo com resultado incompleto e confirme que o processo de triagem o encaminha para revisão em vez de descartá-lo.

## Conexões
- [[axe-result-categories]] — Veja também: axe-core: distinguir violations, passes, incomplete e inapplicable.
- [[axe-impact-priorizacao-nao-conformidade]] — Veja também: axe-core: usar impact para priorizar sem certificar conformidade.

## Fontes
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
