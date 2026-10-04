---
id: software.testes.tranche20.001389
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://keploy.io/docs/", "https://github.com/keploy/keploy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Keploy: gerar testes a partir de tráfego real

## Em uma frase
A ferramenta observa o tráfego recebido pela aplicação em execução e grava cada pedido com a resposta devolvida como um caso de teste.

## Por que importa
Partir do comportamento real cobre entradas que o time não imaginaria escrever à mão e reduz o esforço de autoria.

## Como funciona
Execute a aplicação com a ferramenta ativa, exercite os fluxos relevantes e versione os artefatos gerados.

## Exemplo
Um fluxo de cadastro exercitado manualmente uma vez vira caso de teste reutilizável nas execuções seguintes.

## Limites e trade-offs
Tráfego gravado reflete apenas os caminhos exercitados, e gravar sem revisar pode registrar dados sensíveis junto do caso.

## Como verificar
Conte os casos gerados após a primeira gravação e confirme que cada pedido exercitado tem artefato correspondente.

## Conexões
- [[keploy-dependency-mocks]] — Veja também: Keploy: registrar dependências como mocks.

## Fontes
- [Keploy — Documentação](https://keploy.io/docs/) — instalação, gravação de tráfego, repetição e integração; consultado em 2026-10-03.
- [Keploy — repositório oficial](https://github.com/keploy/keploy) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
