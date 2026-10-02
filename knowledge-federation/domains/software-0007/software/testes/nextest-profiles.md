---
id: software.testes.tranche15.000941
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
fontes: ["https://nexte.st/docs/configuration/", "https://nexte.st/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: separar perfis local e de integração contínua

## Em uma frase
Configurações ficam em arquivo de perfil no workspace, com um perfil padrão e perfis nomeados que podem ser selecionados na linha de comando.

## Por que importa
Feedback local e evidência de pipeline têm objetivos distintos: um prioriza velocidade e interrupção cedo, o outro prioriza coleta completa e relatório.

## Como funciona
Defina o perfil de desenvolvimento com parada na primeira falha e o perfil de integração com coleta completa, retries e saída estruturada.

## Exemplo
`cargo nextest run --profile ci` carrega o perfil nomeado, e o arquivo de configuração mora em `.config/nextest.toml` na raiz do workspace.

## Limites e trade-offs
Perfis herdam do padrão e diferenças ficam escondidas quando o arquivo não é versionado; configuração local fora do repositório quebra a reprodutibilidade do pipeline.

## Como verificar
Rode a mesma suíte com os dois perfis e compare comportamento de parada, tempo e artefatos gerados por cada um.

## Conexões
- [[nextest-process-per-test]] — Veja também: nextest: isolar cada teste em processo próprio.
- [[nextest-retries-and-flaky-result]] — Veja também: nextest: usar retries com política explícita.

## Fontes
- [nextest — Configuration](https://nexte.st/docs/configuration/) — perfis, overrides, retries, timeouts e grupos de teste; consultado em 2026-10-02.
- [nextest — Documentation](https://nexte.st/docs/) — visão geral do runner, instalação e operação; consultado em 2026-10-02.
