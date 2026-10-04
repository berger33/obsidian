---
id: software.testes.tranche16.000968
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://www.artillery.io/docs/get-started/first-test", "https://github.com/artilleryio/artillery"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: escolher entre execução rápida e arquivo

## Em uma frase
O comando de execução rápida parte de um alvo e gera um cenário mínimo para verificação imediata, enquanto a execução por arquivo usa a definição completa.

## Por que importa
Uma verificação rápida serve para confirmar conectividade antes de investir na modelagem, mas não substitui o teste com fases e limites.

## Como funciona
Use a forma rápida para validar alvo e credenciais e migre para o arquivo assim que houver jornada, limites ou dados de entrada.

## Exemplo
Verificar a saúde de um serviço recém-publicado pode ser feito com alguns segundos de carga leve antes de rodar a suíte completa.

## Limites e trade-offs
A forma rápida não é versionada e desaparece ao fechar o terminal, de modo que qualquer verificação recorrente precisa virar arquivo de teste.

## Como verificar
Execute a forma rápida contra um alvo conhecido e compare com o resultado do mesmo alvo pela execução por arquivo.

## Conexões
- [[artillery-expect-plugin]] — Veja também: Artillery: verificar respostas com asserções.
- [[artillery-scenario-weights]] — Veja também: Artillery: distribuir carga entre cenários.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
