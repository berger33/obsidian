---
id: software.testes.tranche21.001559
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/CodeIntelligenceTesting/jazzer", "https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jazzer: sanitizers que denunciam a vulnerabilidade

## Em uma frase
Os sanitizers (bug detectors) monitoram a execução contra padrões de risco como SSRF, path traversal e injeção de comando, devolvendo feedback que orienta a geração de entradas.

## Por que importa
Um crash não diz o que você queria saber; os hooks transformam a corrida em busca dirigida ao comportamento vulnerável, não apenas ao ponto de exceção.

## Como funciona
Escolha os sanitizers relevantes ao seu domínio e desative os que atrapalham via disabled_hooks nos argumentos, conforme a documentação de configuração.

## Exemplo
Um parser de URI com hook de rede ligado produz inputs que chegam a chamar alvos proibidos — e o relatório aponta o par risco/input.

## Limites e trade-offs
Hooks têm custo de instrumentação em toda chamada monitorada, e desligar o errado apaga justamente a classe de bugs buscada; valide a lista por projeto.

## Como verificar
Ative um sanitizer simples em alvo neutro e confirme que a ausência de risco mantém a corrida verde.

## Conexões
- [[jazzer-seeding-junit]] — Veja também: Jazzer: sementes vindas de parâmetros do JUnit.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — Arguments and configuration options](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md) — argumentos do agente e hooks desativáveis; consultado em 2026-10-03.
