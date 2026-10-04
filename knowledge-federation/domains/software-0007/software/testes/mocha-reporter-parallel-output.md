---
id: software.testes.tranche13.000658
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://mochajs.org/reporters/", "https://mochajs.org/features/parallel-mode/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: combinar reporter com o modo de execução

## Em uma frase
Reporters transformam resultados em saída de terminal ou arquivos, e algumas opções precisam conhecer a suíte inteira antes da execução.

## Por que importa
Escolher formato conforme o consumidor melhora diagnóstico humano ou integração com CI sem exigir parsing frágil do terminal.

## Como funciona
Selecione reporter via CLI ou configuração, guarde arquivos que a pipeline consome e valide compatibilidade antes de ativar `--parallel`; os reporters que dependem de contagem prévia podem não funcionar ali.

## Exemplo
Uma execução local pode usar o reporter spec para leitura e outra exportar JSON para um job que agrega resultados após o processo concluir.

## Limites e trade-offs
Em paralelo a saída é agrupada por arquivo e certos reporters são incompatíveis. Arquivo gerado localmente também pode desaparecer se o job não publicar artefatos.

## Como verificar
Execute a suíte com a combinação exata de reporter e workers da CI e confira tanto status de saída quanto a presença do arquivo de relatório.

## Conexões
- [[mocha-grep-focused-suite]] — Veja também: Mocha: filtrar casos sem deixar foco acidental.
- [[mocha-global-fixture-lifecycle]] — Veja também: Mocha: separar fixture global de hooks de suite.

## Fontes
- [Mocha — Reporters](https://mochajs.org/reporters/) — built-in reporter output formats; consultado em 2026-10-02.
- [Mocha — Parallel Mode](https://mochajs.org/features/parallel-mode/) — workers, nondeterministic file order and parallel-mode limitations; consultado em 2026-10-02.
