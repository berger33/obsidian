---
id: software.testes.tranche15.000942
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/configuration/", "https://nexte.st/docs/running/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: usar retries com política explícita

## Em uma frase
Retries configuram quantas vezes um teste falho é repetido, e a política de resultado define se a execução final conta como falha ou como instável.

## Por que importa
Repetir sem política pode tornar o pipeline verde sobre um defeito real, enquanto não repetir deixa a flutuação conhecida quebrar builds repetidamente.

## Como funciona
Habilite retries no perfil de integração e escolha explicitamente como o resultado final deve ser tratado quando a repetição passar.

## Exemplo
A configuração pode declarar `retries = 1` e `flaky-result = \"fail\"` para que a flutuação apareça como falha mesmo tendo passado na segunda tentativa.

## Limites e trade-offs
A política de resultado não habilita a repetição sozinha: sem o orçamento de tentativas configurado, o comportamento não muda e a impressão é de defeito no executor.

## Como verificar
Force um teste a falhar na primeira tentativa e passar na segunda, observando o relatório com cada combinação de retries e política.

## Conexões
- [[nextest-profiles]] — Veja também: nextest: separar perfis local e de integração contínua.
- [[nextest-slow-timeout]] — Veja também: nextest: detectar e interromper testes lentos.

## Fontes
- [nextest — Configuration](https://nexte.st/docs/configuration/) — perfis, overrides, retries, timeouts e grupos de teste; consultado em 2026-10-02.
- [nextest — Running tests](https://nexte.st/docs/running/) — execução, filtros, saída, listagem e testes ignorados; consultado em 2026-10-02.
