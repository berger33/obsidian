---
id: software.criacao_ia.tranche04.000363
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
fontes: ["https://docs.blender.org/manual/en/4.0/render/color_management.html", "https://docs.blender.org/manual/en/latest/render/color_management/displays_views.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender: o display view não é o arquivo salvo — o laço View as Render/Save as Render

## Em uma frase
A janela de render mostra o resultado no View do display (ex.: AgX); o arquivo salvo usa o espaço de arquivo configurado — e os toggles 'View as Render'/'Save as Render' são o mecanismo de fechar essa lacuna conscientemente.

## Por que importa
O bug clássico do compositor: o quadro 'estourado e sem cor' no arquivo quando a preview estava linda, ou vice-versa — porque o arquivo foi salvo com o transform do display embutido e depois re-gradeado no consumo. Times que gravam EXR intermediário precisam saber de que lado a curva mora.

## Como funciona
Para o caso intermediário (render → compositor → entrega), mantenha o arquivo em espaço de trabalho linear e deixe o view transform só para a exibição. A doc (seção Color Management do manual 4.x) registra os comandos de render para o comportamento do display no arquivo — 'View as Render' faz o resultado do render carregar a aparência do view escolhido, 'Save as Render' aplica isso ao salvar — usando-os, a decisão fica explícita no pipeline em vez de implícita no driver da preview. A escolha documentada do espaço do arquivo (ex.: Linear vs Filmic para EXR) é o outro par do toggle.

## Exemplo
Um fluxo de FX grava EXR multi-camadas em raw (sem view), a composição final aplica AgX uma única vez na saída; o compositor que receber JPEG 'já com AgX' produziria o duplo rolloff clássico — evitado porque o view mora só na entrega.

## Limites e trade-offs
Comportamento exato dos toggles e nomes de menu variam entre versões do manual (a referência aqui é a seção homóloga da série 4.x/5.x); valide na sua build antes de codificar um padrão de estúdio. 'View as Render' em material preview é conveniência de look, não metadado de pipeline. Para entrega vídeo (codecs de 8 bits), o view precisa estar no arquivo — e é a inversão do caso EXR, não contradição.

## Como verificar
Salve o mesmo quadro com e sem 'Save as Render', amostrando um highlight no arquivo: um tem o shoulder, o outro é linear — a prova de onde a curva entrou. Compare a janela de render com o output real na mesma composição para pegar divergências. Rode o pipeline completo numa imagem de teste com rampa conhecida.

## Conexões
- [[blender-non-color-dados-nunca-convertidos]] — Blender: máscaras, normal maps e LUTs são Non-Color — converter dado é corromper sinal.
- [[blender-proxy-tamanho-global-view]] — Blender VSE: Proxy Render Size é um switch global que habilita todos os strips.

## Fontes
- [Blender — Color Management (4.0)](https://docs.blender.org/manual/en/4.0/render/color_management.html) — página da série 4.x que registra View as Render/Save as Render no fluxo de render Consulta: 2026-10-04.
- [Blender — Displays & Views (atual)](https://docs.blender.org/manual/en/latest/render/color_management/displays_views.html) — a separação display-view vs arquivo que o toggle atravessa Consulta: 2026-10-04.
