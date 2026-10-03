---
id: software.testes.tranche22.001575
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://pester.dev/docs/usage/mocking", "https://pester.dev/docs/quick-start"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: Mock substitui qualquer comando

## Em uma frase
Mock substitui o comportamento de um comando existente por uma implementação alternativa, e a documentação garante que isso vale para qualquer comando do PowerShell — cmdlet, função ou script — servindo para "shimar" uma camada de dados ou isolar funções complexas.

## Por que importa
Em scripts de administração o custo de testar está em acessar AD, Azure ou sistema de arquivos; o Mock permite fingir exatamente esses pontos de contato sem tocar no ambiente real.

## Como funciona
Declare Mock NomeDoComando { scriptblock de resposta } dentro do bloco de teste ou do seu BeforeEach, e o comando passa a responder pelo mock apenas naquele escopo.

## Exemplo
Mock Get-Version {return 1.1} e Mock Get-NextVersion {return 1.2} preparam o cenário "há mudanças" para exercitar BuildIfChanged sem nenhum módulo real.

## Limites e trade-offs
Mockar demais transforma o teste em fotografia da própria implementação; a página recomenda explicitamente não mockar funções que já têm testes próprios.

## Como verificar
Injete um Mock com scriptblock vazio Mock Build {} e confirme que o código sob teste executa sem efeitos colaterais reais.

## Conexões
- [[pester-assertions-should]] — Veja também: Pester: asserções Should e a mensagem de falha.
- [[pester-mock-verification]] — Veja também: Pester: Should-Invoke, -Times e -Verifiable.

## Fontes
- [Pester — Mocking](https://pester.dev/docs/usage/mocking) — Mock, Should-Invoke, escopo, natives e classes; consultado em 2026-10-03.
- [Pester — Quick start](https://pester.dev/docs/quick-start) — mini-DSL, convenção de nomes e primeira execução; consultado em 2026-10-03.
