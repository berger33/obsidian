---
id: software.testes.tranche16.000965
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://www.artillery.io/docs/get-started/first-test", "https://github.com/artilleryio/artillery"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: interpretar o resumo de métricas

## Em uma frase
Durante a execução a ferramenta publica resumo periódico, e ao final apresenta contagens de cenários, requisições, taxas e distribuição de latência.

## Por que importa
Ler apenas a média de latência esconde cauda longa, e é justamente a cauda que costuma indicar o comportamento sob carga.

## Como funciona
Acompanhe percentuais altos, taxa de requisições, contagem de erros e cenários interrompidos, comparando sempre com uma execução de referência.

## Exemplo
Um aumento de latência no percentil 99 com mediana estável sugere contenção pontual, enquanto elevação simultânea de erros indica saturação de recurso.

## Limites e trade-offs
Métricas de cliente medem a experiência da jornada simulada e não substituem a observabilidade do servidor, que aponta qual recurso está saturado.

## Como verificar
Repita a mesma execução em dois momentos e compare os números antes de atribuir qualquer variação ao sistema sob teste.

## Conexões
- [[artillery-thresholds]] — Veja também: Artillery: impor limites de desempenho.
- [[artillery-browser-engine]] — Veja também: Artillery: medir navegador com mecanismo de browser.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
