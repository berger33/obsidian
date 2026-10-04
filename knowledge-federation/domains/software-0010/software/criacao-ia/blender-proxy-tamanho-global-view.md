---
id: software.criacao_ia.tranche04.000364
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
fontes: ["https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/proxy.html", "https://docs.blender.org/manual/en/latest/editors/video_sequencer/preview/sidebar.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender VSE: Proxy Render Size é um switch global que habilita todos os strips

## Em uma frase
Escolher Proxy Render Size na aba View da Preview ativa a resolução escolhida para todos os strips do projeto e dispara a geração dos arquivos de proxy — é um modo de exibição global, não um toggle por-clip.

## Por que importa
A expectativa natural ('vou ativar proxy só no clipe pesado') leva o editor a não entender por que toda a timeline de repente baixa de resolução. E a parte não documentada no susto: mudar o tamanho global reconfigura os demais, com geração em massa de proxies no primeiro play. Saber que o View tab é o interruptor mestre da doc oficial evita as duas surpresas.

## Como funciona
No Sequencer, Preview/Sequencer & Preview modes, sidebar > View > View Settings: 'Proxy Render Size' controla a resolução da preview (valores menores, pior detalhe, melhor performance) e 'Use Proxies' liga/desliga o uso como toggle separado (aba View do preview sidebar). O caminho rápido documentado é o View tab; a aba Proxy (ausente em modo Preview puro) expõe o setup por-strips — e em Preview mode o setup migra para o menu View ‣ Proxy ‣ Setup.

## Exemplo
Uma timeline de 4K multicam: o editor deixa o View global em 50% para corte fino e sobe para 100% (proxy 100% já codificado) só para conferir foco — os clipes não precisam de reconfiguração individual para isso.

## Limites e trade-offs
O tamanho é um preset (25/50/75/100% e afins da UI); se o arquivo do tamanho não existe, a preview cai no full-res e a performance engasga silenciosamente até a geração. 'Use Proxies' desligado mantém os arquivos mas exibe o original — estado que parece bug de cache. A configuração por-strip (Strip Proxy & Timecode) refina o que o global habilitou, não substitui o gate global.

## Como verificar
Numa timeline com um clip pesado, mude o View global e confirme que todos os strips respondem juntos — inclusive o leve, que ganha proxy 'por tabela'. Desligue 'Use Proxies' e observe o frame time voltar ao original: é o par de switches documentado. Registre os fps medidos em 25/50/100 na máquina do estúdio — é o número da decisão de tamanho.

## Conexões
- [[blender-what-you-see-is-not-what-you-save]] — Blender: o display view não é o arquivo salvo — o laço View as Render/Save as Render.
- [[blender-proxy-bl-pasta-e-arquivos-externos]] — Blender VSE: proxies vivem em BL_proxy junto da footage — e podem ser arquivos existentes.

## Fontes
- [Blender — Sequencer Sidebar: Proxy](https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/proxy.html) — descreve o atalho do View tab que habilita todos os strips e gera os arquivos Consulta: 2026-10-04.
- [Blender — Preview Sidebar](https://docs.blender.org/manual/en/latest/editors/video_sequencer/preview/sidebar.html) — define Proxy Render Size e Use Proxies nos View Settings da preview Consulta: 2026-10-04.
