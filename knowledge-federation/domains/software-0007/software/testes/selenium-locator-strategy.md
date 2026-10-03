---
id: software.testes.tranche17.001096
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/", "https://github.com/SeleniumHQ/selenium"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: escolher localizadores estáveis

## Em uma frase
Os localizadores identificam elementos por identificador, seletor de estilo, texto visível ou caminho estrutural, com estabilidade decrescente nessa ordem em geral.

## Por que importa
A escolha do localizador determina quanto o teste resiste a mudanças de estilo e de marcação, e caminhos estruturais quebram com qualquer reordenação.

## Como funciona
Prefira identificadores dedicados à automação e seletores de estilo ancorados em atributos estáveis, evitando textos que mudam com revisão de conteúdo.

## Exemplo
Um campo de busca pode ser localizado por identificador dedicado, enquanto o botão de envio usa seletor com atributo de nome acessível.

## Limites e trade-offs
Localizadores por texto quebram com tradução, e caminhos absolutos dependem de cada elemento intermediário da página.

## Como verificar
Renomeie um atributo de estilo e confirme que apenas os localizadores realmente frágeis deixam de encontrar o elemento.

## Conexões
- [[selenium-explicit-waits]] — Veja também: Selenium: esperar condições com limite.

## Fontes
- [Selenium — Page object models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) — objetos de página e de componente e boas práticas de estruturação; consultado em 2026-10-03.
- [Selenium — repositório oficial](https://github.com/SeleniumHQ/selenium) — código-fonte e documentação das ligações por linguagem; consultado em 2026-10-03.
