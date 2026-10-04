---
id: software.criacao_ia.tranche04.000371
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/resume", "https://webaudio.github.io/web-audio-api/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Web Audio: o AudioContext nasce suspenso e só um gesto humano o acorda

## Em uma frase
Navegadores exigem interação do usuário para retomar um AudioContext: sem resume() chamado dentro de um gesto, nada toca — e o estado 'suspended' é a norma, não a exceção.

## Por que importa
A política de autoplay existe para impedir áudio não solicitado, e a Web Audio a respeita no nível do contexto. Times que descobrem isso em produção veem o áudio 'mudo' sem erro nenhum no console: os nós rodam o grafo, o clock avança... para o lugar nenhum. A arquitetura da resposta (fila de eventos até o gesto) precisa ser decidida no design, não no hotfix.

## Como funciona
Trate o estado do contexto como máquina de estados: 'suspended' → 'running' via resume() (promise), tipicamente disparado por um handler de click/keydown. O estado é lido em ctx.state; listeners emonstatechange ajudam a reagir quando o browser retoma sozinho (ex.: interação com outro elemento). Áudio de fundo com intenção clara pode oferecer um botão 'ativar som'; a API não oferece bypass da política — o caminho é desenhar a transição, não contorná-la.

## Exemplo
Um jogo web cria o contexto no 'pointerdown' do 'Play' (não no load da página), resolve a promise de resume() e só então scheduleia a música — o primeiro frame já sai com clock correto, sem o atraso clássico de 'um segundo mudo'.

## Limites e trade-offs
Chamar resume() fora de gesto é permitido e pode resolver para rejected — não há 'gesto emprestado' de eventos antigos em todas as implementações. Um contexto criado e nunca retomado consome alocação? Ele existe, mas sem render até correr — não confunda 'criado' com 'audível'. A política é por browser/plataforma (iOS historicamente mais estrita que desktop); teste as duas pontas.

## Como verificar
No device real, carregue sem interação e leia ctx.state: 'suspended' é o esperado antes do gesto, 'running' depois. Simule autoplay negado (recarregar a página e agendar som sem clique) e confirme o silêncio sem erro no console — o sinal do diagnóstico errado mais comum. Registre a transição com onstatechange num dev overlay.

## Conexões
- [[webaudio-fontes-oneshot-start-stop]] — Web Audio: nós de fonte são one-shot — start() e stop() cada um uma vez só.

## Fontes
- [MDN — AudioContext: resume()](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/resume) — documenta a retomada do contexto e a restrição de autoplay policy Consulta: 2026-10-04.
- [W3C — Web Audio API (spec)](https://webaudio.github.io/web-audio-api/) — define o modelo de estados do AudioContext Consulta: 2026-10-04.
