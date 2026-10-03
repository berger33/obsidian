---
id: software.testes.tranche16.001007
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
fontes: ["https://github.com/istanbuljs/nyc", "https://github.com/istanbuljs/istanbuljs"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nyc: consolidar dados de várias execuções

## Em uma frase
Os dados brutos ficam no diretório temporário, e a ferramenta permite mesclar arquivos de execuções distintas antes de gerar o relatório consolidado.

## Por que importa
Suítes separadas por tipo de teste produzem dados parciais, e julgar cobertura a partir de apenas uma delas subestima o comportamento exercitado.

## Como funciona
Faça cada execução gravar seus dados, preserve-os como artefato e mescle tudo em uma etapa única antes do relatório final.

## Exemplo
Testes unitários e de integração podem rodar em trabalhos diferentes e ter seus dados unidos antes do cálculo do total.

## Limites e trade-offs
A mesclagem exige arquivos gerados da mesma revisão, e diretórios antigos no projeto contaminam o resultado com dados obsoletos.

## Como verificar
Compare o total consolidado com a soma dos parciais e confirme que a diferença corresponde apenas à sobreposição de linhas.

## Conexões
- [[nyc-check-coverage-thresholds]] — Veja também: nyc: reprovar por limites de cobertura.
- [[nyc-typescript-and-source-maps]] — Veja também: nyc: ajustar a medição para código transpilado.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [Istanbul — monorepo oficial](https://github.com/istanbuljs/istanbuljs) — instrumentação JavaScript, bibliotecas de cobertura e geradores de relatório; consultado em 2026-10-03.
