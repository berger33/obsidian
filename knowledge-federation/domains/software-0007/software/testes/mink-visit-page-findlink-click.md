---
id: software.testes.tranche25.001875
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

# Fluxo básico de navegação e interação: visit, getPage, findLink, click e getContent

## Em uma frase
O README mostra o encadeamento fundamental da API do Mink: $mink->getSession()->visit($startUrl) abre a URL inicial, $mink->getSession()->getPage() obtém o elemento de documento da página atual, ->findLink('Downloads')->click() localiza um link e dispara o clique, e ->getContent() retorna o conteúdo bruto da página resultante.

## Por que importa
Separar Session (controle do navegador: visitar URL, cabeçalhos, status) de getPage() (inspeção e manipulação do DOM atual) mantém a API previsível: ações de navegador ficam na sessão e buscas de elementos ficam na página.

## Como funciona
Após chamar visit($url) na sessão, encadeie getPage() para localizar links, botões ou campos (como findLink('Downloads')) e invoque click() ou getContent() sobre o resultado.

## Exemplo
O exemplo do README executa $mink->getSession()->visit('http://example.com'), clica no link 'Downloads' via getPage()->findLink('Downloads')->click() e imprime echo $mink->getSession()->getPage()->getContent().

## Limites e trade-offs
Se findLink('Downloads') não encontrar o elemento na página, o retorno é nulo e encadear ->click() direto lançará erro fatal em PHP; em asserções de teste reais, valide a existência do elemento antes de interagir.

## Como verificar
Conferi o trecho de navegação e clique no Usage Example do README oficial.

## Conexões
- [[mink-mixing-sessions-multiuser]] — Veja também: Misturar sessões no mesmo teste para simular múltiplos usuários.
- [[mink-custom-driver-extensibility]] — Veja também: Arquitetura extensível por DriverInterface: o caso MyCustomDriver.

## Fontes
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
- [Mink — documentação oficial (en/latest)](https://mink.behat.org/en/latest/) — Página inicial da documentação oficial do Mink com definição como browser controller/emulator, instalação via Composer, catálogo de oito drivers, oito guias temáticos e integrações com Behat e PHPUnit.; consultado em 2026-10-03.
