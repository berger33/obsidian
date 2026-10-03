---
id: software.testes.tranche24.001821
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
fontes: ["https://raw.githubusercontent.com/Behat/Behat/master/README.md", "https://docs.behat.org/en/latest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalação oficial: um require de dev

## Em uma frase
O README define o caminho padrão: "The easiest way to install Behat is by using Composer", com o comando "composer require --dev behat/behat" e a execução resultante via "vendor/bin/behat" — o pacote vive como dependência de desenvolvimento, não do runtime do produto.

## Por que importa
O --dev não é decorativo: o framework de especificação executável é ferramenta de build/qualidade; declará-lo dev-dependency mantém o artefato de produção limpo e o versionamento preso ao composer.lock junto com phpunit e afins.

## Como funciona
No repositório do projeto PHP, rode o require --dev, commite composer.lock, e adicione o binário vendor/bin/behat ao passo de teste do CI; a configuração inicial do projeto (behat.yml e os contexts) segue os guias da documentação linkada.

## Exemplo
Fluxo mínimo: composer require --dev behat/behat; vendor/bin/behat — a doc aponta para o quick start para além disso.

## Limites e trade-offs
O README cobre o instalador padrão via Composer; distribuição phar ou global não são mencionadas no trecho lido, e a nota não afirma disponibilidade desses caminhos.

## Como verificar
O bloco "Installing Behat" do README oficial define o comando e o caminho de execução.

## Conexões
- [[behat-what-it-is]] — Veja também: Behat: BDD em linguagem natural para PHP.
- [[behat-development-version]] — Veja também: Rodando a versão de desenvolvimento.

## Fontes
- [Behat — README oficial](https://raw.githubusercontent.com/Behat/Behat/master/README.md) — README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.; consultado em 2026-10-03.
- [Behat — documentação oficial (en/latest)](https://docs.behat.org/en/latest/) — Página inicial da documentação oficial do Behat com exemplo Gherkin, cobertura de aplicação inteira, profiles/tags/suites, componentes Symfony e extensões.; consultado em 2026-10-03.
