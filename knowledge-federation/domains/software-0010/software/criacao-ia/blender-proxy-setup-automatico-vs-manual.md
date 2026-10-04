---
id: software.criacao_ia.tranche04.000370
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
fontes: ["https://docs.blender.org/manual/en/latest/editors/preferences/system.html", "https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/proxy.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender VSE: Proxy Setup Automatic gera sozinho, Manual delega à farm — a decisão é de pipeline

## Em uma frase
A preference Video Sequencer ‣ Proxy Setup decide o comportamento raiz: Automatic constrói proxies de cada strip de vídeo/imagem adicionado em cada preview size; Manual deixa o setup para o operador (ou para a sua pipeline externa).

## Por que importa
Em produção pequena, Automatic é mão-na-roda: o proxy existe antes do primeiro corte. Em ingest de 20h de material por dia, ele é uma armadilha — a geração local compete com o próprio decode, no disco onde a footage mora. A doc define os dois modos literalmente, e a escolha pertence ao pipeline de ingest, não à preferência de última pessoa que mexeu.

## Como funciona
Automatic: ao adicionar um strip, Blender programa a geração para os tamanhos ativos; o painel do Proxy Settings (Resolutions, Quality, Overwrite) define o que é gerado. Manual: o operador ativa via 'Set Selected Strip Proxies' (pop-up de resoluções com overwrite) ou 'Rebuild Proxy' do menu Strip nos clipes escolhidos — dois cliques por seleção, zero custo no ingest. O ponto cego de ambos: o View tab global (Proxy Render Size) ainda habilita a exibição — setup é sobre quem gera, display é sobre quem usa; documente a dupla nos SOPs do time.

## Exemplo
O ingest do estúdio roda Manual com um job no farm produzindo proxies padronizados no BL_proxy custom; a preference local nunca muda. O editor independente roda Automatic com 25/50% só — o default da estação.

## Limites e trade-offs
Automatic + pasta de footage read-only (mount de arquivo só-escritura) é falha de geração silenciosa — o primeiro sintoma é proxy 'inexistente' no View. Proxies gerados pelo Blender priorizam decode rápido de edição, não fidelidade de cor — o grade final continua lendo o original. A preference é global à instalação (não por projeto): times com ingest local E farm precisam do mesmo valor e da mesma resolução-alvo, senão os modos se sobrepõem e duplicam arquivos.

## Como verificar
Num projeto limpo, adicione um clipe em cada modo e observe a fila de jobs de codificação (Automatic) vs. o silêncio (Manual) — é a diferença do painel em 10 segundos. Rode Automatic contra share somente-leitura e registre a falha para o SOP. No modo farm, confirme que os proxies externos aparecem como 'existing' e que o overwrite está desligado por padrão.

## Conexões
- [[blender-limites-de-memoria-undo-shaders-stack]] — Blender 5.2: os limites de memória do System — undo, shaders, geometry nodes — e seus efeitos colaterais.

## Fontes
- [Blender — Preferences: System](https://docs.blender.org/manual/en/latest/editors/preferences/system.html) — a definição dos dois modos na seção Video Sequencer, na íntegra Consulta: 2026-10-04.
- [Blender — Sequencer Sidebar: Proxy](https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/proxy.html) — o caminho de ativação por-clip do modo Manual e o pop-up de geração Consulta: 2026-10-04.
