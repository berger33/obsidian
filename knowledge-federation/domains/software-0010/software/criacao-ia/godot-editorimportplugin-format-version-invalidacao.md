---
id: software.criacao_ia.tranche05.000430
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

# Godot EditorImportPlugin: incrementar format_version ao incompatibilizar recursos importados

## Em uma frase
`_get_format_version()` permite indicar a versão do formato produzido pelo importador; incremente-a quando mudanças forem incompatíveis com recursos já gerados.

## Por que importa
Sem um sinal de versão, uma alteração de serialização ou conversão pode deixar recursos antigos aceitos como se tivessem sido produzidos pelo contrato atual.

## Como funciona
Mantenha uma versão numérica vinculada ao formato de saída e atualize esse valor ao quebrar compatibilidade. A referência informa que o default é zero quando o método não é sobrescrito.

## Exemplo
Uma nova versão do importador altera a estrutura binária do recurso, incrementa o valor de formato e reimporta amostras antigas para confirmar que o pipeline produz o layout esperado.

## Limites e trade-offs
A versão não substitui migração nem verificação semântica do arquivo fonte; não a incremente por toda mudança cosmética que mantém o mesmo formato.

## Como verificar
Mantenha fixture de saída anterior, altere a versão em uma mudança incompatível e execute reimportação limpa para conferir que o editor regenera os recursos necessários.

## Conexões
- [[godot-editorimportplugin-threaded-import-safety]] — Godot EditorImportPlugin: habilitar importação paralela só após provar thread safety.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Define a finalidade de `_get_format_version()` e o valor padrão quando não sobrescrito. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Descreve o ciclo de criação e reimportação dos recursos personalizados. Consulta: 2026-10-04.
