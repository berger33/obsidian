---
id: software.testes.tranche25.001943
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
fontes: ["https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md", "https://github.com/BurntSushi/quickcheck"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Política de MSRV (Rust 1.85.0) e o papel de rand como dependência pública

## Em uma frase
A seção Minimum Rust version policy estabelece que a versão mínima suportada do compilador rustc (MSRV) desta crate é 1.85.0 e explica a regra de evolução: a MSRV pode subir em atualizações minor (por exemplo, de 1.0 para 1.y com y > 0), mas não em atualizações patch (1.0.z manterá a mesma MSRV de 1.0); por fim, ressalva que rand é atualmente uma dependência pública do quickcheck, de modo que o quickcheck difere para a política de MSRV do rand caso ela seja mais agressiva.

## Por que importa
Em ambientes corporativos ou distribuições Linux que congelam o compilador Rust, entender que patches 1.0.z preservam a MSRV mas que a dependência pública rand pode puxar requisitos de compilador evita quebras inesperadas de build ao atualizar o Cargo.lock.

## Como funciona
Verifique se o toolchain do projeto atende ao piso rustc 1.85.0 declarado no README e fixe o Cargo.lock em pipelines de CI que não atualizam o compilador continuamente.

## Exemplo
Como rand faz parte da API pública do quickcheck (usado na geração de valores Arbitrary), a árvore de versões do rand influencia diretamente a compatibilidade de compilador da crate.

## Limites e trade-offs
A política declarada no README afirma que a crate será em geral conservadora quanto à versão mínima do Rust, sujeita apenas ao limite imposto pela dependência pública rand.

## Como verificar
Conferi a seção Minimum Rust version policy no README oficial de BurntSushi/quickcheck.

## Conexões
- [[quickcheck-logging-and-default-features]] — Veja também: Diagnóstico com RUST_LOG=quickcheck e as features padrão use_logging e regex.
- [[quickcheck-arbitrary-compatibility-caveat]] — Veja também: Compatibilidade SemVer: implementações de Arbitrary podem mudar e achar bugs novos.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Repositório oficial BurntSushi/quickcheck](https://github.com/BurntSushi/quickcheck) — Repositório oficial do quickcheck para Rust no GitHub com código-fonte, quickcheck_macros e examples/reverse_single.rs.; consultado em 2026-10-03.
