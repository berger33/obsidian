---
id: software.testes.tranche17.001074
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
fontes: ["https://docs.locust.io/en/stable/quickstart.html", "https://github.com/locustio/locust"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: executar sem interface e automatizar

## Em uma frase
A execução sem interface aceita número de usuários, velocidade de criação e tempo, grava resumos em arquivos e permite integrar a carga ao pipeline.

## Por que importa
Verificações recorrentes exigem comando reproduzível e resultado consumível, sem depender de observação manual da interface.

## Como funciona
Declare todos os parâmetros na linha de comando, grave o resumo e o histórico em arquivos e arquive-os como evidência da execução.

## Exemplo
Uma verificação noturna pode rodar com número fixo de usuários, gravar estatísticas e publicar o resultado como artefato do trabalho.

## Limites e trade-offs
Ambientes compartilhados do pipeline introduzem variação, e limites derivados de uma única execução produzem decisões frágeis.

## Como verificar
Repita a execução automatizada em dois momentos e compare os arquivos de estatísticas antes de definir qualquer limite de aprovação.

## Conexões
- [[locust-distributed-execution]] — Veja também: Locust: distribuir a carga entre processos.
- [[locust-limits-and-interpretation]] — Veja também: Locust: interpretar resultados com cautela.

## Fontes
- [Locust — Quickstart](https://docs.locust.io/en/stable/quickstart.html) — primeira execução, parâmetros de linha de comando e resumo de estatísticas; consultado em 2026-10-03.
- [Locust — repositório oficial](https://github.com/locustio/locust) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
