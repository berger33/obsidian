---
id: software.criacao_ia.tranche05.000428
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

# Godot EditorImportPlugin: gravar em save_path e declarar arquivos gerados

## Em uma frase
O recurso principal deve ser gravado em `save_path` com a extensão declarada, e arquivos adicionais gerados em `res://` devem ser listados em `gen_files`.

## Por que importa
O editor usa o caminho de destino e a lista de arquivos dependentes para manter a importação e o rastreamento de dependências coerentes.

## Como funciona
Construa o destino como `save_path + "." + _get_save_extension()`, salve por `ResourceSaver` e inclua em `gen_files` o caminho completo de cada recurso adicional criado no filesystem do projeto. Para variante de feature tag, siga o formato e a lista `platform_variants` documentados.

## Exemplo
Um conversor grava o material em `save_path.material`, gera uma textura derivada em `res://generated/`, acrescenta esse caminho a `gen_files` e anota a tag da variante quando a saída é específica.

## Limites e trade-offs
`save_path` não deve ser substituído por um caminho arbitrário da máquina; não declare arquivo em `gen_files` se ele não foi realmente gerado.

## Como verificar
Reimporte a fonte, confira o recurso principal, confirme que dependências geradas aparecem no projeto e teste uma feature tag em exportação compatível.

## Conexões
- [[godot-editorimportplugin-validar-source-file-e-error]] — Godot EditorImportPlugin: validar source_file e propagar Error do import.
- [[godot-editorimportplugin-threaded-import-safety]] — Godot EditorImportPlugin: habilitar importação paralela só após provar thread safety.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Especifica caminho esperado do recurso, feature variants e registro de arquivos gerados. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Mostra salvamento do recurso importado e a relação entre arquivo fonte e artefato. Consulta: 2026-10-04.
