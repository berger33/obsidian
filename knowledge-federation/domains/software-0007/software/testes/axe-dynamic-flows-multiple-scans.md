---
id: software.testes.tranche12.000648
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
fontes: ["https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md", "https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: escanear separadamente estados de interação

## Em uma frase
Uma página interativa pode revelar conteúdo novo após abrir modal, menu ou erro de formulário, e cada estado exige uma execução própria para ser observado.

## Por que importa
Um único scan de inicialização deixa fora rotas de interação nas quais foco, labels ou mensagens de erro podem apresentar problemas.

## Como funciona
Acione a interação com o runner de UI, aguarde o DOM estabilizar e rode axe-core depois de cada transição que altera conteúdo ou foco.

## Exemplo
Um teste de formulário pode examinar o estado limpo e depois submeter vazio para analisar mensagens de validação que só aparecem após a tentativa.

## Limites e trade-offs
Esperas arbitrárias não garantem que a animação ou atualização assíncrona terminou; uma assertion de estado deve confirmar a transição observada.

## Como verificar
Faça a análise falhar se a mensagem de erro não apareceu antes do scan e confira que ambos os estados geram resultados independentes.

## Conexões
- [[axe-tags-nao-cobertura-total-wcag]] — Veja também: axe-core: interpretar tags como escopo de regras.
- [[axe-result-targets-regression]] — Veja também: axe-core: registrar alvos de nós para regressões.

## Fontes
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
