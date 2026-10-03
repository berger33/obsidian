---
id: software.testes.tranche17.001073
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.locust.io/en/stable/running-distributed.html", "https://github.com/locustio/locust"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: distribuir a carga entre processos

## Em uma frase
A execução pode dividir usuários entre vários processos trabalhadores coordenados por um processo principal, ampliando a capacidade de gerar carga.

## Por que importa
Uma única máquina deixa de acompanhar a taxa desejada, e o gargalo passa a ser o gerador em vez do serviço avaliado.

## Como funciona
Inicie o processo principal, conecte trabalhadores pelo mesmo endereço e dimensione os recursos de rede e de CPU antes de aumentar a carga.

## Exemplo
Uma campanha de alta taxa pode usar vários processos trabalhadores, mantendo o resumo consolidado no processo principal.

## Limites e trade-offs
Estatísticas consolidadas dependem do canal entre principal e trabalhadores, e perda de um trabalhador reduz a carga efetiva sem interromper o teste.

## Como verificar
Compare a taxa alcançada com um e com vários trabalhadores, observando o consumo de recursos da máquina geradora.

## Conexões
- [[locust-tags-and-selection]] — Veja também: Locust: selecionar tarefas por etiquetas.
- [[locust-headless-and-ci]] — Veja também: Locust: executar sem interface e automatizar.

## Fontes
- [Locust — Distributed execution](https://docs.locust.io/en/stable/running-distributed.html) — processo principal, trabalhadores e consolidação de estatísticas; consultado em 2026-10-03.
- [Locust — repositório oficial](https://github.com/locustio/locust) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
