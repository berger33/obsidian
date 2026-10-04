---
id: software.criacao_ia.tranche02.000196
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://diataxis.fr/explanation/", "https://diataxis.fr/how-to-guides/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Documentação Interativa: incorporar sandboxes de código executável em tutoriais

## Em uma frase
Sandboxes executáveis no navegador permitem que desenvolvedores testem trechos de código e shaders sem configurar ambientes locais complexos.

## Por que importa
A fricção de instalar dependências e ferramentas pesadas reduz a taxa de conclusão de tutoriais técnicos por novos desenvolvedores.

## Como funciona
Incorpore containers interativos WebAssembly (Wasm) ou iframes com editores como CodeSandbox, Godot Web Export ou StackBlitz diretamente nas páginas da documentação.

## Exemplo
```html
<!-- Exemplo de incorporacao de demo interativo via WebAssembly -->
<iframe
  src="https://meu-jogo.dev/demos/steering-sandbox.html"
  width="100%"
  height="450px"
  title="Demonstracao Interativa de Steering Behaviors"
></iframe>
```

## Limites e trade-offs
Demos em WebAssembly podem demorar para carregar em conexões lentas ou exigir navegadores modernos com suporte a SharedArrayBuffer.

## Como verificar
Abra a página de documentação no navegador e teste a execução do código interativo no sandbox incorporado.

## Conexões
- [[diataxis-elaborar-artigos-de-explicacao-e-design]] — Veja também: Diátaxis Explicação: aprofundar decisões arquiteturais e modelos conceituais.
- [[documentacao-explicar-grafos-de-shaders-e-materiais]] — Veja também: Documentação de Arte: detalhar entradas e nós matemáticos de shader graphs.
- [[documentacao-executar-exemplos-de-codigo]] — Conexão temática direta com documentacao-executar-exemplos-de-codigo.
- [[diataxis-construir-tutoriais-focados-no-primeiro-sucesso]] — Conexão temática direta com diataxis-construir-tutoriais-focados-no-primeiro-sucesso.
- [[documentacao-usar-imagens-acessiveis-e-uteis]] — Conexão temática direta com documentacao-usar-imagens-acessiveis-e-uteis.

## Fontes
- [Diátaxis Documentation Framework — Explanation](https://diataxis.fr/explanation/) — Especificação formal do quadrante de explicação, arquitetura conceitual e análise de trade-offs. Consulta: 2026-10-04.
- [Diátaxis Documentation Framework — How-to Guides](https://diataxis.fr/how-to-guides/) — Guia para redação de passos orientados a problemas práticos de produção e trabalho diário. Consulta: 2026-10-04.
