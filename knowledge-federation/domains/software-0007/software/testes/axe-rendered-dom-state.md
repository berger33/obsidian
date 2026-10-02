---
id: software.testes.tranche12.000640
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

# axe-core: executar análise depois de renderizar o estado

## Em uma frase
axe.run analisa conteúdo renderizado no documento e não avalia automaticamente regiões ocultas que ainda não foram ativadas.

## Por que importa
Executar no momento errado pode deixar menus, diálogos e painéis fora do resultado, produzindo falsa impressão de que o fluxo inteiro foi verificado.

## Como funciona
Renderize a página e estabilize a transição relevante, carregue axe-core no documento e rode uma análise distinta depois de cada estado importante se ele revelar conteúdo novo.

## Exemplo
Um teste pode abrir primeiro o menu de conta e depois o diálogo de ajuda, chamando a análise em cada estado visível em vez de testar apenas a tela inicial.

## Limites e trade-offs
A análise automática cobre regras e DOM presentes naquele momento; ela não percorre sozinha ações futuras nem conteúdo que permaneça inativo.

## Como verificar
Confira no teste que o elemento foi ativado e está no DOM antes de chamar `axe.run`, então confirme que o resultado inclui os nós esperados.

## Conexões
- [[axe-context-include-exclude]] — Veja também: axe-core: restringir contexto sem abandonar cobertura.

## Fontes
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
