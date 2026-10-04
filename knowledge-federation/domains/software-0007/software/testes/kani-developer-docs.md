---
id: software.testes.tranche24.001789
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

# Por dentro: developer docs e política de segurança

## Em uma frase
Além do uso, o README abre as portas de manutenção: contribuição regida pela developer documentation do livro oficial (model-checking.github.io/kani/dev-documentation.html) e reporte de vulnerabilidades governado pela SECURITY policy do repositório (github.com/model-checking/kani/security/policy), ambas linkadas do README como destinos canônicos.

## Por que importa
Verificadores erram — a existência de um policy linkado para security e de um canal de desenvolvimento no livro define como reportar um contraexemplo falso ou um UB não pego, que é a pergunta que separa adoção séria de curiosidade.

## Como funciona
Antes de abrir issue de bug, classifique: falha de verificação (resultado errado) segue a trilha da developer docs; suspeita de vulnerabilidade na ferramenta ou no uso seguro segue a SECURITY policy do GitHub — cada uma tem o próprio formato pedido pelos mantenedores.

## Exemplo
O fluxo completo que o README prescreve: interested in contributing abre dev-documentation.html; para informação de segurança, SECURITY aponta a policy no próprio repositório — links diretos no final do README.

## Limites e trade-offs
O README funciona como índice desses dois documentos; os procedimentos detalhados (escopo, respostas esperadas) estão no livro e no template do repo, que o projeto pode atualizar sem tocar o README.

## Como verificar
A dupla de links developer docs e security policy, e o texto que os introduz, foi conferida nas seções finais do README oficial.

## Conexões
- [[kani-license]] — Veja também: Licenciamento espelhado no do próprio Rust.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial model-checking/kani](https://github.com/model-checking/kani) — Repositório oficial do Kani Rust Verifier no GitHub com código-fonte, workflows, CITATION.cff e política de segurança.; consultado em 2026-10-03.
