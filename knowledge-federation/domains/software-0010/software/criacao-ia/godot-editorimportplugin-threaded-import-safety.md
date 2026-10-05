---
id: software.criacao_ia.tranche05.000429
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

# Godot EditorImportPlugin: habilitar importação paralela só após provar thread safety

## Em uma frase
`_can_import_threaded()` informa se o importador pode rodar em paralelo; o padrão é falso e só deve ser alterado por uma implementação segura para threads.

## Por que importa
Importação concorrente pode reduzir espera no editor, mas compartilhamento de estado mutável ou API não thread-safe pode introduzir falhas intermitentes difíceis de reproduzir.

## Como funciona
Mantenha o comportamento padrão enquanto o importador depender de estado global, UI ou recursos não seguros. Sobrescreva retornando verdadeiro apenas após isolar estado por arquivo e confirmar segurança da leitura, conversão e gravação paralelas.

## Exemplo
Uma conversão pura de arquivos independentes passa a declarar capacidade threaded após testes concorrentes; um plugin que atualiza uma tabela compartilhada continua serial.

## Limites e trade-offs
O retorno autoriza paralelismo do importador, não garante ganho em toda máquina nem torna automaticamente thread-safe uma biblioteca externa chamada pelo plugin.

## Como verificar
Execute reimportação em lote repetidas vezes com arquivos diferentes e simultâneos, compare hashes de saída e monitore erros e corrupção antes de habilitar a opção.

## Conexões
- [[godot-editorimportplugin-save-path-gen-files-variants]] — Godot EditorImportPlugin: gravar em save_path e declarar arquivos gerados.
- [[godot-editorimportplugin-format-version-invalidacao]] — Godot EditorImportPlugin: incrementar format_version ao incompatibilizar recursos importados.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Define o significado, o padrão falso e o requisito de implementação thread-safe. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Demonstra o ciclo de importação executado pelo editor para recursos personalizados. Consulta: 2026-10-04.
