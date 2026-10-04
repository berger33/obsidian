---
id: software.testes.tranche19.001320
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/garris/BackstopJS/blob/master/README.md", "https://garris.github.io/BackstopJS/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# BackstopJS: limitar a captura a elementos

## Em uma frase
O cenário pode capturar o documento inteiro, a área visível ou um conjunto de seletores, isolando regiões específicas da página.

## Por que importa
Capturar o componente sob teste reduz ruído de conteúdo dinâmico ao redor e localiza melhor a causa da diferença.

## Como funciona
Prefira seletores estáveis por atributo de teste, capture componentes críticos separadamente e evite depender de posição na árvore.

## Exemplo
Um cenário pode capturar apenas o cartão de produto, ignorando o carrossel de recomendações que muda a cada acesso.

## Limites e trade-offs
Seletores frágeis quebram com refatoração de estilo, e capturas muito amplas incluem dados voláteis que geram diferenças irrelevantes.

## Como verificar
Faça o seletor corresponder a zero elementos e confirme que o relatório indica a ausência em vez de capturar a página inteira.

## Conexões
- [[backstopjs-scenarios]] — Veja também: BackstopJS: descrever cenários.
- [[backstopjs-readiness]] — Veja também: BackstopJS: controlar o momento da captura.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — Página do projeto](https://garris.github.io/BackstopJS/) — demonstração e documentação publicada; consultado em 2026-10-03.
