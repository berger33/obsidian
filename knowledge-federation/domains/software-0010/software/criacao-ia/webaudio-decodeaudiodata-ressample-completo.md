---
id: software.criacao_ia.tranche04.000375
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/decodeAudioData", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: decodeAudioData ressampleia para o contexto e exige o dado completo

## Em uma frase
decodeAudioData transforma qualquer arquivo de áudio em AudioBuffer no sample rate do contexto — não o do arquivo — e não aceita streaming: só dados inteiros.

## Por que importa
Dois bugs de integração nascem de esperar comportamento de <audio>: (1) 'meu sample de 48k tocou rápido/lento' — o buffer veio em 44.1k porque o contexto é 44.1k; (2) feeds parciais (fetch progressivo) falham o decode porque o decodificador não trabalha em stream. Saber que o API é 'arquivo inteiro → buffer já no rate certo' define o carregador.

## Como funciona
Fluxo: fetch/arrayBuffer → ctx.decodeAudioData(wholeBuffer) → AudioBuffer (canais float linearizados, rate = sampleRate do contexto). O sample rate do contexto é escolhido na criação (AudioContext com options; em material/soa­pes, escolher rate fixo — ex.: 48000 — sincroniza com vídeo e evita re-amostragem por asset). A página cobre que o caminho primário é a promise (os callbacks legado existem, evite-os em código novo). Dados parciais: acumule até o fim do fetch; para latência zero, decodifique na carga, não no trigger.

## Exemplo
Um editor de vídeo web mantém o AudioContext em 48 kHz para bater com a timeline; todos os assets (44.1 de MP3, 32k de voice memo) chegam convertidos — o scrubbing não tem drift porque tudo já está no rate do relógio.

## Limites e trade-offs
A ressampleagem do decode é offline-quality (não é para playback time-stretched; playbackRate faz outra coisa). Codec suportado é o que o decoder do navegador tem (um WebM estranho pode falhar sem detalhe — a promessa é 'dados válidos de áudio', a validação é do navegador). AudioBuffer é imutável: 'editar' é novo buffer. O custo de decode de arquivos grandes no main thread vira tarefa de warm-up, não de interação.

## Como verificar
Meça sampleRate do AudioBuffer retornado vs. o do arquivo de origem (ffprobe) e confirme a igualdade com o contexto, não com o arquivo. Teste o caminho de falha: um JSON mandado para decodeAudioData rejeita a promise — e o handler deve existir. Rode o carregador com fetch chunked acumulado vs. por-chunk e confirme que o segundo falha — a restrição documentada.

## Conexões
- [[webaudio-exp-ramp-zero-proibido]] — Web Audio: exponentialRampToValueAtTime não passa por zero — nem começando nem terminando nele.
- [[webaudio-audioworklet-modulos-processador]] — Web Audio: AudioWorklet é módulo separado com o seu próprio global scope.

## Fontes
- [MDN — BaseAudioContext: decodeAudioData()](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/decodeAudioData) — documenta o ressample para o rate do contexto e a recusa de dados incompletos Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — a definição de AudioBuffer e do papel do decode no grafo Consulta: 2026-10-04.
