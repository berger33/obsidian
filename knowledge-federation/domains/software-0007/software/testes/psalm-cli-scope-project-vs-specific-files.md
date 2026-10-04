---
id: software.testes.tranche26.001995
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

# Escopo de execução na linha de comando: projeto inteiro `<projectFiles>` vs. arquivos específicos

## Em uma frase
A abertura de `docs/running_psalm/command_line_usage.md` mostra os dois modos de invocação após configurar o arquivo do projeto: rodar `./vendor/bin/psalm` sem argumentos na raiz escaneia todos os arquivos referenciados por `<projectFiles>` na configuração, enquanto passar caminhos explícitos — `./vendor/bin/psalm file1.php [file2.php...]` — executa a verificação sobre arquivos específicos (e `--help` lista todas as opções suportadas).

## Por que importa
Durante a edição local ou em hooks de pré-commit, verificar apenas `file1.php file2.php` dá resposta imediata sobre o trecho alterado, ao passo que a chamada sem argumentos (`./vendor/bin/psalm`) garante a consistência global de todos os diretórios declarados em `<projectFiles>`.

## Como funciona
Configure os diretórios de código e de testes dentro da seção `<projectFiles>` do `psalm.xml`, use `./vendor/bin/psalm` para a validação completa da suíte e passe caminhos individuais `./vendor/bin/psalm arquivo.php` para checagens pontuais rápidas.

## Exemplo
Enquanto o desenvolvedor corrige anotações de tipo num controlador específico, rodar `./vendor/bin/psalm src/Controller/OrderController.php` foca a saída naquele arquivo antes da rodada geral.

## Limites e trade-offs
Lembre-se de que alterações na assinatura de um método em `file1.php` podem quebrar chamadores em outros arquivos; por isso, para validar apenas o impacto das mudanças recentes sobre seus dependentes, o Psalm oferece também o modo incremental `--diff`.

## Como verificar
Conferi a seção inicial Running Psalm e Command-line options em `docs/running_psalm/command_line_usage.md`.

## Conexões
- [[psalm-phar-distribution-conflict-free]] — Veja também: Uso via Phar autocontido (`psalm.phar` ou `psalm/phar`) para evitar conflito de dependências.
- [[psalm-exit-status-codes-0-1-2]] — Veja também: Semântica dos códigos de saída do processo: 0 (limpo), 1 (erro de execução) e 2 (issues encontrados).

## Fontes
- [Psalm — Command-line usage (docs/running_psalm/command_line_usage.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md) — Guia oficial de linha de comando do Psalm: escopo de projeto vs arquivos, códigos de saída 0/1/2, integração --shepherd, execução rápida com --threads e --diff/--no-diff e revisão interativa com psalm-review.; consultado em 2026-10-03.
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
