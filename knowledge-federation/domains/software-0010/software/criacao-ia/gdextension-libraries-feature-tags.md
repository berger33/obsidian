---
id: software.criacao_ia.tranche04.000356
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
fontes: ["https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html", "https://docs.godotengine.org/en/stable/tutorials/export/feature_tags.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: a seção [libraries] é um filtro por feature flags, não uma lista de caminhos

## Em uma frase
Cada linha de [libraries] combina flags (sistema × build × arquitetura) a um caminho de binário; todas as flags da linha devem casar com as flags ativas do motor ou da export para aquela entrada valer.

## Por que importa
Uma extensão multiplataforma mantém um mapa de dezenas de binários — e o motor decide qual carregar por matching, não por extensão de arquivo. Entender o modelo de linhas 'macos.debug', 'linux.release.arm64' como conjunção de flags evita o clássico 'funciona no editor, some no export de Android'.

## Como funciona
As listas oficiais de flags: sistemas windows, macos, linux, bsd, linuxbsd, android, ios, web; build debug, release, editor (builds de editor sempre têm debug features); arquitetura double, single, x86_64, arm64, rv64, riscv, wasm32. Toda flag da linha precisa bater com as feature flags do Godot ou das suas flags de export customizadas; 'every feature flag must match'. Caminhos relativos são recomendados pela doc; comentários começam com ';', inclusive inline após a linha. O conjunto completo (incluindo as custom) está na página de feature tags.

## Exemplo
O template canônico da doc cobre 'linux.debug.arm64', 'linux.release.rv64', 'windows.*.x86_32'... — um espelho honesto dos presets que o godot-cpp compila, pronto para cortar o que seu produto não exporta.

## Limites e trade-offs
Flag errada é linha morta, e o motor avisa pouco: a falha aparece como 'a lib não carregou' na plataforma afetada. Flags de export customizadas (por exemplo, presets com tags próprias) ampliam a matriz de teste por produto. A lista da página é 'algumas das opções' — a página de feature tags é a fonte completa; não invente flag nova sem checar.

## Como verificar
Teste de matriz: exporte um debug e um release numa plataforma e confirme no log qual linha casou (o caminho carregado é reportado). Rode com uma linha removida e registre a mensagem de ausência — sua equipe precisa saber lê-la. Um script que cruza os binários existentes no build com as linhas do .gdextension pega desalinhamento antes do release.

## Conexões
- [[gdextension-reloadable-dev-debug]] — Godot 4: reloadable recarrega a extensão — e é ferramenta de desenvolvimento, não de produção.
- [[gdextension-ordem-especifica-antes]] — Godot 4: no .gdextension, a linha mais específica precisa vir antes — o matching é sequencial.

## Fontes
- [Godot — The .gdextension file](https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html) — a seção Libraries com as tabelas de flags e as regras de matching Consulta: 2026-10-04.
- [Godot — Feature tags](https://docs.godotengine.org/en/stable/tutorials/export/feature_tags.html) — a fonte completa das flags de plataforma/export referenciada pela página Consulta: 2026-10-04.
