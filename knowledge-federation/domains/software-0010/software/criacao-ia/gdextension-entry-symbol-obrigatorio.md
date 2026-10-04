---
id: software.criacao_ia.tranche04.000352
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html", "https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/gdextension_cpp_example.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: entry_symbol é o contrato mínimo do arquivo .gdextension

## Em uma frase
A seção [configuration] do arquivo .gdextension declara entry_symbol — o nome da função que inicializa a extensão — sem o qual a extensão não funciona.

## Por que importa
O loader precisa de um ponto de entrada estável para iniciar a biblioteca após carregá-la; a doc crava que a função deve estar definida e que 'Adding this is necessary for the extension to work' com godot-cpp no arquivo register_types.cpp. Erro clássico de primeira extensão: a .dll carrega, nada acontece, e o problema são dois caracteres no nome da função.

## Como funciona
Com godot-cpp, o template de projeto gera a função de registro (por exemplo 'example_library_init') em register_types.cpp; o valor de entry_symbol deve ser exatamente esse nome. A tabela oficial da seção [configuration] lista os campos: entry_symbol (String), compatibility_minimum, compatibility_maximum, reloadable e android_aar_plugin. Mantenha o .gdextension dentro do projeto e referencie as libs por caminho relativo — a doc recomenda relativo porque 'permite que a extensão continue funcionando se for instalada em outra pasta'.

## Exemplo
O repositório de exemplo da doc usa 'entry_symbol = "gdexample_library_init"' no gdexample.gdextension espelhando a função em register_types.cpp; renomeie um sem o outro e o motor reporta falha de entrada, não um crash mudo.

## Limites e trade-offs
O nome é um símbolo C exportado — mangled C++ não resolve; os bindings cuidam do extern 'C', código cru precisa cuidar você mesmo. A função de entrada roda cedo, na carga: trabalho pesado ou dependências de cena ali são fonte de deadlock e ordem de inicialização quebrada — registre tipos, não simule. Cada binding tem sua convenção de nome de entrada.

## Como verificar
Corrompa de propósito o entry_symbol (um caractere a mais) e observe a mensagem de falha de carregamento no console do editor — é o contrato em ação. Rode o exemplo oficial da doc de ponta a ponta e compare o seu .gdextension campo a campo. Um teste de fumaça no CI que abre o projeto e verifica se o nó da extensão existe pega regressão de rename.

## Conexões
- [[gdextension-biblioteca-compartilhada-runtime]] — Godot 4: GDExtension é a ponte runtime para bibliotecas nativas.
- [[gdextension-alvo-baixo-compative-frente]] — Godot 4: mire a extensão na versão mais baixa que te atende, não na mais nova.

## Fontes
- [Godot — The .gdextension file](https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html) — tabela da seção [configuration] e a nota de necessidade do entry function Consulta: 2026-10-04.
- [Godot — GDExtension C++ example](https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/gdextension_cpp_example.html) — exemplo oficial onde o entry_symbol é definido e usado Consulta: 2026-10-04.
