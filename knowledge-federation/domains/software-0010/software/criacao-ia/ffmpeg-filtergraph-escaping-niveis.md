---
id: software.criacao_ia.tranche03.000268
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://ffmpeg.org/ffmpeg-filters.html#Notes-on-filtergraph-escaping", "https://ffmpeg.org/ffmpeg-utils.html#Quoting-and-escaping"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg filtergraph: separar escaping do filtro e da shell

## Em uma frase
Uma string de filtro pode passar por mais de um parser, então escaping interno do filtergraph e quoting da shell são camadas distintas.

## Por que importa
Paths com dois pontos, apóstrofos, vírgulas ou colchetes podem ser interpretados como separadores de filtros. Escapar apenas para shell não garante que o parser de opções ou parser de filtergraph receba o caractere literal pretendido.

## Como funciona
Identifique a sintaxe do valor no filtro, a gramática de filtergraph e por fim a shell ou linguagem que monta o comando. Escape caracteres especiais na camada correta, considere lista de args sem shell em automação e mova graphs longos para arquivo quando suportado por opção apropriada como `-/filter:v` em versões compatíveis.

## Exemplo
Um `drawtext` com caminho contendo dois pontos é construído em string de filtro com quoting FFmpeg e depois passado como argumento único via subprocess sem shell. Um teste usa nome com apóstrofo, espaço e vírgula para verificar que nenhum caractere vira separador de filtro.

## Limites e trade-offs
A regra varia por contexto: filtros têm escaping próprio, shells POSIX e PowerShell diferem e uma wrapper de linguagem pode adicionar outra camada. Opções de arquivo para ler argumentos dependem de suporte na versão instalada.

## Como verificar
Use `ffmpeg-utils` e a seção filtergraph escaping para reproduzir a string em cada camada; imprima os argumentos finais do subprocess e teste paths adversariais de forma automatizada.

## Conexões
- [[ffmpeg-fps-filter-versus-output-r]] — FFmpeg: distinguir filtro fps de opção de output -r.
- [[ffmpeg-framesync-overlay-eof-policy]] — FFmpeg framesync: definir comportamento ao terminar uma entrada.

## Fontes
- [FFmpeg — Notes on filtergraph escaping](https://ffmpeg.org/ffmpeg-filters.html#Notes-on-filtergraph-escaping) — explica escaping em filtergraph e as camadas de parser Consulta: 2026-10-04.
- [FFmpeg — Utilities quoting and escaping](https://ffmpeg.org/ffmpeg-utils.html#Quoting-and-escaping) — define quoting, backslash escaping e segundo nível de escaping da shell Consulta: 2026-10-04.
