---
id: software.testes.tranche10.000388
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://jestjs.io/docs/snapshot-testing", "https://jestjs.io/docs/mock-functions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: revisar mudança de snapshot antes de atualizar

## Em uma frase
Snapshot armazena uma representação serializada para comparar execuções futuras e detectar mudanças de saída.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Atualizar snapshot automaticamente sem revisar o diff pode converter regressão visual ou estrutural em novo baseline.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Inspecione a diferença, confirme a intenção do produto e atualize os arquivos somente depois de validar a mudança.

## Exemplo
Uma alteração intencional no rótulo atualiza o snapshot; uma mudança inesperada no preço ou no texto mantém o teste falhando até investigação.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Snapshot grande ou instável produz ruído e não substitui assertions focadas nas propriedades críticas.

## Como verificar
Revise o diff gerado na revisão de código e combine snapshots com assertions semânticas para dados importantes.

## Conexões
- [[jest-mock-modulos-esm-commonjs]] — Veja também: Jest: escolher API de mock conforme ESM ou CommonJS.
- [[jest-coverage-thresholds-nao-medir-qualidade-sozinhos]] — Veja também: Jest: usar thresholds de cobertura como guarda de mudança.

## Fontes
- [Jest 30.5 — Snapshot testing](https://jestjs.io/docs/snapshot-testing) — criação, revisão e atualização de snapshots; consultado em 2026-10-02.
- [Jest 30.5 — Mock Functions](https://jestjs.io/docs/mock-functions) — estado de chamadas, resultados, implementações e spies; consultado em 2026-10-02.
