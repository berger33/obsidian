---
id: software.testes.tranche12.000617
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
fontes: ["https://rspec.info/features/3-13/rspec-core/command-line/tag/", "https://rspec.info/features/3-13/rspec-core/example-groups/shared-examples/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: filtrar exemplos por metadata

## Em uma frase
Metadata é associada a example groups e exemplos e pode selecionar quais casos entram numa execução da CLI.

## Por que importa
Tags ajudam a separar integrações, requisitos ambientais ou suítes lentas sem mover exemplos para arquivos artificiais.

## Como funciona
Atribua símbolos ou pares de metadata a grupos e use a opção `--tag` para incluir ou excluir valores com política documentada.

## Exemplo
Uma pipeline pode selecionar exemplos que dependem de um serviço externo com a tag `:external`, preservando os testes unitários na execução padrão.

## Limites e trade-offs
Uma tag herdada no grupo pode incluir exemplos descendentes não planejados e uma configuração que exclui categorias pode esconder cobertura inadvertidamente.

## Como verificar
Liste a suite com e sem o filtro e compare os exemplos descobertos antes de aplicar a tag a um grupo de nível superior.

## Conexões
- [[rspec-message-argument-constraints]] — Veja também: RSpec 3.13: restringir argumentos de expectativas de mensagem.
- [[rspec-random-order-seed]] — Veja também: RSpec 3.13: reproduzir falhas de ordem aleatória.

## Fontes
- [RSpec 3.13 — Metadata filtering](https://rspec.info/features/3-13/rspec-core/command-line/tag/) — seleção e exclusão de exemplos por tags/metadata; consultado em 2026-10-02.
- [RSpec 3.13 — Shared examples](https://rspec.info/features/3-13/rspec-core/example-groups/shared-examples/) — inclusão de grupos compartilhados, parâmetros, carregamento e escopo; consultado em 2026-10-02.
