---
id: software.criacao_ia.tranche04.000359
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
fontes: ["https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html", "https://docs.godotengine.org/en/stable/engine_details/editor/creating_icons.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: [icons] e [dependencies] completam o .gdextension — com contrato de 16×16 px

## Em uma frase
Além de configuration e libraries, o arquivo tem a seção [icons] (SVG 16×16 com dois toggles de import) e a seção [dependencies] (caminhos das libs de terceiros a exportar com o jogo).

## Por que importa
A experiência do add-on no editor é parte do produto: nós com o ícone genérico de Node no dock dizem 'estoque' quando dizem 'sua extensão'; e esquecer [dependencies] é entregar um binário que abre na máquina de dev e cai na do cliente pela lib que faltou no export.

## Como funciona
Em [icons], o par nome-do-no = caminho do SVG; a doc exige SVG de 16×16 pixels com duas opções marcadas na importação: 'Editor > Scale with Editor Scale' e 'Editor > Convert Colors with Editor Theme', 'garante que o ícone se comporte o mais próximo possível dos ícones do editor'. Em [dependencies], declaram-se os caminhos das libs que a extensão requer — a seção existe 'para exportar as dependências quando exportar o executável do jogo'. Comente o porquê de cada linha — é a segunda metade da doc de manutenção do arquivo.

## Exemplo
O plugin GDExample publica 'GDExample = "res://icons/gd_example.svg"' e registra 'libonnxruntime.so' em dependencies; na release do cliente o executável exporta com as duas bibliotecas sem manual de instalação nativa.

## Limites e trade-offs
Ícone sem os dois toggles importados fica com tamanho/cores errados em tema escuro e editor em HiDPI — o contrato não é cosmético. A seção de ícones não define a categoria do nó na Scene dock (isso é ClassDB); e dependencies não resolve versões de SONAME/Loader Path — se a lib exige rpath, é build seu. O campo de ícone aceita um caminho por nome de classe.

## Como verificar
Abra a Scene dock e compare o ícone do seu nó com os nativos no tema escuro e no zoom 200%: o par de toggles é justamente o que garante o match. Exporte o projeto para uma máquina limpa sem as libs de sistema instaladas — o export com [dependencies] declaradas roda; sem, não. Um teste de fumaça automatizado confirma.

## Conexões
- [[gdextension-double-single-api-json]] — Godot 4: a extensão só carrega no build de motor com a mesma precisão de float.
- [[gdextension-vs-modules-custo-distribuicao]] — Godot 4: godot-cpp versus módulos C++ — uma decisão de distribuição.

## Fontes
- [Godot — The .gdextension file](https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html) — as seções Icons e Dependencies com o contrato do SVG e do export Consulta: 2026-10-04.
- [Godot — Editor icons](https://docs.godotengine.org/en/stable/engine_details/editor/creating_icons.html) — o guia de criação de ícones referenciado pela seção [icons] Consulta: 2026-10-04.
