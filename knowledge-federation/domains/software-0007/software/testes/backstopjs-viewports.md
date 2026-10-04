---
id: software.testes.tranche19.001324
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

# BackstopJS: cobrir tamanhos de tela

## Em uma frase
A configuração declara tamanhos de tela com rótulo e dimensões, aplicados a todos os cenários ou sobrescritos por cenário.

## Por que importa
Layouts responsivos mudam de forma por faixa, e verificar apenas um tamanho deixa faixas inteiras sem proteção visual.

## Como funciona
Defina os tamanhos correspondentes às faixas reais de uso, nomeie-os de forma reconhecível e limite a lista ao conjunto relevante.

## Exemplo
O componente de navegação pode ser verificado em largura de telefone, de tablet e de área de trabalho.

## Limites e trade-offs
Cobrir muitos tamanhos multiplica capturas e tempo de execução, e rótulos genéricos dificultam identificar a faixa que falhou.

## Como verificar
Provoque uma quebra de layout em faixa estreita e confirme que o cenário correspondente falha enquanto os outros passam.

## Conexões
- [[backstopjs-hiding-dynamic-content]] — Veja também: BackstopJS: isolar conteúdo dinâmico.
- [[backstopjs-reports-and-approval]] — Veja também: BackstopJS: revisar o relatório e aprovar mudanças.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — Página do projeto](https://garris.github.io/BackstopJS/) — demonstração e documentação publicada; consultado em 2026-10-03.
