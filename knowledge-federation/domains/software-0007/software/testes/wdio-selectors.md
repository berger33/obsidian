---
id: software.testes.tranche18.001167
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://webdriver.io/docs/selectors", "https://webdriver.io/docs/gettingstarted"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: localizar elementos com clareza

## Em uma frase
Os seletores aceitam estilo, texto, identificador de acessibilidade e estratégias específicas de plataforma móvel, com retorno de um ou vários elementos.

## Por que importa
A escolha do seletor determina a estabilidade do teste entre navegadores e dispositivos, e estratégias semânticas sobrevivem a mudanças de layout.

## Como funciona
Prefira identificadores de testabilidade ou rótulos de acessibilidade, reserve estilos para casos simples e evite posições estruturais.

## Exemplo
Um botão pode ser consultado por identificador de testabilidade, funcionando tanto no navegador quanto no aplicativo móvel.

## Limites e trade-offs
Seletores acoplados a classes de estilo quebram com refatoração visual, e o seletor de texto exige cuidado com a tradução da interface.

## Como verificar
Renomeie uma classe de estilo e confirme que os testes baseados em identificador continuam passando sem ajuste.

## Conexões
- [[wdio-waiting-strategies]] — Veja também: WebdriverIO: esperar condições de elemento.

## Fontes
- [WebdriverIO — Selectors](https://webdriver.io/docs/selectors) — estratégias de seleção por estilo, acessibilidade e plataforma; consultado em 2026-10-03.
- [WebdriverIO — Documentation](https://webdriver.io/docs/gettingstarted) — configuração, modos de execução, serviços e paralelismo; consultado em 2026-10-03.
