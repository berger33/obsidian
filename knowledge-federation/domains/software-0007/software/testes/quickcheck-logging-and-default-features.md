---
id: software.testes.tranche25.001942
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

# Diagnóstico com RUST_LOG=quickcheck e as features padrão use_logging e regex

## Em uma frase
Na seção Installation, o README observa (N.B.) que definir a variável de ambiente RUST_LOG=quickcheck habilita mensagens info! mostrando informações úteis como o número de testes que passaram, frisando que isso não é necessário para exibir os contraexemplos (witnesses) quando há falha; logo abaixo, lista as duas features da crate habilitadas por padrão: "use_logging" (habilita mensagens de log governadas por RUST_LOG) e "regex" (habilita o uso de expressões regulares com env_logger).

## Por que importa
Durante a execução normal, testes que passam ficam silenciosos; saber ativar RUST_LOG=quickcheck permite confirmar quantos casos foram efetivamente gerados e aprovados, enquanto quem quer enxugar a árvore de dependências de compilação pode desabilitar as features padrão use_logging e regex.

## Como funciona
Rode RUST_LOG=quickcheck cargo test quando quiser ver no log a contagem de testes passados por propriedade; se não precisar de suporte a log e env_logger, desative as default features da crate no Cargo.toml.

## Exemplo
Mesmo sem definir RUST_LOG=quickcheck no ambiente, qualquer falha de propriedade continua imprimindo automaticamente a testemunha (witness) mínima encontrada pelo shrinking.

## Limites e trade-offs
As features "use_logging" e "regex" vêm ativadas por padrão (Enabled by default); projetos com restrição severa de tempo de compilação em dev-dependencies devem observar a presença de env_logger/regex nessas features.

## Como verificar
Conferi a nota N.B. e a lista Crate features na seção Installation do README oficial.

## Conexões
- [[quickcheck-macro-vs-attribute]] — Veja também: Duas formas de declarar propriedades: a macro quickcheck! e o atributo #[quickcheck].
- [[quickcheck-msrv-policy-and-rand]] — Veja também: Política de MSRV (Rust 1.85.0) e o papel de rand como dependência pública.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Crate quickcheck no docs.rs](https://docs.rs/quickcheck) — Documentação oficial da API da crate quickcheck no docs.rs.; consultado em 2026-10-03.
