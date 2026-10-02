---
id: software.testes.tranche14.000750
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://bazel.build/reference/test-encyclopedia", "https://bazel.build/docs/user-manual"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Bazel: delimitar o contrato hermético do teste

## Em uma frase
Um teste executado por Bazel deve depender de fontes declaradas, produtos de build declarados e recursos cujo comportamento o runner garante.

## Por que importa
A reprodutibilidade depende de remover pressupostos invisíveis como diretório da máquina, relógio, rede externa ou variáveis locais que não foram declaradas.

## Como funciona
Trate o contrato do Test Encyclopedia como limite: use apenas runfiles e recursos fornecidos pelo runner, e faça dependências externas serem explícitas ou substituídas por fixtures controladas.

## Exemplo
Um teste que lê `./config.json` do checkout pode passar localmente e falhar em sandbox; declarar o arquivo em `data` e abri-lo via runfiles deixa a dependência visível.

## Limites e trade-offs
A especificação descreve o resultado pretendido, mas algumas garantias não são atualmente impostas pelo runner; hermeticidade continua responsabilidade do teste.

## Como verificar
Execute o alvo em sandbox e numa segunda máquina ou worker remoto, verificando se nenhum caminho absoluto, home local ou serviço incidental altera o resultado.

## Conexões
- [[bazel-test-runtime-files-through-runfiles]] — Veja também: Bazel: fornecer arquivos de runtime por runfiles.

## Fontes
- [Bazel — Test encyclopedia](https://bazel.build/reference/test-encyclopedia) — contrato normativo do ambiente de execução, hermeticidade, runfiles, timeout e shards; consultado em 2026-10-02.
- [Bazel — Commands and Options](https://bazel.build/docs/user-manual) — opções de bazel test, seleção de alvos, variáveis, saída e argumentos; consultado em 2026-10-02.
