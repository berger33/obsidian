---
id: software.testes.tranche12.000613
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/", "https://rspec.info/features/3-13/rspec-core/command-line/tag/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: limitar hooks ao escopo necessário

## Em uma frase
Hooks `before` e `after` podem ser definidos para exemplos ou grupos e participam de uma ordem que depende do escopo.

## Por que importa
Estado compartilhado em hook de grupo afeta todos os exemplos descendentes, ao passo que setup de exemplo permite isolamento mais previsível.

## Como funciona
Use hooks de exemplo para dados mutáveis por caso, mantenha setup de grupo para preparação realmente compartilhável e filtre hooks globais por metadata quando o custo não se aplica a toda a suite.

## Exemplo
Uma conexão cara pode ser aberta no grupo, enquanto cada exemplo cria uma transação independente que é revertida no hook correspondente.

## Limites e trade-offs
Inicializar estado gravável uma vez no grupo pode fazer o resultado depender da ordem e expor interferência entre exemplos.

## Como verificar
Instrumente chamadas de hook em um grupo aninhado e confirme quais exemplos recebem cada preparação e limpeza.

## Conexões
- [[rspec-around-hook-envelope]] — Veja também: RSpec 3.13: `around` como envelope de um exemplo.
- [[rspec-composable-matchers-estruturas]] — Veja também: RSpec 3.13: compor matchers para respostas estruturadas.

## Fontes
- [RSpec 3.13 — Before and after hooks](https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/) — escopo e ordem de before/after hooks por exemplo e grupo; consultado em 2026-10-02.
- [RSpec 3.13 — Metadata filtering](https://rspec.info/features/3-13/rspec-core/command-line/tag/) — seleção e exclusão de exemplos por tags/metadata; consultado em 2026-10-02.
