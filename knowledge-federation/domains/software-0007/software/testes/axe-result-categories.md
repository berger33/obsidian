---
id: software.testes.tranche12.000644
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

# axe-core: distinguir violations, passes, incomplete e inapplicable

## Em uma frase
O objeto de resultados separa regras que falharam, passaram, exigem revisão incompleta ou não se aplicam à árvore examinada.

## Por que importa
Manter essas categorias distintas evita que a equipe trate todo item retornado como defeito confirmado ou descarte uma checagem que não pôde concluir.

## Como funciona
Leia cada coleção com seu significado, associe violações às regras e alvos e não converta ausência de violações em afirmação de cobertura total.

## Exemplo
Uma execução pode conter uma violação de contraste, passes de outras regras e checagens incompletas que precisam ser avaliadas por uma pessoa.

## Limites e trade-offs
O resultado depende das regras, configuração e DOM presentes; duas execuções com escopos diferentes não são diretamente comparáveis apenas pelo total.

## Como verificar
Registre counts por categoria junto ao escopo e revise os itens incompletos antes de fechar o relatório.

## Conexões
- [[axe-runonly-tags-rules]] — Veja também: axe-core: selecionar regras com `runOnly`.
- [[axe-incomplete-manual-review]] — Veja também: axe-core: revisar resultados marcados como incomplete.

## Fontes
- [axe-core — JavaScript Accessibility API](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/API.md) — axe.run, objeto de resultados, tags, conteúdo renderizado e iframes; consultado em 2026-10-02.
- [axe-core — Testing Context](https://raw.githubusercontent.com/dequelabs/axe-core/develop/doc/context.md) — include/exclude, seletores DOM, iframes e shadow DOM; consultado em 2026-10-02.
