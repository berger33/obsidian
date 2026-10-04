---
id: software.testes.tranche16.001033
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

# Pa11y: reconhecer o limite da verificação automática

## Em uma frase
A varredura detecta parte dos problemas de acessibilidade, mas não avalia qualidade da experiência com tecnologia assistiva real.

## Por que importa
Declarar conformidade total com base apenas na ferramenta cria falsa garantia e deixa barreiras importantes sem verificação.

## Como funciona
Combine a varredura com verificação manual de teclado, leitura por tecnologia assistiva e revisão de conteúdo, registrando o que ficou fora do alcance automático.

## Exemplo
Ordem de foco, texto alternativo significativo e clareza de mensagens de erro exigem julgamento humano que a análise estática não substitui.

## Limites e trade-offs
Avisos e notificações ficam fora do relatório por padrão, e problemas em estados dinâmicos só aparecem com preparação por ações.

## Como verificar
Escolha uma jornada crítica e execute-a apenas com teclado, comparando o que funciona com o que a varredura havia reportado.

## Conexões
- [[pa11y-ci-environment]] — Veja também: Pa11y CI: preparar ambiente e navegador.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
