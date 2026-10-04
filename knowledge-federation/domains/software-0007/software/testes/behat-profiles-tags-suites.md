---
id: software.testes.tranche24.001827
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
fontes: ["https://docs.behat.org/en/latest/", "https://raw.githubusercontent.com/Behat/Behat/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Profiles, tags e suites: o mesmo feature, jeitos diferentes

## Em uma frase
A doc oficial fecha o argumento de flexibilidade com um caso de uso nomeado: "You can even use profiles, tags and suites to test the same features in different ways. For example, a quick regression test that directly calls your API handlers in PHP, or a more thorough test over HTTP when you've made bigger changes. It's all up to you!"

## Por que importa
O padrão que a frase descreve é um dos maiores economizadores de CI em projetos BDD: o mesmo contrato de negócio executado leve no dia a dia e pesado antes do release, sem duplicar a especificação em duas suítes divergentes — tags seletam, profiles trocam a configuração de execução.

## Como funciona
Configure suítes no behat.yml com filtros de tag, declare perfis com conjuntos de steps e contextos diferentes, e rode por perfil no CI: o smoke por perfil nos pushes, o perfil completo na janela de release.

## Exemplo
Exemplo da própria doc traduzido: feature de pagamento com @api e @http marcando os jeitos; o smoke roda o perfil de handlers PHP diretos, o teste de release valida a travessia HTTP inteira.

## Limites e trade-offs
Os nomes de opção e o formato completo do behat.yml não constam do trecho lido da página inicial; os guias da documentação cobrem os detalhes de configuração de perfis e suítes.

## Como verificar
O parágrafo de profiles/tags/suites da seção "Cover your whole application" sustenta a nota.

## Conexões
- [[behat-mix-approaches]] — Veja também: Misture tecnologias: navegador, HTTP, shell, banco e PHP direto.
- [[behat-under-the-hood-symfony]] — Veja também: Por dentro: componentes Symfony, qualquer framework.

## Fontes
- [Behat — documentação oficial (en/latest)](https://docs.behat.org/en/latest/) — Página inicial da documentação oficial do Behat com exemplo Gherkin, cobertura de aplicação inteira, profiles/tags/suites, componentes Symfony e extensões.; consultado em 2026-10-03.
- [Behat — README oficial](https://raw.githubusercontent.com/Behat/Behat/master/README.md) — README oficial do Behat com instalação via Composer, versão de desenvolvimento, política SemVer/BC, mantenedores e canais de apoio.; consultado em 2026-10-03.
