---
id: software.testes.tranche25.001944
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
fontes: ["https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md", "https://docs.rs/quickcheck"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Compatibilidade SemVer: implementações de Arbitrary podem mudar e achar bugs novos

## Em uma frase
A seção Compatibility traz um aviso essencial de engenharia: a crate considera as implementações de Arbitrary fornecidas como detalhes de implementação; as estratégias de geração e encolhimento podem mudar ao longo do tempo em releases compatíveis com SemVer, o que pode causar novas falhas na sua suíte de testes — presumivelmente pela descoberta de novos bugs graças à geração de um novo tipo de testemunha (witness).

## Por que importa
Diferentemente de um teste determinístico com entradas fixas, um gerador baseado em propriedades que melhora sua cobertura de casos de borda numa atualização minor/patch está cumprindo seu papel ao revelar um bug latente no código do usuário, razão pela qual o projeto não trata ajustes nos geradores Arbitrary como quebra de compatibilidade SemVer.

## Como funciona
Ao atualizar o quickcheck e observar uma propriedade falhar pela primeira vez no CI, inspecione a testemunha reportada antes de culpar a atualização: na maioria das vezes a nova distribuição de Arbitrary encontrou um caso de borda real no código testado.

## Exemplo
Uma mudança interna na estratégia de geração de inteiros ou floats em uma versão semver-compatível pode passar a gerar um valor extremo que antes não era sorteado e expor um bug antigo na função verificada.

## Limites e trade-offs
Se uma propriedade faz suposições implícitas sobre quais valores o gerador padrão de um tipo nunca produziria, essa suposição deve ser transformada em pré-condição explícita no teste (com TestResult::discard ou um tipo wrapper próprio).

## Como verificar
Conferi a seção Compatibility no README oficial do quickcheck.

## Conexões
- [[quickcheck-msrv-policy-and-rand]] — Veja também: Política de MSRV (Rust 1.85.0) e o papel de rand como dependência pública.
- [[quickcheck-testable-trait-polymorphism]] — Veja também: Por que propriedades são polimórficas: o trait Testable e a função quickcheck.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Crate quickcheck no docs.rs](https://docs.rs/quickcheck) — Documentação oficial da API da crate quickcheck no docs.rs.; consultado em 2026-10-03.
