---
id: software.testes.tranche16.001024
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/pa11y/pa11y", "https://github.com/pa11y/pa11y-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pa11y: escolher o padrão de conformidade

## Em uma frase
O nível de conformidade pode ser declarado entre os três níveis de acessibilidade e é usado apenas pelo motor baseado em regras estáticas.

## Por que importa
Declarar o nível explicitamente evita que uma atualização da ferramenta mude silenciosamente o conjunto de critérios aplicados.

## Como funciona
Fixe o padrão na configuração, registre a decisão e amplie o rigor conforme o passivo de acessibilidade diminui.

## Exemplo
Um projeto que mira o nível intermediário pode começar por ele e promover o nível avançado quando a dívida conhecida for tratada.

## Limites e trade-offs
O motor de regras cobre versões específicas das diretrizes, e critérios mais recentes exigem o outro motor ou verificações adicionais.

## Como verificar
Compare a contagem de problemas entre dois níveis de conformidade na mesma página para tornar visível o custo de adotar o nível mais rígido.

## Conexões
- [[pa11y-cli-basics]] — Veja também: Pa11y: executar a varredura de uma página.
- [[pa11y-runners]] — Veja também: Pa11y: combinar motores de verificação.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
