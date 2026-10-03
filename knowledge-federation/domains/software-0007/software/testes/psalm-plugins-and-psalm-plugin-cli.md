---
id: software.testes.tranche26.001993
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
fontes: ["https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md", "https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ecossistema de plugins no Packagist e ativação com `vendor/bin/psalm-plugin enable`

## Em uma frase
A seção Installing plugins de `installation.md` explica que, embora o Psalm consiga deduzir os tipos usados por várias bibliotecas a partir do código-fonte e de docblocks, ele funciona ainda melhor com tipos sob medida fornecidos por plugins do Psalm (listados no Packagist com `?type=psalm-plugin`), instalados e ativados com `composer require --dev <plugin/package> && vendor/bin/psalm-plugin enable <plugin/package>`.

## Por que importa
Frameworks e bibliotecas como Symfony, Laravel, Doctrine, PHPUnit ou Mockery usam containers de injeção de dependência, métodos mágicos e asserções dinâmicas que o código-fonte puro não explicita; ativar o plugin correspondente ensina essas convenções ao analisador e elimina falsos positivos.

## Como funciona
Procure na lista do Packagist (`packagist.org/?type=psalm-plugin`) os plugins para os frameworks e bibliotecas de teste do seu projeto, instale cada pacote com `composer require --dev` e habilite-o no `psalm.xml` rodando `vendor/bin/psalm-plugin enable <plugin/package>`.

## Exemplo
Em dois passos encadeados — `composer require --dev <plugin/package> && vendor/bin/psalm-plugin enable <plugin/package>` — o plugin é baixado e registrado na configuração do projeto.

## Limites e trade-offs
Apenas instalar o pacote do plugin no Composer sem executar `vendor/bin/psalm-plugin enable` (ou registrá-lo manualmente no `psalm.xml`) não ativa as regras customizadas de tipos durante a análise.

## Como verificar
Conferi a seção Installing plugins em `docs/running_psalm/installation.md`.

## Conexões
- [[psalm-official-docker-image-performance]] — Veja também: A imagem Docker oficial `ghcr.io/danog/psalm`: PHP customizado +30% a +50% mais rápido.
- [[psalm-phar-distribution-conflict-free]] — Veja também: Uso via Phar autocontido (`psalm.phar` ou `psalm/phar`) para evitar conflito de dependências.

## Fontes
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
- [Psalm — README oficial (branch 6.x)](https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md) — README oficial do Psalm com definição, Live Demo em psalm.dev, documentação em psalm.dev/docs, badges do Shepherd, histórico de criador e mantenedores, canais no Telegram e contratos de suporte.; consultado em 2026-10-03.
