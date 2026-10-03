---
id: software.testes.tranche26.001994
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
fontes: ["https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md", "https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Uso via Phar autocontido (`psalm.phar` ou `psalm/phar`) para evitar conflito de dependências

## Em uma frase
A seção Using the Phar de `installation.md` aborda o caso em que o seu projeto entra em conflito com uma ou mais dependências internas do próprio Psalm: a saída oficial é usar o Phar (um executável PHP autocontido), seja baixando-o diretamente das releases do GitHub (`wget https://github.com/vimeo/psalm/releases/latest/download/psalm.phar`, `chmod +x psalm.phar` e `./psalm.phar --version`), seja instalando o pacote wrapper via Composer com `composer require --dev psalm/phar`.

## Por que importa
Ferramentas de análise estática em PHP possuem sua própria árvore de dependências (parsers de AST, bibliotecas de console, etc.); se a aplicação sob análise exigir uma versão incompatível de um desses pacotes no mesmo `composer.json`, o pacote `vimeo/psalm` normal trava na resolução do Composer, enquanto o `psalm.phar` ou `psalm/phar` isola completamente as dependências internas.

## Como funciona
Quando houver conflito de pacotes no Composer com `vimeo/psalm`, substitua a instalação pelo pacote `composer require --dev psalm/phar` ou baixe o `psalm.phar` diretamente das releases do repositório oficial.

## Exemplo
Com `composer require --dev psalm/phar`, a equipe continua gerenciando a ferramenta pelo Composer no `require-dev`, mas consome o binário Phar isolado sem misturar a árvore de pacotes do analisador com a da aplicação.

## Limites e trade-offs
Ao usar o binário Phar, subcomandos auxiliares como o revisor interativo podem ser acionados diretamente pela flag `--review` no ponto de entrada principal (`./vendor/bin/psalm.phar --review ...`), como documentado no guia de linha de comando.

## Como verificar
Conferi a seção Using the Phar em `docs/running_psalm/installation.md` e a nota em `command_line_usage.md`.

## Conexões
- [[psalm-plugins-and-psalm-plugin-cli]] — Veja também: Ecossistema de plugins no Packagist e ativação com `vendor/bin/psalm-plugin enable`.
- [[psalm-cli-scope-project-vs-specific-files]] — Veja também: Escopo de execução na linha de comando: projeto inteiro `<projectFiles>` vs. arquivos específicos.

## Fontes
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
- [Psalm — Command-line usage (docs/running_psalm/command_line_usage.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md) — Guia oficial de linha de comando do Psalm: escopo de projeto vs arquivos, códigos de saída 0/1/2, integração --shepherd, execução rápida com --threads e --diff/--no-diff e revisão interativa com psalm-review.; consultado em 2026-10-03.
