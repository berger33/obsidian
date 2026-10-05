---
id: software.criacao_ia.tranche05.000424
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

# Godot EditorImportPlugin: alinhar resource_type ao save_extension declarado

## Em uma frase
O importador declara o tipo do recurso com `_get_resource_type()` e a extensão de salvamento com `_get_save_extension()` para que o editor trate o resultado adequadamente.

## Por que importa
O tipo permite inserir o recurso em slots compatíveis, enquanto a extensão declara como o artefato será armazenado na área importada do projeto.

## Como funciona
Escolha o nome de classe do recurso que realmente será criado e a extensão de saída coerente com esse recurso; o guia usa `StandardMaterial3D` e `material` como exemplo de material.

## Exemplo
Um importador de texto para material retorna `StandardMaterial3D`, salva o objeto com extensão `material` e permite arrastá-lo do FileSystem para uma propriedade de material.

## Limites e trade-offs
O tutorial observa que a extensão não é rigidamente imposta pelo mecanismo e que uma extensão fonte pode ter vários tipos de saída, caso em que se criam importadores separados.

## Como verificar
Reimporte o arquivo de teste, confirme a classe do recurso no editor e tente atribuí-lo ao slot esperado; confira também a extensão gerada na área de importação.

## Conexões
- [[godot-editorimportplugin-extensoes-prioridade]] — Godot EditorImportPlugin: limitar extensões aceitas e declarar prioridade consciente.
- [[godot-editorimportplugin-opcoes-e-presets]] — Godot EditorImportPlugin: descrever opções de importação com defaults e presets.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Define tipo do recurso, extensão usada no diretório importado e caminho esperado de saída. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Explica o papel do tipo de recurso e exemplifica material e extensão de saída. Consulta: 2026-10-04.
