---
id: software.testes.tranche16.000956
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

# Detox: restringir a desativação da sincronização

## Em uma frase
A sincronização pode ser desativada e reativada durante o teste, delimitando um trecho em que a ferramenta não aguarda operações pendentes.

## Por que importa
Animações contínuas ou fluxos de longa duração impedem a estabilização, e sem um trecho controlado a execução trava esperando algo que nunca termina.

## Como funciona
Isole a menor região possível entre a desativação e a reativação, acompanhe-a de uma espera por condição observável e documente por que a exceção é necessária.

## Exemplo
Um indicador de carregamento animado infinitamente pode ser contornado desativando a sincronização apenas durante o toque e aguardando o resultado por asserção explícita.

## Limites e trade-offs
Esquecer de reativar afeta os casos seguintes, e usar a desativação como padrão elimina justamente a proteção contra corridas que torna a ferramenta valiosa.

## Como verificar
Execute o caso com o trecho isolado e confirme que os testes posteriores voltaram a aguardar operações, verificando que nenhum estado ficou alterado.

## Conexões
- [[detox-assertions-visibility-existence]] — Veja também: Detox: distinguir visível de existente.
- [[detox-device-actions]] — Veja também: Detox: usar ações de dispositivo no fluxo.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — repositório oficial](https://github.com/wix/Detox) — visão geral do projeto, documentação complementar e exemplos; consultado em 2026-10-03.
