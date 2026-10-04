---
id: software.testes.tranche22.001627
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
fontes: ["https://tavern.readthedocs.io/en/latest/", "https://taverntesting.github.io/documentation"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Tavern: a biblioteca embutível

## Em uma frase
Além de plugin e CLI, o Tavern expõe a biblioteca Python para quem integra o motor de testes ao próprio framework ou pipeline de CI — a mesma máquina de stages, chamada por código.

## Por que importa
Quebras de contrato entre times que não usam pytest (runners caseiros, gateways internos) ganham uma API estável em vez de shell-out para tavern-ci.

## Como funciona
A frase da doc: "integrate Tavern into your own test framework or continuous integration setup using the Python library".

## Exemplo
O projeto foi iniciado em 2017 justamente para endereçar as lacunas que os times viam nos frameworks disponíveis à época.

## Limites e trade-offs
Usar a lib diretamente significa abrir mão do discovery e reporting do pytest: você mesmo coleta, executa e publica resultado.

## Como verificar
Chame a API da biblioteca num script Python contra o exemplo público do quickstart e imprima o status por conta própria.

## Conexões
- [[tavern-vs-postman]] — Veja também: Tavern: contra Postman, Insomnia e pyresttest.
- [[tavern-examples-ecosystem]] — Veja também: Tavern: exemplos e documentação viva.

## Fontes
- [Tavern — documentação inicial](https://tavern.readthedocs.io/en/latest/) — proposta, quickstart YAML, CLI e comparativos; consultado em 2026-10-03.
- [Tavern — documentação completa](https://taverntesting.github.io/documentation) — documentação oficial linkada pela página inicial; consultado em 2026-10-03.
