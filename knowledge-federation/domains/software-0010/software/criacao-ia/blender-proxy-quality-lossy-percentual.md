---
id: software.criacao_ia.tranche04.000366
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

# Blender VSE: Quality do proxy é compressão com perda em percentual direto — 100 é sem perda

## Em uma frase
No painel Strip Proxy & Timecode, Quality controla o nível de compressão lossy aplicada à imagem do proxy: 0% é compressão máxima (menor arquivo, mais artefato), 100% é 'no compression'.

## Por que importa
O engano frequente é ler o percentual como 'qualidade final' na cabeça de export — aqui o eixo é a perda: 'Lossy compression reduces file size by discarding some image data'. Em projetos longos, a escolha de Quality é um cálculo explícito: espaço de disco em BL_proxy, velocidade de decode, e fidelidade da decisão de corte/color — proxy agressivo esconde banding que depois assombra a entrega.

## Como funciona
Combine Quality com a resolução: para edição de corte (não de look), resolução menor costuma comprar mais que compressão agressiva; para proxies 'de verdade' (pré-render para cor), 100% com resolução média é o meio-termo. A doc define as múltiplas Resolutions selecionáveis por clipe — gere só os tamanhos usados no View global, porque cada resolução extra tem seu custo de codificação e disco. A qualidade é um parâmetro da geração (Rebuild), não do playback: mudar exige regenerar.

## Exemplo
Um documentário 4K com 30h de material: 25/50% a 90% de quality ocupam menos que o volume da footage, e a revisão de corte não julga gradiente — a aprovação de look volta ao original no grade final.

## Limites e trade-offs
Artefato de compressão em proxy pode ser lido como 'problema do master' na revisão de cor se a pessoa não sabe que está em proxy — comunicação de pipeline, não bug. O codec/formato interno da geração do VSE não é configurável finamente pela UI documentada (resoluções+quality); pipelines que exigem ProRes para cor geram proxies externos e os plugam via Custom File. Banding em proxy é irreversível ao subir o View (o arquivo é o que é).

## Como verificar
Gere o mesmo clipe em 0/50/100% e compare tamanho do arquivo e decode do frame no player — a curva custo/fidelidade fica visível. Faça uma revisão de cor dupla (proxy vs. original) num quadro extremo: os problemas que só existem no proxy definem seu floor de Quality. Rode o rebuild pós-mudança para confirmar que a geração é quem lê o parâmetro.

## Conexões
- [[blender-proxy-bl-pasta-e-arquivos-externos]] — Blender VSE: proxies vivem em BL_proxy junto da footage — e podem ser arquivos existentes.
- [[blender-sequencer-cache-memoria-limites]] — Blender VSE: Memory Cache Limit vive nas Preferences, e o VSE lê dele.

## Fontes
- [Blender — Sequencer Sidebar: Proxy](https://docs.blender.org/manual/en/latest/editors/video_sequencer/sequencer/sidebar/proxy.html) — a definição literal de Quality: 0% compressão máxima, 100% sem compressão, perda de detalhe Consulta: 2026-10-04.
- [Blender — Preview Sidebar](https://docs.blender.org/manual/en/latest/editors/video_sequencer/preview/sidebar.html) — o consumo dos proxies no preview (Proxy Render Size/Use Proxies) que o Quality serve Consulta: 2026-10-04.
