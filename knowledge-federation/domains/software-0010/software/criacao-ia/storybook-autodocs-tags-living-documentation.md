---
id: software.criacao_ia.tranche05.000469
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://storybook.js.org/docs/writing-docs/autodocs", "https://storybook.js.org/docs/writing-stories/args"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Storybook: habilitar Autodocs por tag e estender a documentação com MDX

## Em uma frase
Autodocs usa metadados de histórias para gerar documentação de componentes quando um arquivo CSF inclui a tag `autodocs`.

## Por que importa
Ligar docs a stories mantém exemplos renderizáveis perto das props e reduz o custo de reconstruir tabela de controles manualmente.

## Como funciona
Adicione `tags: ['autodocs']` globalmente no preview ou no meta do componente; complemente a página gerada com MDX e Doc Blocks quando precisar explicar contexto não inferível.

## Exemplo
Uma biblioteca ativa autodocs no preview e adiciona MDX com decisões de uso, mantendo stories reais como exemplos interativos e controles como referência de args.

## Limites e trade-offs
Autodocs infere metadata conhecida, mas não substitui orientação de uso, acessibilidade ou trade-offs de produto que não estão nas stories.

## Como verificar
Confirme uma página gerada por componente marcado, remova a tag de uma story que não deve aparecer e revise que conteúdo inferido corresponde à API pública.

## Conexões
- [[storybook-visual-tests-baselines-chromatic]] — Storybook: detectar regressões de pixels com visual tests e baselines revisados.
- [[storybook-a11y-axe-auditoria-manual]] — Storybook a11y: combinar varredura axe com verificação manual de acessibilidade.

## Fontes
- [Storybook — Autodocs](https://storybook.js.org/docs/writing-docs/autodocs) — Define a tag `autodocs`, geração automática e extensão da página com MDX. Consulta: 2026-10-04.
- [Storybook — Args](https://storybook.js.org/docs/writing-stories/args) — Explica metadados de args usados para controles e documentação de componente. Consulta: 2026-10-04.
