---
id: software.testes.tranche12.000556
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://playwright.dev/docs/downloads", "https://playwright.dev/docs/api/class-download"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: persistir downloads antes de fechar o contexto

## Em uma frase
O evento de download fornece um objeto temporário cujo arquivo é removido quando o browser context que o criou é encerrado.

## Por que importa
Uma assertion sobre nome ou conteúdo depende de preservar o artefato antes que a limpeza normal do teste destrua o caminho temporário.

## Como funciona
Registre `page.waitForEvent('download')` antes da ação que inicia a transferência, aguarde o evento e use `saveAs()` para copiar o arquivo ao diretório de resultados do teste.

## Exemplo
Um teste de exportação clica em “CSV”, espera o download e salva uma cópia com nome determinístico antes de validar cabeçalho e quantidade de linhas.

## Limites e trade-offs
Guardar o arquivo em caminho compartilhado pode causar colisões entre workers. O caminho temporário interno não deve ser tratado como artefato de longa duração.

## Como verificar
Force um download, leia o caminho salvo depois da assertion e confirme que o artefato continua disponível após o context ser fechado.

## Conexões
- [[playwright-page-object-contract]] — Veja também: Playwright Test: limites de um Page Object.
- [[playwright-apirequest-cookie-context]] — Veja também: Playwright Test: cookies em APIRequestContext.

## Fontes
- [Playwright — Downloads](https://playwright.dev/docs/downloads) — evento de download, salvamento persistente e remoção ao encerrar o contexto; consultado em 2026-10-02.
- [Playwright — Download API](https://playwright.dev/docs/api/class-download) — métodos saveAs, failure e path de objetos Download; consultado em 2026-10-02.
