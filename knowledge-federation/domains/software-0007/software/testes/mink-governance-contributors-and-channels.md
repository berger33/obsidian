---
id: software.testes.tranche25.001879
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/minkphp/Mink/master/README.md", "https://mink.behat.org/en/latest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Governança, canais comunitários e desenvolvimento do repositório

## Em uma frase
O README oficial lista os canais e mantenedores do projeto: site principal com documentação em https://mink.behat.org, grupo oficial no Google Groups (groups.google.com/group/behat), guia de patches/PRs em CONTRIBUTING.md, instalação de dependências de desenvolvimento via Composer (curl getcomposer.org/installer | php e php composer.phar install) e os lead developers Konstantin Kudryashov (everzet), Christophe Coevoet (stof) e Alexander Obuhovich (aik099), com CI em GitHub Actions (tests.yml) e pacote behat/mink no Packagist.

## Por que importa
Compartilhar mantenedores e lista de discussão com o Behat explica a forte coesão arquitetural entre os dois projetos, ao mesmo tempo em que o repositório minkphp/Mink permanece independente para uso fora do BDD.

## Como funciona
Ao contribuir com código para o Mink, instale as dependências via Composer no clone do repositório, confira o workflow tests.yml e siga as diretrizes do CONTRIBUTING.md; para a documentação, o link Edit on GitHub no topo de mink.behat.org aponta para o repositório separado minkphp/docs.

## Exemplo
Um ajuste na documentação da página inicial é proposto em minkphp/docs/blob/master/index.rst, enquanto correções na classe Session ou Mink vão para minkphp/Mink.

## Limites e trade-offs
A nota registra os dados de governança e canais publicados no README e na página inicial da doc; políticas específicas de cada driver vivem nos respectivos repositórios da organização minkphp.

## Como verificar
Conferi as seções Useful Links, Install Dependencies e Contributors do README oficial e o cabeçalho de mink.behat.org.

## Conexões
- [[mink-behat-and-phpunit-integrations]] — Veja também: Integrações oficiais: Behat MinkExtension e phpunit-mink.

## Fontes
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
