---
id: software.testes.tranche15.000948
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/", "https://nexte.st/docs/running/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: reconhecer o limite dos doctests

## Em uma frase
O nextest executa binários de teste compilados e não cobre exemplos de documentação, que continuam precisando do comando clássico do Cargo.

## Por que importa
Assumir que o nextest substitui integralmente o executor padrão deixa exemplos de documentação sem verificação e reduz a cobertura sem que ninguém perceba.

## Como funciona
Mantenha uma etapa separada para verificações de documentação e considere os dois comandos como partes complementares da mesma suíte.

## Exemplo
`cargo test --doc` verifica os exemplos embutidos na documentação, enquanto `cargo nextest run` cobre os testes compilados das demais categorias.

## Limites e trade-offs
Exemplos que não compilam são apontados apenas pelo comando de documentação, e a separação aumenta o número de passos que o pipeline precisa orquestrar.

## Como verificar
Execute os dois comandos em uma revisão com exemplo quebrado e confirme qual deles detecta o problema, garantindo a cobertura de ambos no pipeline.

## Conexões
- [[nextest-archives]] — Veja também: nextest: reutilizar binários com archive.
- [[nextest-listing-and-ignored]] — Veja também: nextest: listar e reexecutar testes ignorados.

## Fontes
- [nextest — Documentation](https://nexte.st/docs/) — visão geral do runner, instalação e operação; consultado em 2026-10-02.
- [nextest — Running tests](https://nexte.st/docs/running/) — execução, filtros, saída, listagem e testes ignorados; consultado em 2026-10-02.
