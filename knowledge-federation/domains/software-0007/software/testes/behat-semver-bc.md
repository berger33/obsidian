---
id: software.testes.tranche24.001823
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

# Promessa de compatibilidade: interfaces e service constants

## Em uma frase
A seção Versioning do README declara a política: a partir da v3.0.0, o Behat segue Semantic Versioning v2.0.0, e o contrato específico é — "if all you do is implement interfaces... and use service constants..., you would not have any backwards compatibility issues with Behat until v4.0.0 (or later major) is released", com a ressalva de que uma quebra de BC pode ocorrer como medida rara para corrigir um issue sério; a definição detalhada de BC remete ao guia de compatibilidade do Symfony.

## Por que importa
Isso traduz o upgrade do framework em cálculo de risco para extensões: código que só implementa as interfaces públicas e consome service constants tem garantia documentada entre majors; código que tocou internals aceita risco próprio — e o guia do Symfony linkado dá o vocabulário para o code review de upgrade.

## Como funciona
Na revisão de uma extension: confirme que os pontos de contato são interfaces e constantes de serviço documentadas; fixe a dependência com caret em ~3 ou ^3 no composer.json do plugin e trate o anúncio de um major como janela de migração planejada, não susto.

## Exemplo
O README ancora a política nos dois tipos de exemplo: implementação de interface (o link aponta para ClassResolver) e constante de serviço (ContextExtension) — as formas que a garantia cobre nominalmente.

## Limites e trade-offs
A promessa cobre extensionistas que respeitam a fronteira; usuários que estenderam por herança de classes concretas ou hooks privados não estão no texto da garantia, e o caso extremamente raro de BC break por issue sério é exceção declarada.

## Como verificar
A seção "Versioning" do README oficial define a política e os dois exemplos linkados.

## Conexões
- [[behat-development-version]] — Veja também: Rodando a versão de desenvolvimento.
- [[behat-gherkin-features]] — Veja também: O formato: Feature, Background e Scenario em inglês estruturado.

## Fontes
- [Behat — README oficial](https://raw.githubusercontent.com/Behat/Behat/master/README.md) — README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.; consultado em 2026-10-03.
- [Repositório oficial Behat/Behat](https://github.com/Behat/Behat) — Repositório oficial do Behat no GitHub com código-fonte, suíte auto-hospedada em features/ e guia de contribuição.; consultado em 2026-10-03.
