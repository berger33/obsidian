---
id: software.testes.tranche24.001808
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
fontes: ["https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md", "https://github.com/AFLplusplus/LibAFL"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O artigo científico: fuzzer modular e reutilizável

## Em uma frase
O README traz a citação oficial para trabalho acadêmico: Fioraldi, Maier, Zhang e Balzarotti, "LibAFL: A Framework to Build Modular and Reusable Fuzzers", nos Proceedings da 29th ACM Conference on Computer and Communications Security (CCS), série CCS '22, novembro de 2022, Los Angeles — com o BibTeX pronto e o PDF linkado na página do laboratório (s3.eurecom.fr).

## Por que importa
O design "components de fuzzer como peças" tem artigo revisado por pares; para relatórios de adoção ou trabalho de pesquisa, a base conceitual está documentada em venue de primeira linha em vez de apenas no código.

## Como funciona
Cite o paper ao publicar resultados obtidos com o LibAFL; para entender as decisões de arquitetura (por que LLMP, por que componentes substituíveis), o texto do CCS'22 é a fonte primária apontada pelo próprio README.

## Exemplo
O material didático adicional citado pelo README inclui o talk de RC3 ("Fuzzers Like LEGO") e o do Fuzzcon Europe com discussão passo a passo dos exemplos — este último marcado pelo próprio projeto como "a bit but not so much outdated".

## Limites e trade-offs
O README avisa que as apresentações podem envelhecer (a palavra do projeto sobre o Fuzzcon talk); para código corrente, o docs.rs e os exemplos continuam sendo a verdade executável.

## Como verificar
O bloco "Cite" e a seção Resources do README oficial fornecem a referência completa e os talks.

## Conexões
- [[libafl-examples-first]] — Veja também: O caminho de partida: ler os exemplos, just run.
- [[libafl-community-license]] — Veja também: Comunidade, depuração e a dupla licença MIT/Apache.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
