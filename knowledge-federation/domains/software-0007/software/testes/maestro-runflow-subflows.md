---
id: software.testes.tranche15.000904
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
fontes: ["https://docs.maestro.dev/api-reference/commands/runflow", "https://docs.maestro.dev/api-reference/commands"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maestro: reutilizar fluxos com runFlow

## Em uma frase
O comando `runFlow` executa comandos de outro arquivo, aceita variáveis de ambiente e pode ser condicionado à visibilidade de um elemento.

## Por que importa
Repetir a sequência de login em cada cenário multiplica pontos de manutenção e faz uma mudança de interface exigir edição em vários arquivos.

## Como funciona
Extraia sequências estáveis para subfluxos, parametrize o que varia por ambiente e use a condição de visibilidade para passos opcionais.

## Exemplo
`- runFlow: { file: login.yaml, env: { USUARIO: "ada" } }` reaproveita o login, e `- runFlow: { when: { visible: "Aceitar" }, commands: [ { tapOn: "Aceitar" } ] }` trata o banner opcional.

## Limites e trade-offs
Subfluxos compartilhados criam acoplamento entre cenários; um deles precisa ser estável e ter contrato claro, sem depender de estado deixado pelo fluxo chamador.

## Como verificar
Execute o fluxo chamador isoladamente e depois em conjunto com outros que usam o mesmo subfluxo, verificando que o resultado não depende da ordem.

## Conexões
- [[maestro-assertions-and-waits]] — Veja também: Maestro: afirmar visibilidade e esperar condição.
- [[maestro-input-and-keyboard]] — Veja também: Maestro: preencher campos e controlar teclado.

## Fontes
- [Maestro — runFlow](https://docs.maestro.dev/api-reference/commands/runflow) — reuso de fluxos, subflows, variáveis de ambiente e condições; consultado em 2026-10-02.
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
