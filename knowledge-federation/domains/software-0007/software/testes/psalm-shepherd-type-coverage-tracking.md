---
id: software.testes.tranche26.001998
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
fontes: ["https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md", "https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rastreamento de cobertura de tipos com `--shepherd` e os badges `shepherd.dev`

## Em uma frase
A seção Shepherd de `command_line_usage.md` e os badges no topo do `README.md` documentam a integração pública para projetos no GitHub: adicionar a flag `--shepherd` envia informações sobre a build para `https://shepherd.dev`, que rastreia a cobertura de tipos (a porcentagem de tipos que o Psalm consegue inferir na base de código) nas branches `master`.

## Por que importa
Enquanto cobertura de testes tradicional mede quais linhas foram executadas em runtime, a cobertura de tipos medida pelo Shepherd mostra qual fração das variáveis, propriedades, parâmetros e retornos do projeto possui tipo conhecido pelo analisador estático (em vez de `mixed`).

## Como funciona
Em projetos públicos no GitHub, adicione `--shepherd` ao comando do Psalm no CI da branch principal para acompanhar a evolução da porcentagem de tipos inferidos em `shepherd.dev` e exibir os badges de `Psalm coverage` e `Psalm level`.

## Exemplo
O próprio repositório `vimeo/psalm` exibe no topo do seu README os dois badges gerados pelo serviço: `shepherd.dev/github/vimeo/psalm/coverage.svg` (cobertura de tipos) e `shepherd.dev/github/vimeo/psalm/level.svg` (nível de rigor).

## Limites e trade-offs
A integração `--shepherd` descrita na documentação é voltada a projetos públicos no GitHub; como ela envia metadados da build para o serviço externo `shepherd.dev`, não deve ser habilitada em repositórios privados que proíbam telemetria externa.

## Como verificar
Conferi a seção Shepherd em `docs/running_psalm/command_line_usage.md` e os badges do `README.md` oficial.

## Conexões
- [[psalm-fast-execution-threads-and-diff-cache]] — Veja também: Aceleração máxima da análise: `--threads=[n]`, `--diff` (ativo por padrão) e diretório de cache no CI.
- [[psalm-review-interactive-ide-tool]] — Veja também: Triagem interativa de issues na IDE com `psalm-review` (ou `psalm.phar --review`) e `report.json`.

## Fontes
- [Psalm — Command-line usage (docs/running_psalm/command_line_usage.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md) — Guia oficial de linha de comando do Psalm: escopo de projeto vs arquivos, códigos de saída 0/1/2, integração --shepherd, execução rápida com --threads e --diff/--no-diff e revisão interativa com psalm-review.; consultado em 2026-10-03.
- [Psalm — README oficial (branch 6.x)](https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md) — README oficial do Psalm com definição, Live Demo em psalm.dev, documentação em psalm.dev/docs, badges do Shepherd, histórico de criador e mantenedores, canais no Telegram e contratos de suporte.; consultado em 2026-10-03.
