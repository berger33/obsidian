---
id: software.testes.tranche12.000552
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
fontes: ["https://playwright.dev/docs/test-webserver", "https://playwright.dev/docs/test-configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: prontidão do servidor local

## Em uma frase
A opção `webServer` inicia um processo de aplicação e aguarda a URL configurada responder antes de liberar os testes.

## Por que importa
Esperar por disponibilidade evita que a primeira navegação concorra com compilação ou inicialização e reduz dependência de atrasos fixos no começo da suíte.

## Como funciona
Declare o comando, a URL de readiness e o diretório de trabalho no arquivo de configuração; use `reuseExistingServer` quando o fluxo local puder aproveitar um servidor já ativo e `baseURL` para navegações relativas.

## Exemplo
Um comando de desenvolvimento pode iniciar a aplicação e Playwright só começar a abrir páginas quando o endpoint de saúde responder, sem inserir `sleep` em cada teste.

## Limites e trade-offs
Uma URL HTTP acessível não garante que todas as dependências ou dados de negócio estejam prontos. Ambientes compartilhados também exigem cuidado para não reaproveitar um processo de outra revisão.

## Como verificar
Pare o servidor, rode a suíte e observe o log de inicialização; em seguida deixe uma instância ativa para conferir que a opção de reuse se comporta como foi configurada.

## Conexões
- [[playwright-project-dependencies-setup]] — Veja também: Playwright Test: setup como dependência de projeto.
- [[playwright-sharding-ci-particionamento]] — Veja também: Playwright Test: particionamento por shards na CI.

## Fontes
- [Playwright — Web server](https://playwright.dev/docs/test-webserver) — prontidão do servidor, URL, reuseExistingServer, baseURL e múltiplos servidores; consultado em 2026-10-02.
- [Playwright — Test configuration](https://playwright.dev/docs/test-configuration) — configuração de testDir, projetos, expect, retries, workers e artefatos; consultado em 2026-10-02.
