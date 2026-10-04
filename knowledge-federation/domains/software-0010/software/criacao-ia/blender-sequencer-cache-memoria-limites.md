---
id: software.criacao_ia.tranche04.000367
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
fontes: ["https://docs.blender.org/manual/en/latest/editors/preferences/system.html", "https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/cache.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender VSE: Memory Cache Limit vive nas Preferences, e o VSE lê dele

## Em uma frase
O orçamento do cache de quadros do Sequencer/Movie Clip Editor é definido em Preferences ‣ System ‣ Video Sequencer ‣ Memory Cache Limit (MB), com recomendação oficial de valores altos para performance ótima.

## Por que importa
O buffer default é conservador; numa máquina com RAM, o gargalo de scrubbing costuma ser o cache esvaziando cedo, não o disco. A página do System é explícita: 'For an optimal Clip editor and Sequencer performance, high values are recommended' — um toggle que muitos setups nunca tocaram, documentado como ajuste primário do editor de vídeo.

## Como funciona
Defina o limite em MB conforme a RAM do host (a doc não prescreve fração — a regra prática de estúdio é deixá-lo folgado para o resto da máquina). O mesmo bloco System traz o Proxy Setup global: Automatic (gera proxies para cada preview size ao adicionar strips de vídeo/imagem) ou Manual (setup feito a mão), a decisão que liga/desliga o pipeline da nota de BL_proxy. O lado por-projeto do cache (quais imagens entram, tipos) mora no painel Sequencer Cache Properties, referenciado pela própria página.

## Exemplo
Uma workstation de 64 GB com projeto de multicam 4K sobe o limite para 32768: o scrubbing passa a servir frames do cache e o pico de engasgo some — a medição é o tempo de seek nos 10 primeiros segundos após seek.

## Limites e trade-offs
O limite é global à instalação (preferences), não por projeto: dois editores na mesma máquina compartilham o orçamento e a configuração. Cache de memória não é pré-render: efeitos de strips pesados ainda custam por frame, o cache só amortiza repetição — para esses, o sequencer tem render cache próprio. Values altos demais em máquina apertada trocam engasgo por swap/OOM.

## Como verificar
Meça o scrubbing antes/depois de dobrar o limite num projeto longo (mesmo seek, mesma timeline) — é o número que sustenta a config. Confirme no painel Cache Properties do projeto que o conteúdo cachado cresce até o teto (o contador de cache do VSE mostra). Rode com Proxy Setup Automatic numa pasta só de leitura e observe a falha de geração que o modoManual evita.

## Conexões
- [[blender-proxy-quality-lossy-percentual]] — Blender VSE: Quality do proxy é compressão com perda em percentual direto — 100 é sem perda.
- [[blender-backend-vulkan-interface-52]] — Blender 5.2: o backend da interface é escolha (OpenGL × Vulkan) com custo de reinicialização.

## Fontes
- [Blender — Preferences: System](https://docs.blender.org/manual/en/latest/editors/preferences/system.html) — a seção Video Sequencer com Memory Cache Limit e Proxy Setup, na íntegra Consulta: 2026-10-04.
- [Blender — Sequencer Cache Properties](https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/cache.html) — página de propriedades de cache por projeto, referenciada pela página System Consulta: 2026-10-04.
