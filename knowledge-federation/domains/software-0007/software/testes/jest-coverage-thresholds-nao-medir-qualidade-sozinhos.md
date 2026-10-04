---
id: software.testes.tranche10.000389
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
fontes: ["https://jestjs.io/docs/configuration", "https://jestjs.io/docs/snapshot-testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: usar thresholds de cobertura como guarda de mudança

## Em uma frase
A configuração pode impor thresholds de cobertura globais ou para caminhos específicos e falhar quando o limite não é atingido.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Um total alto pode coexistir com caminhos críticos sem assertions sobre resultado, erro ou autorização.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Defina thresholds alinhados a risco e use relatórios de linha/branch para localizar lacunas em arquivos prioritários.

## Exemplo
A CI mantém cobertura de branch mínima para o módulo de cobrança e publica relatório detalhado para revisar linhas não exercitadas.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Cobertura mede execução instrumentada, não correção das assertions, qualidade do oracle ou completude do requisito.

## Como verificar
Introduza um defeito em uma branch executada e confirme se uma assertion falha; o contador de cobertura sozinho não deve ser tratado como prova.

## Conexões
- [[jest-snapshot-revisao-antes-de-atualizar]] — Veja também: Jest: revisar mudança de snapshot antes de atualizar.

## Fontes
- [Jest 30.5 — Configuration](https://jestjs.io/docs/configuration) — opções de cobertura e thresholds de configuração; consultado em 2026-10-02.
- [Jest 30.5 — Snapshot testing](https://jestjs.io/docs/snapshot-testing) — criação, revisão e atualização de snapshots; consultado em 2026-10-02.
