---
id: software.criacao_ia.tranche04.000362
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
fontes: ["https://docs.blender.org/manual/en/latest/render/color_management/color_spaces.html", "https://docs.blender.org/manual/en/latest/render/color_management/displays_views.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender: máscaras, normal maps e LUTs são Non-Color — converter dado é corromper sinal

## Em uma frase
Imagens que codificam números (vetores de normal, máscaras de altura, tabelas de lookup) precisam de Color Space Non-Color; o pipeline sRGB do resto reinterpreta esses bytes como luminância e deforma o dado.

## Por que importa
É a família de bug 'o normal map parece estranho sob luz rasante' e 'a rampa de altura ficou torta': a textura foi lida com decode sRGB→linear quando cada pixel era um valor cru. A página Color Spaces define o espaço Non-Color como o dos dados que não representam cor — a recusa de conversão é a função, não um ajuste fino.

## Como funciona
No atributo da imagem (image editor > sidebar N > Source, ou no node Image), defina o Color Space como Non-Color para normal/depth/mask/LUT; imagens coloridas permanecem no File (sRGB) e o Working Space do cena é o espaço linear de composição. A doc também cobre o caso de View Transform inverso para composições prontas ('View' do tipo 'Raw'/'Inverse' para material já finalizado que não deve ser re-gradeado) — o princípio é um só: dizer ao pipeline que aquele dado não é cor de cena.

## Exemplo
Um displacement map vindo do Substance entra com Non-Color: sem isso, a sombra do cinza-médio é deslocada pelo decode e o relevo inteiro fica mais fundo/mais raso que o authorado.

## Limites e trade-offs
Non-Color no arquivo errado tem efeito oposto: albedo sem cor parece estourado/lavado. O espaço é por imagem (e pode divergir entre o arquivo e o datablock importado — confira após append). LUTs que já carregam suas próprias curvas pedem Non-Color no dado E View apropriado no consumo; dois toggles, dois papéis.

## Como verificar
Abra a imagem com o image editor, leia o valor de um pixel cinza 50%: em Non-Color é 128 (ou 0.5 cru), em sRGB é ~0.21 linear — a medição é a lição. Renderize um material só com o normal map e valide o reflexo numa esfera de teste. Um script de auditoria pode listar imports sem Non-Color nos tipos que o pipeline exige.

## Conexões
- [[blender-view-transform-agx-filmic-standard]] — Blender: o View Transform (AgX, Filmic, Standard) é decisão de destino, não de look.
- [[blender-what-you-see-is-not-what-you-save]] — Blender: o display view não é o arquivo salvo — o laço View as Render/Save as Render.

## Fontes
- [Blender — Color Spaces](https://docs.blender.org/manual/en/latest/render/color_management/color_spaces.html) — define os espaços (File/Non-Color/Working) e o papel de cada um Consulta: 2026-10-04.
- [Blender — Displays & Views](https://docs.blender.org/manual/en/latest/render/color_management/displays_views.html) — o outro lado: como Views tratam o dado já convertido Consulta: 2026-10-04.
