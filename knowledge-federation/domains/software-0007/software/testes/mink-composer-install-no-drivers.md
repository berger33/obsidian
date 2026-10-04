---
id: software.testes.tranche25.001871
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
fontes: ["https://mink.behat.org/en/latest/", "https://raw.githubusercontent.com/minkphp/Mink/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalação via Composer: pacote base sem drivers por padrão

## Em uma frase
A seção Installation da documentação oficial recomenda instalar o Mink via Composer com composer require --dev behat/mink (ou php composer.phar require --dev behat/mink em instalações locais, exigindo ao menos PHP 5.4 na nota histórica da doc) e incluir require_once 'vendor/autoload.php'; logo em seguida, um aviso destaca que, por padrão, o Mink é instalado sem nenhum driver.

## Por que importa
Separar o núcleo dos drivers evita puxar dependências pesadas de Selenium, Chrome ou clientes HTTP que o projeto não vai utilizar; cada equipe instala via Composer apenas os pacotes de driver que realmente executará no CI.

## Como funciona
Execute composer require --dev behat/mink e, no mesmo passo de configuração, adicione ao menos um pacote de driver compatível com o seu tipo de teste antes de instanciar uma Session.

## Exemplo
Um projeto que só testa HTML renderizado no servidor instala behat/mink junto do driver headless escolhido, sem baixar clientes WebDriver desnecessários.

## Limites e trade-offs
Tentar usar o Mink recém-instalado apenas com behat/mink sem requerer um pacote de driver não funciona para testes reais, pois as classes concretas de Driver residem em pacotes Composer separados.

## Como verificar
Conferi a seção Installation e a caixa Note sobre ausência de drivers padrão em mink.behat.org.

## Conexões
- [[mink-what-it-is]] — Veja também: Mink: controlador e emulador de navegador para aplicações web em PHP.
- [[mink-eight-drivers-catalog]] — Veja também: O catálogo de oito drivers na documentação e a dupla recomendada.

## Fontes
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
