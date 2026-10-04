---
id: software.testes.tranche23.001743
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://infection.github.io/guide/installation.html", "https://infection.github.io/guide/command-line-options.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalar o phar assinado: GPG, phive, composer e brew

## Em uma frase
A página Installation oficial recomenda o phar como "the best and recommended way": baixar infection.phar mais infection.phar.asc do release (exemplo com a versão 0.32.0), chmod +x e — o diferencial de supply-chain — verificar a assinatura com as duas linhas gpg (recv-keys da chave C6D76C329EBADE2FB9C458CFC5095986493B4AA0 e --with-fingerprint --verify), conferindo que o fingerprint bate; o phar é assinado com a chave GPG do time, com o link da chave pública no site.

## Por que importa
O phar carrega uma decisão prática sobre ecossistema: vem empacotado com todos os test frameworks oficialmente suportados (PHPUnit, PhpSpec, Codeception e Testo), enquanto a instalação via composer infection/infection instala o PHPUnit por default e os adaptadores "automatically installed on demand".

## Como funciona
Os quatro canais documentados além do phar: copiar o binário para /usr/local/bin/infection para uso global; phive install infection (o PHAR Installation and Verification Environment, que repete a verificação); composer global require infection/infection com o PATH do vendor bin exportado no perfil; e brew tap infection/homebrew-infection mais brew install infection com link automático em /usr/local/bin.

## Exemplo
Adote o phar com verificação e versione os dois comandos gpg no seu script de setup de ambiente — a doc registra o fingerprint no corpo da página justamente para permitir esse checklist.

## Limites e trade-offs
A página Git para desenvolvimento do próprio Infection (bin/infection local após composer install) existe para contribuir com a ferramenta, não para uso cotidiano; e o fingerprint impresso na página é da chave do time no snapshot — a comunidade deve revalidar contra o site oficial no momento da instalação, não confiar em memória de blog.

## Como verificar
Abra a seção Installation do guia oficial e confirme o exemplo com 0.32.0, a chave C6D7... 4AA0, os quatro instaladores alternativos e a nota dos adaptadores on-demand.

## Conexões
- [[infection-msi-metrics]] — Veja também: As três métricas: MSI, Mutation Code Coverage e Covered Code MSI.
- [[infection-threads]] — Veja também: --threads: paralelismo primeiro, depois benchmark.

## Fontes
- [Infection — Installation](https://infection.github.io/guide/installation.html) — phar assinado, phive, composer, brew e tabela de compatibilidade; consultado em 2026-10-03.
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
