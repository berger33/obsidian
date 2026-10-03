---
id: software.testes.tranche15.000876
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://coverage.readthedocs.io/en/latest/", "https://coverage.readthedocs.io/en/latest/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: declarar source para incluir módulos sem execução

## Em uma frase
Configurar `source` delimita o código que será medido e permite que o relatório encontre arquivos Python elegíveis que não foram importados durante a suíte.

## Por que importa
Sem limite de origem, o collector pode reportar somente arquivos observados; código completamente fora da execução pode desaparecer da tabela.

## Como funciona
Um pacote ou diretório declarado também ajuda a evitar misturar cobertura da biblioteca padrão ou de dependências externas ao objetivo do projeto.

## Exemplo
Defina `[run] source = src/minha_app` no arquivo de configuração e execute testes; veja se módulos sem teste aparecem como 0% em vez de sumirem do relatório.

## Limites e trade-offs
Arquivos gerados, plugins e múltiplos pacotes podem exigir uma lista ou mapeamento de caminhos bem pensado; incluir tudo indiscriminadamente dilui o sinal com código fora do contrato.

## Como verificar
Crie um módulo não importado sob a origem declarada e confirme que o relatório o lista como não executado, depois exclua apenas diretórios deliberadamente fora do escopo.

## Conexões
- [[coverage-py-exclusao-de-codigo-afeta-o-total]] — Veja também: coverage.py: revisar como exclusões alteram statements e branches reportados.
- [[coverage-py-contexto-de-cobertura-nao-e-assertividade]] — Veja também: coverage.py: não interpretar linha executada como comportamento validado.

## Fontes
- [Coverage.py 7.16.2 — Documentation](https://coverage.readthedocs.io/en/latest/) — origem medida, capacidades e visão geral dos relatórios; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Configuration reference](https://coverage.readthedocs.io/en/latest/config.html) — opções run/report, arquivos paralelos, paths, exclusões e limites; consultado em 2026-10-02.
