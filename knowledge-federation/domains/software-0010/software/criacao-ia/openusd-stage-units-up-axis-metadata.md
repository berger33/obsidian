---
id: software.criacao_ia.tranche03.000260
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://openusd.org/release/tut_xforms.html", "https://openusd.org/release/api/class_usd_stage.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: harmonizar upAxis, metersPerUnit e timeCodesPerSecond

## Em uma frase
Metadados de stage comunicam eixo vertical, escala métrica e escala temporal, mas não devem ser confundidos com transformação automática de cada asset.

## Por que importa
Duas cenas podem compartilhar coordenadas numéricas e ainda usar convenções diferentes de orientação ou escala. Animação também usa time codes sem unidade que precisam de taxa para converter a segundos, por isso intercâmbio exige ler metadata explícita em cada arquivo.

## Como funciona
Defina e valide `upAxis` por stage ou conforme convenção do site; consulte `metersPerUnit` para interpretar distância e `timeCodesPerSecond` para interpretar time samples. A documentação de xforms recomenda registrar eixo no arquivo para que ele funcione independentemente de configuração local. Conversões espaciais ou temporais precisam ser feitas pela ferramenta de pipeline quando necessário.

## Exemplo
Um importador detecta stage em eixo Z e escala métrica declarada, depois converte para convenção interna Y-up apenas uma vez e registra fator utilizado. Ao processar animação, transforma time codes com a taxa registrada em vez de assumir que frames são segundos.

## Limites e trade-offs
Metadata pode estar ausente ou depender de política de site, e definir um up axis não reorienta automaticamente malhas já autoradas. Diferentes consumidores podem interpretar ou aplicar convenções conforme configuração; valide cada fronteira de import/export.

## Como verificar
Leia metadata root layer e stage API, compare bounds conhecidos com escala esperada e amostre animação em tempo real equivalente após conversão. Inclua assets de eixo e escala conhecidos nos testes de interoperabilidade.

## Conexões
- [[openusd-flattening-stage-export]] — OpenUSD: flattening exporta resultado composto, não estrutura editável.

## Fontes
- [OpenUSD 26.08 — Transformations, Animation, and Layer Offsets](https://openusd.org/release/tut_xforms.html) — explica up axis, time codes e timeCodesPerSecond em arquivo de cena Consulta: 2026-10-04.
- [OpenUSD 26.08 — UsdStage API](https://openusd.org/release/api/class_usd_stage.html) — documenta metadata e métodos de configuração do stage Consulta: 2026-10-04.
