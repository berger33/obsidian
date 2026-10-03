---
id: software.testes.tranche26.001997
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

# Aceleração máxima da análise: `--threads=[n]`, `--diff` (ativo por padrão) e diretório de cache no CI

## Em uma frase
A seção Running Psalm faster de `command_line_usage.md` destaca as duas opções de linha de comando que aceleram as builds: `--threads=[n]` para executar a análise em múltiplas threads e `--diff` para verificar apenas os arquivos atualizados desde a última execução e seus dependentes (observando que desde o Psalm 4 `--diff` vem ativado por padrão, podendo ser desativado com `--no-diff`); os dados da última rodada ficam no diretório de cache configurado em `configuration.md`, e combinar ambas (por exemplo `--threads=8 --diff`) produz a execução mais rápida possível.

## Por que importa
Em servidores de CI que criam containers limpos a cada job, se o diretório de cache do Psalm não for preservado entre execuções, o modo `--diff` não terá os metadados da rodada anterior e reanalisará tudo do zero; persistir o cache no CI destrava o ganho real de analisar apenas os arquivos alterados e seus dependentes.

## Como funciona
Em máquinas multi-core e servidores de build, rode com `--threads=[n]` (como `--threads=8 --diff`) e configure o servidor de CI para preservar o diretório de cache do Psalm entre execuções; quando quiser forçar uma reanálise completa ignorando o diff ou o cache, use `--no-diff` ou `--no-cache`.

## Exemplo
A combinação recomendada literalmente pelo guia oficial para velocidade máxima é `--threads=8 --diff` com o diretório de cache preservado entre builds.

## Limites e trade-offs
Como `--diff` depende do cache da execução anterior para saber quais arquivos mudaram e quais outros arquivos dependem deles, em auditorias de release limpa pode-se rodar com `--no-cache` (como mostra o próprio guia de instalação) para validar toda a árvore sem estado prévio.

## Como verificar
Conferi a seção Running Psalm faster em `docs/running_psalm/command_line_usage.md`.

## Conexões
- [[psalm-exit-status-codes-0-1-2]] — Veja também: Semântica dos códigos de saída do processo: 0 (limpo), 1 (erro de execução) e 2 (issues encontrados).
- [[psalm-shepherd-type-coverage-tracking]] — Veja também: Rastreamento de cobertura de tipos com `--shepherd` e os badges `shepherd.dev`.

## Fontes
- [Psalm — Command-line usage (docs/running_psalm/command_line_usage.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md) — Guia oficial de linha de comando do Psalm: escopo de projeto vs arquivos, códigos de saída 0/1/2, integração --shepherd, execução rápida com --threads e --diff/--no-diff e revisão interativa com psalm-review.; consultado em 2026-10-03.
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
