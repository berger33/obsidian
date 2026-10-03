---
id: software.testes.tranche15.000898
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
fontes: ["https://docs.deno.com/runtime/reference/cli/coverage/", "https://docs.deno.com/runtime/reference/cli/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno coverage: separar limiares de linhas, branches e funções

## Em uma frase
O comando de relatório exibe métricas de linha, branch e função, podendo aplicar thresholds para fazer o job falhar quando uma meta configurada não é atingida.

## Por que importa
Um único `--threshold` aplica o mesmo valor às três métricas e sobrepõe valores de configuração; sem a flag, `deno.json` pode estabelecer alvos por métrica.

## Como funciona
Exportação LCOV atende ferramentas de integração, enquanto HTML ajuda a localizar caminhos ainda não exercitados.

## Exemplo
Configure thresholds específicos em `deno.json` e gere LCOV com `deno coverage --lcov --output=coverage.lcov coverage/`; use `--threshold` apenas quando o limite comum for intencional.

## Limites e trade-offs
Um threshold não avalia se o comportamento está bem testado e pode ser confundido por exclusões ou perfis acumulados; interprete cada dimensão em contexto.

## Como verificar
Crie uma função com branch nunca tomado, rode a suíte, compare o relatório de métricas e force um valor mínimo acima do atual para verificar o código de saída do job.

## Conexões
- [[deno-test-coverage-raw-data-e-relatorio-limpo]] — Veja também: Deno test: limpar perfis de cobertura antes de medir uma nova suíte.
- [[deno-test-snapshot-atualizacao-com-diff-revisavel]] — Veja também: Deno test: revisar snapshots atualizados como fixtures de contrato.

## Fontes
- [Deno Runtime — deno coverage CLI](https://docs.deno.com/runtime/reference/cli/coverage/) — threshold único para lines/branches/functions, precedência sobre thresholds no deno.json e formatos; consultado em 2026-10-02.
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
