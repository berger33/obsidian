---
id: software.testes.tranche24.001822
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/Behat/Behat/master/README.md", "https://github.com/Behat/Behat"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rodando a versão de desenvolvimento

## Em uma frase
Para quem vai mexer no framework, o README documenta o fluxo paralelo ao do usuário: clonar o repositório, instalar dependências com "composer install" e executar a versão em desenvolvimento via "bin/behat" (em vez do vendor/bin/behat do consumidor) — e antes de contribuir, a leitura pedida é o CONTRIBUTING.md do repositório.

## Por que importa
O dualismo bin/behat versus vendor/bin/behat é a materialização da separação entre usar e desenvolver: no checkout, o código-fonte do projeto é a própria instalação, o que permite reproduzir bugs do framework no mesmo binário que os executa.

## Como funciona
Para triar um comportamento suspeito do Behat, faça clone do master, composer install, e reproduza o caso com bin/behat apontando para a feature mínima — o diff entre master e a release instalada responde se o bug já foi corrigido.

## Exemplo
Um maintainer em treinamento roda a suíte de features do próprio repositório (a doc cita que o Behat testa a si mesmo com suas features) antes de propor mudança no parser de passos.

## Limites e trade-offs
A nota cobre o fluxo declarativo do README; o passo a passo de ambiente de teste do próprio projeto (Makefile, scripts) não está no trecho lido.

## Como verificar
As seções "Installing Development Version" e "Contributing" do README oficial definem o fluxo.

## Conexões
- [[behat-install-composer]] — Veja também: Instalação oficial: um require de dev.
- [[behat-semver-bc]] — Veja também: Promessa de compatibilidade: interfaces e service constants.

## Fontes
- [Behat — README oficial](https://raw.githubusercontent.com/Behat/Behat/master/README.md) — README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.; consultado em 2026-10-03.
- [Repositório oficial Behat/Behat](https://github.com/Behat/Behat) — Repositório oficial do Behat no GitHub com código-fonte, suíte auto-hospedada em features/ e guia de contribuição.; consultado em 2026-10-03.
