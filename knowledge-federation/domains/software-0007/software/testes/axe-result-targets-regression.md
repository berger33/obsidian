---
id: software.testes.tranche12.000649
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

# axe-core: registrar alvos de nós para regressões

## Em uma frase
Resultados associam violações a nós e alvos, permitindo identificar onde uma regra encontrou o problema na árvore analisada.

## Por que importa
Persistir uma evidência pequena ajuda a reproduzir regressão sem congelar todo o objeto JSON, que pode variar conforme versão e renderização.

## Como funciona
Selecione campos estáveis como ID da regra, seletor alvo e contexto de rota; para repetir a análise, colete os arrays `node.target` e passe essa coleção a `axe.run(targets)` como contexto. Um único `target` também precisa ser envolvido em um array.

## Exemplo
Um teste pode relatar que `color-contrast` encontrou `.checkout-total` na tela de pagamento e manter uma assertion sobre a regra que importa.

## Limites e trade-offs
Seletor gerado pode mudar após refatoração sem mudança de acessibilidade, enquanto snapshots integrais podem falhar por metadados sem relevância para o contrato.

## Como verificar
Revise diffs de regra e alvo após atualizar axe-core e mantenha uma checagem ampla que encontre problemas fora dos seletores conhecidos.

## Conexões
- [[axe-dynamic-flows-multiple-scans]] — Veja também: axe-core: escanear separadamente estados de interação.

## Fontes
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
