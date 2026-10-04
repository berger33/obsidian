---
id: software.testes.tranche16.001005
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

# nyc: escolher relatórios e destino

## Em uma frase
A lista de geradores define os formatos produzidos, e o diretório de relatórios concentra os artefatos publicados.

## Por que importa
Terminal serve à leitura rápida, formato de intercâmbio alimenta serviços de cobertura e página navegável apoia investigação detalhada.

## Como funciona
Declare os formatos necessários no arquivo de configuração, mantenha o diretório dentro do ignorado pelo controle de versão e publique o artefato no pipeline.

## Exemplo
Uma configuração comum produz resumo no terminal, arquivo de intercâmbio e página navegável a partir dos mesmos dados.

## Limites e trade-offs
Formatos adicionais aumentam o tempo de geração e o volume de artefatos, e relatórios não versionados no repositório poluem revisões de código.

## Como verificar
Regenere os relatórios e confirme que os totais dos formatos textual e de intercâmbio são coerentes entre si.

## Conexões
- [[nyc-negated-excludes]] — Veja também: nyc: reabrir caminhos com padrões negados.
- [[nyc-check-coverage-thresholds]] — Veja também: nyc: reprovar por limites de cobertura.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [Istanbul — monorepo oficial](https://github.com/istanbuljs/istanbuljs) — instrumentação JavaScript, bibliotecas de cobertura e geradores de relatório; consultado em 2026-10-03.
