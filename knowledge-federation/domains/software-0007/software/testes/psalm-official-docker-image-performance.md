---
id: software.testes.tranche26.001992
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

# A imagem Docker oficial `ghcr.io/danog/psalm`: PHP customizado +30% a +50% mais rápido

## Em uma frase
Na seção Docker image de `installation.md`, a documentação oficial recomenda rodar o Psalm através da imagem Docker oficial `ghcr.io/danog/psalm:latest` (ou tags específicas como `ghcr.io/danog/psalm:6.9.1`), explicando o motivo: ela utiliza uma compilação customizada do PHP construída do zero que executa o Psalm em média **+30% mais rápido** do que o PHP normal (e **+50% mais rápido** se comparado ao PHP sem opcache instalado).

## Por que importa
Análise estática interprocedimental em projetos PHP grandes consome bastante CPU; ganhar 30% a 50% de velocidade média apenas trocando o runtime para a imagem `ghcr.io/danog/psalm` reduz diretamente o tempo de espera dos desenvolvedores e o custo de minutos de CI.

## Como funciona
Execute `docker run -v $PWD:/app --rm -it ghcr.io/danog/psalm:latest /composer/vendor/bin/psalm --no-cache` (fixando uma tag de versão como `ghcr.io/danog/psalm:6.9.1` no CI para reprodutibilidade).

## Exemplo
O comando oficial monta o diretório atual em `/app` (`-v $PWD:/app`) e invoca `/composer/vendor/bin/psalm --no-cache` dentro do contêiner descartável (`--rm`).

## Limites e trade-offs
A mesma seção observa que problemas causados por extensões PHP ausentes na imagem podem ser resolvidos habilitando-as no `psalm.xml`, declarando-as no `composer.json` ou, para extensões sem stub nativo no Psalm, usando stubs tradicionais do PHP como `JetBrains/phpstorm-stubs`.

## Como verificar
Conferi a seção Docker image em `docs/running_psalm/installation.md`.

## Conexões
- [[psalm-composer-install-init-and-nocache]] — Veja também: Instalação com PHP >= 8.2 e Composer: `--init` para nível de erro e `--no-cache`.
- [[psalm-plugins-and-psalm-plugin-cli]] — Veja também: Ecossistema de plugins no Packagist e ativação com `vendor/bin/psalm-plugin enable`.

## Fontes
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
- [Psalm — Command-line usage (docs/running_psalm/command_line_usage.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/command_line_usage.md) — Guia oficial de linha de comando do Psalm: escopo de projeto vs arquivos, códigos de saída 0/1/2, integração --shepherd, execução rápida com --threads e --diff/--no-diff e revisão interativa com psalm-review.; consultado em 2026-10-03.
