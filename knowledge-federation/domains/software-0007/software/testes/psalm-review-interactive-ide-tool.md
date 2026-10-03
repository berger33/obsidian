---
id: software.testes.tranche26.001999
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md"
fontes: ["https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md", "https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Triagem interativa de issues na IDE com `psalm-review` (ou `psalm.phar --review`) e `report.json`

## Em uma frase
A seção Reviewing issues in your IDE of choice de `command_line_usage.md` apresenta a ferramenta `psalm-review` (também invocável via ponto de entrada principal com `./vendor/bin/psalm.phar --review`): primeiro gera-se um relatório JSON com `vendor/bin/psalm --report=report.json` e depois executa-se `./vendor/bin/psalm-review report.json [code|phpstorm|code-server] [ inv|rev|[~-]IssueType1 ] ...`, que lê o `report.json` e abre a IDE especificada exatamente na linha e coluna de cada issue, um por um (pressionando Enter para avançar ao próximo e `q` para sair).

## Por que importa
Quando uma execução do Psalm reporta dezenas de problemas espalhados por vários diretórios, copiar caminhos de arquivo e números de linha do terminal para o editor é lento; o `psalm-review` automatiza a navegação sequencial diretamente no VS Code, PhpStorm ou code-server e ainda permite filtrar por tipo de issue.

## Como funciona
Gere o relatório com `vendor/bin/psalm --report=report.json`, rode `./vendor/bin/psalm-review report.json` (se estiver dentro do terminal integrado do PhpStorm, VS Code ou code-server, a IDE é autodetectada via variáveis de ambiente; em terminal externo, informe `code`, `phpstorm` ou `code-server`), use nomes de `IssueType` para focar num único tipo de erro (ou `~IssueType` / `-IssueType` para excluí-lo) e passe `rev` ou `inv` se quiser começar pelo fim do relatório.

## Exemplo
Para corrigir todos os erros de um único tipo no VS Code a partir de um terminal externo, o desenvolvedor roda `vendor/bin/psalm --report=report.json` seguido de `./vendor/bin/psalm-review report.json code NomeDoIssue` e avança com Enter a cada correção.

## Limites e trade-offs
O argumento da IDE só é opcional quando o comando roda dentro do terminal integrado de uma das três IDEs suportadas (PhpStorm, VS Code, code-server); fora delas, omitir o nome da IDE impede a abertura automática.

## Como verificar
Conferi a seção Reviewing issues in your IDE of choice em `docs/running_psalm/command_line_usage.md`.

## Conexões
- [[psalm-shepherd-type-coverage-tracking]] — Veja também: Rastreamento de cobertura de tipos com `--shepherd` e os badges `shepherd.dev`.
- [[psalm-governance-history-and-support-contracts]] — Veja também: Origem no Vimeo, mantenedor ativo, canais no Telegram e contratos de suporte.

## Fontes
- [Psalm — Command-line usage (docs/running_psalm/command_line_usage.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md) — Guia oficial de linha de comando do Psalm: escopo de projeto vs arquivos, códigos de saída 0/1/2, integração --shepherd, execução rápida com --threads e --diff/--no-diff e revisão interativa com psalm-review.; consultado em 2026-10-03.
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
