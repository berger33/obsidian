---
id: software.criacao_ia.tranche04.000365
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
fontes: ["https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/proxy.html", "https://docs.blender.org/manual/en/latest/editors/preferences/system.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender VSE: proxies vivem em BL_proxy junto da footage — e podem ser arquivos existentes

## Em uma frase
O destino default dos proxies gerados é <caminho da footage>/BL_proxy/<nome do clipe>/, configurável por Custom Directory, com Custom File apontando para proxies pré-existentes.

## Por que importa
Esse layout define as decisões de infraestrutura do setup: o volume da mídia vira volume dos proxies (espaço, backup, permissões); o time que edita em rede lê BL_proxy do mesmo share; e a pipeline externa (que gera proxies próprios no render farm) só entra no VSE via Custom File — sem conhecê-lo, o editor duplica codificação que já existia.

## Como funciona
Em Strip Proxy & Timecode (aba Proxy do sidebar): 'Custom Directory' substitui a pasta padrão dos selecionados, 'Custom File' usa um proxy que já existe — a doc também cobre 'Set Selected Strip Proxies', que abre o pop-up de resoluções com escolha de sobrescrever existentes. Resolutions permite múltiplos tamanhos por clipe; a codificação roda em background e o progresso é a janela de process. Regra operacional: mantenha ou tudo-default ou tudo-custom; misturar destinos por clipe é o caminho do 'sumiu o proxy no outro host'.

## Exemplo
Um setup com NVMe local para edição: Custom Directory → /mnt/nvme/BL_proxy compartilhado com o farm; no fim, um script de limpeza trata um destino só em vez do jardim de BL_proxy espalhados por 20 shares de footage.

## Limites e trade-offs
Custom Directory é por-estrip-config: não há 'preferência global' no VSE para isso além do próprio default. Proxies externos (Custom File) precisam manter o nome/formato que o strip espera — a doc não abstrai seu naming scheme. Mover footage sem mover BL_proxy quebra o vínculo do default silenciosamente. Proxy com qualidade 0% em codec pesado decodifica mais devagar que o original leve — a escolha de formato tem duas pernas.

## Como verificar
Rode um rebuild num clipe e confirme a criação da pasta BL_proxy esperada; mude Custom Directory, rebuild, e valide o novo destino. Teste o caminho Custom File com um proxy externo e confira que o strip o usa sem regenerar (sem progresso de codificação ao trocar o View). Documente o layout resultante num README do projeto — é a convenção que sobrevive à pessoa.

## Conexões
- [[blender-proxy-tamanho-global-view]] — Blender VSE: Proxy Render Size é um switch global que habilita todos os strips.
- [[blender-proxy-quality-lossy-percentual]] — Blender VSE: Quality do proxy é compressão com perda em percentual direto — 100 é sem perda.

## Fontes
- [Blender — Sequencer Sidebar: Proxy](https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/proxy.html) — define BL_proxy default, Custom Directory/File e o fluxo Set Selected Strip Proxies Consulta: 2026-10-04.
- [Blender — Preferences: System (Video Sequencer)](https://docs.blender.org/manual/en/latest/editors/preferences/system.html) — o Proxy Setup global (Automatic/Manual) que decide quando essa máquina gera os arquivos Consulta: 2026-10-04.
