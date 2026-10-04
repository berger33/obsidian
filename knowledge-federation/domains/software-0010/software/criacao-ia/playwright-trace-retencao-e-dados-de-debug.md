---
id: software.criacao_ia.tranche03.000275
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://playwright.dev/docs/trace-viewer", "https://playwright.dev/docs/api/class-testoptions#test-options-trace"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright Trace: coletar diagnóstico sem expor dados de teste

## Em uma frase
Uma trace reúne ações, snapshots de DOM, screenshots e logs que ajudam a reconstruir a execução após o teste.

## Por que importa
Esse material explica falhas intermitentes melhor que uma mensagem final, mas pode incluir conteúdo exibido na página, URLs, rede e dados de usuário. Artefato útil para debug também é um pacote de dados que precisa de política de acesso e retenção.

## Como funciona
No CI, a documentação recomenda `trace: on-first-retry`; use `retain-on-failure` quando não houver retry e remova arquivos de testes bem-sucedidos. Abra com CLI `show-trace` ou viewer local; trace.playwright.dev carrega o arquivo no browser sem transmiti-lo externamente segundo a documentação. Limite quem baixa artefatos e evite anexar dados reais desnecessários.

## Exemplo
Um pipeline de staging registra trace apenas na primeira repetição. Após corrigir uma falha, o artefato expira conforme prazo interno; nomes de conta e requests de teste usam dados sintéticos, e acesso ao relatório é restrito à equipe responsável.

## Limites e trade-offs
Registrar trace para todos os testes pode ser pesado e pode conservar dados de páginas sensíveis. O viewer local não elimina riscos de upload para armazenamento compartilhado ou de configuração inadequada de CORS ao abrir traces remotas.

## Como verificar
Inspecione conteúdo de uma trace de teste e inventarie capturas, logs, URLs e dados de request. Verifique retenção, permissões, opção selecionada no retry e remoção do artefato após sucesso.

## Conexões
- [[playwright-service-worker-network-routing]] — Playwright: service workers mudam visibilidade de network routing.
- [[playwright-video-context-close-artifact]] — Playwright video: fechar browser context para salvar o arquivo.

## Fontes
- [Playwright — Trace Viewer](https://playwright.dev/docs/trace-viewer) — explica conteúdo do trace, estratégias de recording e opção de primeiro retry Consulta: 2026-10-04.
- [Playwright — Test options trace](https://playwright.dev/docs/api/class-testoptions#test-options-trace) — define modos configuráveis de gravação e retained traces Consulta: 2026-10-04.
