---
id: software.criacao_ia.tranche04.000373
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/AudioParam/setTargetAtTime", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: setTargetAtTime é o easing exponencial — a constante define 63%, não o fim

## Em uma frase
setTargetAtTime alvo suaviza o parâmetro em curva exponencial: após uma timeConstant ele percorreu 63,2% da distância, após 3 constantes ~95% — e nunca atinge o alvo matematicamente.

## Por que importa
É o setter certo para 'chegar perto sem estourar' (envelope de release sem clique, ganho de fader que nunca trisca em zero com rampa linear) e o mais mal-entendido da API: quem espera 'atingir o target em T segundos' configura T e vê o parâmetro parar em 95%, e quem o usa para mute total deixa um restinho de sinal para sempre.

## Como funciona
A curva é exponencial com constante τ; a relação prática documentada pela própria página: se você quer que o parâmetro 'chegue' (para todos os efeitos práticos) em D segundos, use τ = D/3 (3τ = 95%). O startTime é em tempo de contexto (ctx.currentTime para 'agora'). Para precisão absoluta de fim (gain zero, freq exata), encadeie uma setValueAtTime depois do alvo aproximado, ou troque de setter — a rampa exponencial pura não termina.

## Exemplo
Um ducking de música sob narração: gain.setTargetAtTime(0.15, ctx.currentTime, 0.1) chega a ~15% do caminho em 0,3 s e assenta suavemente; a volta usa outra setTarget com τ maior — o 'feeling' de radio ao vivo mora nessas duas constantes.

## Limites e trade-offs
O target nunca é atingido de fato — para zero exato, o caminho é outro setter. timeConstant ≤ 0 e startTime negativo são erros de tempo de execução de tipo próprio (a página MDN lista as exceções por parâmetro). E a interação com automações ativas substitui a fila: agendar setTarget em cima de um ramp em andamento é decisão explícita, não composição.

## Como verificar
Renderize um buffer com OfflineAudioContext amostrando o valor do parâmetro em 1τ, 2τ, 3τ, 5τ e confira 63,2/86/95/99+% — o teste numérico da curva num caso sintético. Tente o 'fade a zero' com setTarget puro e observe o resíduo audível: é a lição. Um teste de regressão compara a τ escolhida com a duração percebida do fade na mix.

## Conexões
- [[webaudio-fontes-oneshot-start-stop]] — Web Audio: nós de fonte são one-shot — start() e stop() cada um uma vez só.
- [[webaudio-exp-ramp-zero-proibido]] — Web Audio: exponentialRampToValueAtTime não passa por zero — nem começando nem terminando nele.

## Fontes
- [MDN — AudioParam: setTargetAtTime()](https://developer.mozilla.org/en-US/docs/Web/API/AudioParam/setTargetAtTime) — define a exponencial, o 63,2% por τ, e a relação com a rampa para alvo exato Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — a fórmula normativa das automation curves Consulta: 2026-10-04.
