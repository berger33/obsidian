---
id: software.testes.tranche16.001053
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://hurl.dev/docs/manual.html", "https://github.com/Orange-OpenSource/hurl"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hurl: parametrizar e reportar execuções

## Em uma frase
Variáveis podem ser definidas por linha de comando ou arquivo, e a execução gera relatórios em formatos de página e de resultado de testes.

## Por que importa
Parametrizar endereço e credenciais permite usar o mesmo conjunto de arquivos em ambientes diferentes sem editar conteúdo.

## Como funciona
Passe valores sensíveis por variáveis de ambiente, mantenha padrões no arquivo para desenvolvimento e publique relatórios como artefato da execução.

## Exemplo
Endereço base e identificadores de ambiente podem variar por linha de comando enquanto os arquivos permanecem idênticos.

## Limites e trade-offs
Segredos gravados no arquivo acabam versionados, e relatórios podem conter dados sensíveis que não devem ser publicados sem revisão.

## Como verificar
Rode o mesmo arquivo contra dois endereços usando variáveis distintas e confirme que as respostas correspondem ao ambiente indicado.

## Conexões
- [[hurl-session-scope]] — Veja também: Hurl: entender o escopo da sessão.
- [[hurl-ci-integration]] — Veja também: Hurl: usar o resultado como verificação de esteira.

## Fontes
- [Hurl — Manual (CLI)](https://hurl.dev/docs/manual.html) — modo de teste, paralelismo, repetição, relatórios e códigos de saída; consultado em 2026-10-03.
- [Hurl — repositório oficial](https://github.com/Orange-OpenSource/hurl) — visão geral do projeto, exemplos e documentação complementar; consultado em 2026-10-03.
