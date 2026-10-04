---
id: software.criacao_ia.tranche04.000372
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/AudioScheduledSourceNode/start", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: nós de fonte são one-shot — start() e stop() cada um uma vez só

## Em uma frase
Um AudioBufferSourceNode (ou Oscillator) aceita um único start() e um único stop(); recomeçar o mesmo objeto lança InvalidStateError — a unidade reutilizável é o buffer, não o nó.

## Por que importa
A API é declarativa sobre a timeline: agendar 'esse trecho, naquele instante' e descartar. Quem trata o nó como 'objeto player' com play/pause escreve o caminho de exceção no segundo play. O padrão — criar um nó novo por disparo a partir do mesmo buffer — é o que torna o scheduling barato e determinístico.

## Como funciona
Para cada som: crie o source node, conecte, atribua buffer/params, e agende start(when) com o tempo do contexto (ctx.currentTime como base). Para encerramentos precisos, stop(when) agendado no mesmo futuro. 'Pause' não existe: é stop + lembrar o offset e reiniciar com start(when, offset). Nós de fonte descartáveis significam GC após o fim — não desconectá-los não vaza, mas segurá-los em coleções, sim.

## Exemplo
Um drum pad: um AudioBuffer por sample no carregamento; cada hit cria 'const s = ctx.createBufferSource(); s.buffer = buf; s.connect(bus); s.start(0)' — 32 pads simultâneos sem pool, sem estado, sem exceção.

## Limites e trade-offs
O erro 'cannot call start more than once' é a regra, não um warning configurável; wrappers que 'reiniciam' fontes escondem o nó novo — escolha o padrão explícito. start() com mesmo 'when' duas vezes em nós diferentes é permitido, e a ordem espectral dos disparos depende do clock, não da ordem de chamada. Oscillator contínuo sem stop() vira fonte de CPU infinita — stop agendado é higiene.

## Como verificar
Chame start() duas vezes no mesmo nó num teste: a exceção é o contrato. Implemente o pad com pool de nós reutilizados e com nós fresh, e o segundo deve vencer em clareza (e empatar ou ganhar em perf). Um teste Playwright que toca 50 disparos e afirma que nenhum console error apareceu cobre a regressão.

## Conexões
- [[webaudio-contexto-suspenso-gesto]] — Web Audio: o AudioContext nasce suspenso e só um gesto humano o acorda.
- [[webaudio-settargetattime-constante-tempo]] — Web Audio: setTargetAtTime é o easing exponencial — a constante define 63%, não o fim.

## Fontes
- [MDN — AudioScheduledSourceNode: start()](https://developer.mozilla.org/en-US/docs/Web/API/AudioScheduledSourceNode/start) — documenta o erro por start duplicado e o parâmetro de agendamento Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — define o ciclo de vida one-shot dos audio source nodes Consulta: 2026-10-04.
