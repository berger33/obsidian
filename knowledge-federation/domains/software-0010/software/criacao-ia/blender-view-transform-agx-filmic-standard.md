---
id: software.criacao_ia.tranche04.000361
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
fontes: ["https://docs.blender.org/manual/en/latest/render/color_management/displays_views.html", "https://docs.blender.org/manual/en/latest/render/color_management/color_spaces.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender: o View Transform (AgX, Filmic, Standard) é decisão de destino, não de look

## Em uma frase
O View Transform converte a cena linear para o espaço do display, e cada um (AgX, Filmic, Standard, Linear) define um teto de stops e um comportamento de saturação nas altas luzes — antes de qualquer look.

## Por que importa
Times que tratam o view transform como 'filtro' descobrem tarde que a cena foi iluminada para um rolloff que não existe no escolhido: Standard estoura highlights em branco puro, enquanto AgX/Filmic comprimem a faixa alta trocando estouro por desaturação progressiva. A escolha determina quanta luz a cena pode ter antes do clipping.

## Como funciona
Por View de dispositivo (padrão sRGB), o seletor troca entre Standard, AgX, Filmic e Linear: Standard destina-se a vídeo sem fotorealismo e material pronto (sem compressão de faixa); AgX estende a faixa útil para ~16,5 stops com desaturação em luzes altas; Filmic é o antecessor direto; Linear assume display sem transform (uso de referência). A doc do color management lista os Views disponíveis por dispositivo — é aí que a escolha acontece, no render e na preview, cada um com seus Views.

## Exemplo
Uma cena de pôr do sol com céu HDR 'estoura' em Standard mas vira gradiente legível em AgX — sem toque em nenhuma luz: a mudança foi no destino, não na fonte. A look (olho estilizado) entra depois, por Look.

## Limites e trade-offs
Trocar o transform não re-gradua texturas já authoradas para o outro destino (pintura feita em Filmic muda de aspecto em AgX). 'Standard é só para vídeo' é a regra da doc para o caso fotográfico; uso artístico de outros Views tem seu lugar declarado (Linear p/ referência). O render final e a exibição podem divergir quando o destino do arquivo não acompanha o View do display (nota separada sobre salvamento).

## Como verificar
Renderize o mesmo quadro em cada View e meça a curva em um rampa cinza 0..4 em scopes — a diferença de shoulder é o que você está padronizando. Grave o View escolhido no template de projeto e num teste que falha se o .blend divergir do preset do pipeline. Para look-dev, compare frames com Look desligado e transform ligado.

## Conexões
- [[blender-non-color-dados-nunca-convertidos]] — Blender: máscaras, normal maps e LUTs são Non-Color — converter dado é corromper sinal.

## Fontes
- [Blender — Displays & Views](https://docs.blender.org/manual/en/latest/render/color_management/displays_views.html) — página oficial que lista os Views por dispositivo e suas propriedades Consulta: 2026-10-04.
- [Blender — Color Spaces](https://docs.blender.org/manual/en/latest/render/color_management/color_spaces.html) — o outro lado do pipeline: espaços de entrada/trabalho vs Views de saída Consulta: 2026-10-04.
