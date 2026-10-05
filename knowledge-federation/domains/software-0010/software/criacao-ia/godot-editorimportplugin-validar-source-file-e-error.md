---
id: software.criacao_ia.tranche05.000427
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

# Godot EditorImportPlugin: validar source_file e propagar Error do import

## Em uma frase
`_import()` recebe caminho fonte, opções e informações de variantes, e deve retornar um código `Error` apropriado ao resultado do trabalho.

## Por que importa
Importação é uma fronteira de dados: arquivos podem estar ausentes ou malformados, e falhar sem retorno claro deixa a interface sem diagnóstico confiável.

## Como funciona
Abra e valide o arquivo antes de construir o recurso, consulte as opções recebidas e retorne `OK` apenas quando a importação for bem-sucedida; em erro, devolva um código de falha em vez de salvar um recurso parcial como sucesso.

## Exemplo
Um importador CSV verifica que a abertura não retornou handle nulo, valida o número de colunas e só então cria o recurso; entrada inválida produz erro observável no editor.

## Limites e trade-offs
A API não interpreta automaticamente o formato privado do arquivo; o plugin é responsável por validação e mensagens úteis, sem supor que extensão prova conteúdo correto.

## Como verificar
Teste arquivo válido, inexistente, vazio e com estrutura corrompida; confirme retorno de erro e ausência de recurso parcial tratado como importação aprovada.

## Conexões
- [[godot-editorimportplugin-visibilidade-de-opcoes]] — Godot EditorImportPlugin: ocultar opções dependentes sem perder seu contrato.
- [[godot-editorimportplugin-save-path-gen-files-variants]] — Godot EditorImportPlugin: gravar em save_path e declarar arquivos gerados.

## Fontes
- [Godot — EditorImportPlugin](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) — Define os argumentos de `_import`, o retorno `Error` e o exemplo de falha de abertura. Consulta: 2026-10-04.
- [Godot — Import plugins](https://docs.godotengine.org/en/stable/tutorials/plugins/editor/import_plugins.html) — Recomenda validar dados e não presumir que arquivos de extensões genéricas estejam bem formados. Consulta: 2026-10-04.
