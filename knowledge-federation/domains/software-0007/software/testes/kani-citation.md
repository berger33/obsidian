---
id: software.testes.tranche24.001787
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
fontes: ["https://raw.githubusercontent.com/model-checking/kani/main/README.md", "https://github.com/model-checking/kani"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Base acadêmica rastreável: o paper ASE 2026

## Em uma frase
Para uso em pesquisa, o README fornece a citação oficial: o paper "Kani: A Model Checker for Rust" publicado nos Proceedings da 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26, outubro de 2026, Munique), com DOI 10.1145/3832783.3834499, formato ACM e BibTeX completos, e uma cópia legível por máquina em CITATION.cff que alimenta o botão "Cite this repository" do GitHub.

## Por que importa
Ferramentas de verificação aparecem e somem; aqui a afirmação de correção do projeto tem trilha pública revisada por pares, e o CITATION.cff elimina a etapa manual — o mesmo registro serve para relatórios técnicos e para o README do projeto que depende dele.

## Como funciona
Ao publicar resultados que dependem do Kani, cite pelo DOI oficial; em repositórios internos, adicione a referência no documento de decisão técnica com o link do paper — a existência do CITATION.cff torna o Cite button no lado direito do repositório um atalho verificável.

## Exemplo
A lista completa de autores (Delmas, Hassan, Hu, Kumar, Monteiro, Nguyen, Palacios, Val, Tautschnig, Adam, Schwartz-Narbonne, Zech) e as 13 páginas do artigo constam na referência formatada do próprio README.

## Limites e trade-offs
A citação cobre o estado do artefato de pesquisa na data da conferência; notas de release e documentação do livro continuam sendo a fonte para uso de engenharia no dia a dia.

## Como verificar
O bloco "Citing Kani" do README oficial contém o formato ACM, o BibTeX e a referência ao CITATION.cff.

## Conexões
- [[kani-github-action]] — Veja também: CI nativo: o action model-checking/kani-github-action.
- [[kani-license]] — Veja também: Licenciamento espelhado no do próprio Rust.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial model-checking/kani](https://github.com/model-checking/kani) — Repositório oficial do Kani Rust Verifier no GitHub com código-fonte, workflows, CITATION.cff e política de segurança.; consultado em 2026-10-03.
