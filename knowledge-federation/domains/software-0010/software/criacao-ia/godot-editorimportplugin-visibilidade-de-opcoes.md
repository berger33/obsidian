---
id: software.criacao_ia.tranche05.000426
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
fontes: ["https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html", "https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot EditorImportPlugin: ocultar opções dependentes sem perder seu contrato

## Em uma frase
`_get_option_visibility()` decide se uma opção aparece no dock e pode esconder um campo dependente do valor de outro campo.

## Por que importa
Exibir configurações irrelevantes para o modo selecionado confunde usuários e incentiva combinações que o importador não deveria aplicar.

## Como funciona
Inspecione `option_name` e o dicionário `options`, devolvendo falso apenas quando a opção não se aplica; a implementação padrão documentada deixa todas visíveis.

## Exemplo
Um importador mostra `lossy_quality` somente quando `compress/mode` seleciona Lossy e mantém o campo visível nos demais casos se o valor puder ser reutilizado.

## Limites e trade-offs
Visibilidade é uma regra de apresentação, não validação de entrada; rejeite ou normalize valores incompatíveis também no callback de importação.

## Como verificar
Alterne a opção controladora no dock, confira que o campo dependente muda de visibilidade e teste a importação direta com combinações incompatíveis para confirmar a validação.

## Conexões
- [[godot-editorimportplugin-opcoes-e-presets]] — Godot EditorImportPlugin: descrever opções de importação com defaults e presets.
- [[godot-editorimportplugin-validar-source-file-e-error]] — Godot EditorImportPlugin: validar source_file e propagar Error do import.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Define `_get_option_visibility`, o comportamento padrão e um exemplo de opção dependente. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Contextualiza opções de importação expostas no dock do editor. Consulta: 2026-10-04.
