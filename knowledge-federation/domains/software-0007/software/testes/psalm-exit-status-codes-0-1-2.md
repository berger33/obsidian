---
id: software.testes.tranche26.001996
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

# Semântica dos códigos de saída do processo: 0 (limpo), 1 (erro de execução) e 2 (issues encontrados)

## Em uma frase
A seção Exit status de `command_line_usage.md` define com precisão os códigos de retorno do processo: o Psalm termina com status `0` quando concluiu a análise com sucesso e não encontrou nenhum problema (issue), status `1` quando houve um problema ao executar o próprio Psalm (por exemplo, configuração inválida ou falha de inicialização) e status `2` quando concluiu a análise com sucesso mas encontrou algum problema de código; qualquer outro código além de 0, 1 e 2 indica um problema interno.

## Por que importa
Distinguir código `1` (a ferramenta não conseguiu rodar) de código `2` (a ferramenta rodou normalmente e achou erros de tipo no código analisado) é essencial para scripts de CI, wrappers de IDE e automações que precisam separar falha de infraestrutura de falha de qualidade de código.

## Como funciona
Em scripts de automação que envolvem o Psalm, trate `0` como aprovado, `2` como reprovação por issues de análise estática reportados e `1` (ou códigos fora de 0/1/2) como erro operacional ou interno da ferramenta.

## Exemplo
Se alguém cometer um erro de sintaxe no `psalm.xml` ou passar uma flag inválida, o código de saída distingue essa falha operacional (`1`) de uma rodada válida que detectou um argumento nulo indevido no PHP (`2`).

## Limites e trade-offs
Tanto o status `1` quanto o status `2` são diferentes de zero e, portanto, interrompem automaticamente jobs padrão de CI (como GitHub Actions ou GitLab CI) sem configuração extra.

## Como verificar
Conferi a seção Exit status em `docs/running_psalm/command_line_usage.md`.

## Conexões
- [[psalm-cli-scope-project-vs-specific-files]] — Veja também: Escopo de execução na linha de comando: projeto inteiro `<projectFiles>` vs. arquivos específicos.
- [[psalm-fast-execution-threads-and-diff-cache]] — Veja também: Aceleração máxima da análise: `--threads=[n]`, `--diff` (ativo por padrão) e diretório de cache no CI.

## Fontes
- [Psalm — Command-line usage (docs/running_psalm/command_line_usage.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md) — Guia oficial de linha de comando do Psalm: escopo de projeto vs arquivos, códigos de saída 0/1/2, integração --shepherd, execução rápida com --threads e --diff/--no-diff e revisão interativa com psalm-review.; consultado em 2026-10-03.
- [Psalm — README oficial (branch 6.x)](https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md) — README oficial do Psalm com definição, Live Demo em psalm.dev, documentação em psalm.dev/docs, badges do Shepherd, histórico de criador e mantenedores, canais no Telegram e contratos de suporte.; consultado em 2026-10-03.
