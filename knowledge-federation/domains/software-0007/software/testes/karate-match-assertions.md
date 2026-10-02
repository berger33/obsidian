---
id: software.testes.tranche15.000911
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
fontes: ["https://karatelabs.github.io/karate/", "https://karatelabs.github.io/karate/#data-driven-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: usar match e marcadores fuzzy

## Em uma frase
O comando `match` compara respostas com valores esperados e aceita marcadores como `#string`, `#number` e `#[]` para validar estrutura sem fixar conteúdo volátil.

## Por que importa
Comparar o corpo inteiro com igualdade exata quebra a cada campo novo do serviço, enquanto validar apenas o status deixa passar contrato incorreto.

## Como funciona
Afirme os campos de negócio com valores concretos e use marcadores para tipo, presença e coleções, escolhendo entre igualdade estrita e verificação por conteúdo.

## Exemplo
`match response == { id: '#number', nome: '#string', itens: '#[]' }` confirma forma e tipos sem depender de identificadores gerados na execução.

## Limites e trade-offs
Marcadores permissivos demais aceitam qualquer conteúdo do tipo declarado; a asserção continua válida apenas se o campo for realmente exercitado em outros cenários.

## Como verificar
Altere um tipo no serviço de teste e confirme que a asserção falha; depois adicione um campo extra e verifique a diferença entre igualdade e verificação por conteúdo.

## Conexões
- [[karate-gherkin-builtin-steps]] — Veja também: Karate: escrever API tests em Gherkin com steps embutidos.
- [[karate-config-js]] — Veja também: Karate: separar configuração por ambiente.

## Fontes
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
- [Karate — Data driven tests](https://karatelabs.github.io/karate/#data-driven-tests) — tabelas, Examples, CSV e laços em feature files; consultado em 2026-10-02.
