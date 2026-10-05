---
id: software.criacao_ia.tranche05.000423
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

# Godot EditorImportPlugin: limitar extensões aceitas e declarar prioridade consciente

## Em uma frase
`_get_recognized_extensions()` associa formatos de arquivo ao importador, e `_get_priority()` influencia qual plugin é preferido quando mais de um reconhece a extensão.

## Por que importa
Extensões genéricas como `.json` ou `.txt` podem pertencer a dados comuns do jogo ou a vários importadores, tornando a seleção indiscriminada arriscada.

## Como funciona
Retorne apenas extensões realmente aceitas, valide o conteúdo do arquivo no importador e defina prioridade maior somente quando a preferência sobre outro plugin for intencional; o padrão documentado é `1.0`.

## Exemplo
Um conversor proprietário registra `.meshsrc` em vez de reivindicar todo `.json` e aumenta a prioridade apenas para o formato legado que deve substituir um importador alternativo.

## Limites e trade-offs
Prioridade não corrige dados inválidos nem elimina a possibilidade de seleção entre importadores. Extensões são associadas sem diferenciar maiúsculas e minúsculas na referência da classe.

## Como verificar
Importe exemplos válidos e malformados da extensão, teste um arquivo que dois plugins reconhecem e confirme qual opção aparece ou é preferida no editor.

## Conexões
- [[godot-editorimportplugin-identidade-e-nome-visivel]] — Godot EditorImportPlugin: manter importer_name estável e separar o rótulo visível.
- [[godot-editorimportplugin-tipo-e-extensao-de-saida]] — Godot EditorImportPlugin: alinhar resource_type ao save_extension declarado.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Documenta extensões reconhecidas, comparação case-insensitive e prioridade padrão. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Alerta para extensões comuns compartilhadas e arquivos que podem não ser importáveis. Consulta: 2026-10-04.
