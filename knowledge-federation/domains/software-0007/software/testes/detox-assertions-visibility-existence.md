---
id: software.testes.tranche16.000955
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
fontes: ["https://wix.github.io/Detox/docs/introduction/getting-started", "https://github.com/wix/Detox"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Detox: distinguir visível de existente

## Em uma frase
As asserções de visibilidade verificam o que está apresentado na tela, enquanto as de existência apenas confirmam que o elemento está montado na hierarquia.

## Por que importa
Um item fora da área visível pode existir sem estar apresentado, e tratar os dois estados como equivalentes produz verificação mais fraca do que a intenção do teste.

## Como funciona
Escolha a asserção conforme a pergunta: visibilidade para o que a pessoa usuária deve enxergar, existência para componentes montados fora da dobra.

## Exemplo
Uma mensagem de erro que deve aparecer para a pessoa usuária pede verificação de visibilidade; um item de lista carregado fora da tela pode ser verificado por existência e depois por rolagem.

## Limites e trade-offs
Existência não garante conteúdo correto nem interatividade, então a asserção precisa ser combinada com verificação de texto quando o valor importa.

## Como verificar
Role a tela até o elemento e compare o resultado das duas asserções antes e depois da rolagem para fixar a diferença observada.

## Conexões
- [[detox-waitfor-explicit]] — Veja também: Detox: esperar condições que a ferramenta não observa.
- [[detox-disable-synchronization-scope]] — Veja também: Detox: restringir a desativação da sincronização.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — repositório oficial](https://github.com/wix/Detox) — visão geral do projeto, documentação complementar e exemplos; consultado em 2026-10-03.
