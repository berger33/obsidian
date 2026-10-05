---
id: software.criacao_ia.tranche05.000425
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

# Godot EditorImportPlugin: descrever opções de importação com defaults e presets

## Em uma frase
`_get_import_options(path, preset_index)` fornece opções e valores padrão, enquanto os métodos de preset nomeiam conjuntos iniciais de configuração.

## Por que importa
Opções explícitas tornam a importação reprodutível e dão ao editor informação suficiente para exibir configurações que afetam a produção do recurso.

## Como funciona
Retorne um array de dicionários que inclua `name` e `default_value`; propriedades opcionais podem indicar hints, texto de hint e uso. Informe a quantidade de presets e associe cada índice a um nome.

## Exemplo
Um importador de textura oferece preset `Balanced` com opção `generate_mips` e preset `Preview` com valor padrão diferente para acelerar iterações locais.

## Limites e trade-offs
Os defaults não substituem a validação do conteúdo nem garantem que toda opção seja suportada pela plataforma de saída; mantenha o mesmo contrato entre índice, nome e valores.

## Como verificar
Abra o dock de importação em cada preset, confira valores iniciais e salve/importa de novo após alterar uma opção para confirmar que o importador recebe o valor esperado.

## Conexões
- [[godot-editorimportplugin-tipo-e-extensao-de-saida]] — Godot EditorImportPlugin: alinhar resource_type ao save_extension declarado.
- [[godot-editorimportplugin-visibilidade-de-opcoes]] — Godot EditorImportPlugin: ocultar opções dependentes sem perder seu contrato.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Lista as chaves requeridas e opcionais dos dicionários de opções e os métodos de preset. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Apresenta opções e presets como configuração controlável pelo usuário. Consulta: 2026-10-04.
