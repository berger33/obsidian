---
id: software.testes.tranche15.000884
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
fontes: ["https://pestphp.com/docs/optimizing-tests", "https://pestphp.com/docs/continuous-integration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: desenhar testes independentes antes de habilitar parallel

## Em uma frase
A flag `--parallel` executa casos em vários processos; a melhora de tempo só é sustentável quando os testes toleram execução simultânea e não disputam estado mutável sem coordenação.

## Por que importa
A documentação alerta que recursos de banco não devem ser tratados como compartilhados, que ordem não é garantida e que processos podem criar race conditions.

## Como funciona
O runner distribui trabalho, mas não deduz que uma tabela, pasta temporária ou conta externa deve ser particionada.

## Exemplo
Comece com processos limitados, gere banco ou namespace por processo e remova dependências de ordem; habilite `--parallel` em uma suíte representativa antes de tornar o comando obrigatório.

## Limites e trade-offs
Mais processos também aumentam pressão de CPU, memória e backend; ajustar apenas `--processes` não corrige uma fixture global sem isolamento.

## Como verificar
Execute primeiro serial e depois com `--parallel --processes=4`, compare duração, falhas intermitentes e colisões dos recursos compartilhados.

## Conexões
- [[pest-sharding-balanceado-por-tempo]] — Veja também: Pest 5: atualizar tempos para distribuir shards por duração.
- [[pest-tia-baseline-nao-substitui-suite-integral]] — Veja também: Pest 5: manter Tia como aceleração local e suíte completa como contrato de CI.

## Fontes
- [Pest 5 — Optimizing Tests](https://pestphp.com/docs/optimizing-tests) — parallel testing, profiling, sharding balanceado por tempo e saída; consultado em 2026-10-02.
- [Pest 5 — Continuous Integration](https://pestphp.com/docs/continuous-integration) — execução integral em CI, browser plugin, parallel e artifacts; consultado em 2026-10-02.
