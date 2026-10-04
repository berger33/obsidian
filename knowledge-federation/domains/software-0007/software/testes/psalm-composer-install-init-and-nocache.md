---
id: software.testes.tranche26.001991
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

# Instalação com PHP >= 8.2 e Composer: `--init` para nível de erro e `--no-cache`

## Em uma frase
O guia oficial `docs/running_psalm/installation.md` informa que a versão mais recente do Psalm exige PHP >= 8.2 e Composer, instalada com `composer require --dev vimeo/psalm`; em seguida, gera-se o arquivo de configuração rodando `./vendor/bin/psalm --init` (que escaneia o projeto e calcula um nível de erro apropriado para a base de código) e executa-se a análise com `./vendor/bin/psalm --no-cache`.

## Por que importa
Em bases de código legadas ou grandes, começar exigindo o nível máximo de rigor de uma vez pode gerar milhares de avisos paralisantes; o fato de `psalm --init` escanear o projeto e escolher automaticamente um `error level` adequado permite adotar a ferramenta imediatamente e apertar o nível gradualmente.

## Como funciona
Instale com `composer require --dev vimeo/psalm` em PHP >= 8.2, execute `./vendor/bin/psalm --init` na raiz do projeto para criar o `psalm.xml` calibrado e rode `./vendor/bin/psalm --no-cache` na primeira verificação completa.

## Exemplo
Os três comandos sequenciais do guia de instalação — `composer require --dev vimeo/psalm`, `./vendor/bin/psalm --init` e `./vendor/bin/psalm --no-cache` — colocam a análise estática funcionando em qualquer projeto Composer compatível.

## Limites e trade-offs
Na primeira execução é normal que o Psalm encontre diversos problemas existentes; o próprio guia de instalação remete ao capítulo `dealing_with_code_issues.md` para estratégias de tratamento (como baseline ou supressão pontual).

## Como verificar
Conferi a abertura do guia oficial `docs/running_psalm/installation.md`.

## Conexões
- [[psalm-what-it-is]] — Veja também: Psalm: ferramenta de análise estática para encontrar erros em aplicações PHP.
- [[psalm-official-docker-image-performance]] — Veja também: A imagem Docker oficial `ghcr.io/danog/psalm`: PHP customizado +30% a +50% mais rápido.

## Fontes
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
- [Psalm — README oficial (branch 6.x)](https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md) — README oficial do Psalm com definição, Live Demo em psalm.dev, documentação em psalm.dev/docs, badges do Shepherd, histórico de criador e mantenedores, canais no Telegram e contratos de suporte.; consultado em 2026-10-03.
