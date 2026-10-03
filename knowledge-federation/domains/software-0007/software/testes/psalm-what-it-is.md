---
id: software.testes.tranche26.001990
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
fontes: ["https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md", "https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Psalm: ferramenta de análise estática para encontrar erros em aplicações PHP

## Em uma frase
O README oficial no repositório vimeo/psalm define o Psalm de forma direta: "Psalm is a static analysis tool for finding errors in PHP applications", acompanhado de um ambiente de demonstração interativa (Live Demo) em https://psalm.dev/ e da documentação oficial em https://psalm.dev/docs (gerada a partir da pasta docs do repositório).

## Por que importa
Em uma linguagem gradualmente tipada como o PHP, muitos erros de tipo, chamadas inválidas ou caminhos nulos só estourariam em produção se não fossem cobertos por um teste específico; o analisador estático inspeciona todo o código-fonte referenciado pelo projeto sem precisar executar as rotas.

## Como funciona
Instale o Psalm no projeto PHP, gere o arquivo de configuração inicial e integre a verificação ao fluxo de desenvolvimento e ao pipeline de integração contínua.

## Exemplo
Antes mesmo de instalar localmente, qualquer desenvolvedor pode colar um trecho de código PHP na Live Demo em psalm.dev para observar como o analisador infere tipos e aponta problemas.

## Limites e trade-offs
O Psalm analisa estaticamente o código-fonte e os docblocks; ele complementa, mas não substitui, testes funcionais e de unidade que validam regras de negócio dinâmicas.

## Como verificar
Conferi o README oficial na branch 6.x do repositório vimeo/psalm.

## Conexões
- [[psalm-composer-install-init-and-nocache]] — Veja também: Instalação com PHP >= 8.2 e Composer: `--init` para nível de erro e `--no-cache`.

## Fontes
- [Psalm — README oficial (branch 6.x)](https://raw.githubusercontent.com/vimeo/psalm/6.x/README.md) — README oficial do Psalm com definição, Live Demo em psalm.dev, documentação em psalm.dev/docs, badges do Shepherd, histórico de criador e mantenedores, canais no Telegram e contratos de suporte.; consultado em 2026-10-03.
- [Psalm — Installing (docs/running_psalm/installation.md)](https://raw.githubusercontent.com/vimeo/psalm/6.x/docs/running_psalm/installation.md) — Guia oficial de instalação do Psalm: requisito PHP >= 8.2 e Composer, --init e --no-cache, imagem Docker ghcr.io/danog/psalm (+30%/+50% mais rápida), plugins com psalm-plugin enable e uso via Phar.; consultado em 2026-10-03.
