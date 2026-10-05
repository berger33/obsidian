---
id: software.criacao_ia.tranche05.000421
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html", "https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot EditorImportPlugin: registrar e remover a instância pelo EditorPlugin

## Em uma frase
Um importador personalizado passa a integrar o editor quando uma extensão chama `add_import_plugin` e deve ser removido ao desativar essa extensão.

## Por que importa
O ciclo explícito de registro evita importadores órfãos, duplicados ou ainda ativos depois de o plugin de editor ser desabilitado.

## Como funciona
No ciclo de vida do `EditorPlugin`, crie e guarde uma instância de `EditorImportPlugin` ao entrar na árvore, registre-a e chame `remove_import_plugin` na saída antes de limpar a referência.

## Exemplo
Um plugin materializa `MaterialImport.new()` em `_enter_tree()`, chama `add_import_plugin(importer)` e usa a mesma instância em `_exit_tree()` para removê-la.

## Limites e trade-offs
A classe é uma ferramenta de editor, não um importador de runtime; o recurso importado salvo é que será usado pelo projeto. Não crie outra instância na remoção.

## Como verificar
Ative e desative o plugin no editor, observe o importador disponível no dock e confirme que reativar não duplica a entrada nem gera erro de ciclo de vida.

## Conexões
- [[godot-editorimportplugin-identidade-e-nome-visivel]] — Godot EditorImportPlugin: manter importer_name estável e separar o rótulo visível.

## Fontes
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Mostra `add_import_plugin` em `_enter_tree` e remoção com a mesma referência em `_exit_tree`. Consulta: 2026-10-04.
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Define a classe como extensão da função de importação de recursos do editor. Consulta: 2026-10-04.
