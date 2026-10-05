---
id: software.criacao_ia.tranche05.000422
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

# Godot EditorImportPlugin: manter importer_name estável e separar o rótulo visível

## Em uma frase
`_get_importer_name()` identifica o importador de forma única, enquanto `_get_visible_name()` fornece o texto exibido ao usuário no dock de importação.

## Por que importa
Mudar um identificador interno por causa de uma revisão de texto pode confundir reimportações; manter os papéis separados deixa a interface evoluir sem alterar a identidade do plugin.

## Como funciona
Escolha um nome único e estável para `_get_importer_name()` e um rótulo descritivo para `_get_visible_name()`. A documentação recomenda que o rótulo complete a expressão “Import as”, como “Special Mesh”.

## Exemplo
O código mantém `com.example.mesh_importer` como importer name persistente e mostra `Special Mesh` como opção amigável no painel do editor.

## Limites e trade-offs
A documentação exige unicidade do identificador, mas não define uma estratégia universal de migração para nomes já gravados em metadados antigos.

## Como verificar
Reimporte um arquivo com o mesmo importador, inspecione o rótulo no dock e teste a configuração em outro clone do projeto para detectar colisão de identificadores.

## Conexões
- [[godot-editorimportplugin-registro-no-editorplugin]] — Godot EditorImportPlugin: registrar e remover a instância pelo EditorPlugin.
- [[godot-editorimportplugin-extensoes-prioridade]] — Godot EditorImportPlugin: limitar extensões aceitas e declarar prioridade consciente.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Define o nome único do importador e o rótulo visível na interface. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Explica como o identificador permite selecionar o importador correto ao reimportar. Consulta: 2026-10-04.
